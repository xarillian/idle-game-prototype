import json
import random

from pt.config import INITIAL_VILLAGER_COUNT, MODEL_NAME
from pt.render import render_chat
from pt.villager import Villager


def retrieve_villager_data(villager_id):
    """ Retrieves stored information for a particular villager. """
    with open('pt/villager_info.json', 'r', encoding='utf-8') as villager_info_file:
        villager_data = json.load(villager_info_file)
        return villager_data[str(villager_id)]


def chat(client, system_prompt, context, villager_data, memory_key):
    """ Generates a chat response for a villager using the OpenAI API. """

    system_prompt.extend([
        f'Your name is {villager_data["name"]}. Only respond as {villager_data["name"]}. Only respond with dialogue.',
        f'Your core personality traits are:  {", ".join(villager_data["core_personality"])}. ' +
            'These personality traits are vital. They inform how behave, act, and speak. Really play into your traits.',
        f'Your personal history: {"; ".join(villager_data["memory"]["history"])}',
        'What you say should be brief.',
        'Do not use quotation marks. Do not prefix your name. ' + 
            f'For example, do not write {villager_data["name"]}: "Hello.". Do NOT.'
        f'Only respond as {villager_data["name"]}.'
    ])
    if villager_data['flags']['is_new']:
        system_prompt.append('You are new to the village.')

    for history_entry in villager_data["memory"]["history"]:
        for other_villager_name in villager_data["memory"]["other_villagers"]:
            if other_villager_name in history_entry:
                system_prompt.append(
                    f'You remember the following about {other_villager_name}: {villager_data["memory"]["other_villagers"][other_villager_name]["conversation_summaries"][-1]}'
                )

    if memory_key in villager_data['memory']['other_villagers']:
        system_prompt.extend([
            f'You remember the following about {memory_key}: {villager_data["memory"]["other_villagers"][memory_key]["conversation_summaries"]}',
            f'Your opinion on them, on a scale of -10 to 10 is: {villager_data["memory"]["other_villagers"][memory_key]["opinion"]}'
        ])
    else:
        system_prompt.append(
            f'You do not know {memory_key}.'
        )

    # TODO is this better really better as a system prompt?
    previous_conversation = []
    for entry in context:
        previous_conversation.append(f'{entry["message"]}')

    response = client.chat.completions.create(
        model=MODEL_NAME,
        messages=[
            {
                'role': 'system',
                'content': '\n'.join(system_prompt) 
            },
            {
                'role': 'user',
                'content': '\n'.join(previous_conversation)
            },
            {
                'role': 'system',
                'content': '\n' + f'REMEMBER THAT YOU ARE {villager_data["name"]}. Respond only for yourself.'
            }
        ],
        max_tokens=50,
    )

    return response.choices[0].message.content


def conversation_summarizer(client, villager, context):
    """ Summarizes a conversation using the OpenAI API. """
    conversation_text = '\n'.join([f'{entry["speaker"]}: {entry["message"]}' for entry in context])
    summary_prompt = [
        {
            'role': 'system', 
            'content': f"Be extremely brief. No yapping. Summarize the following conversation from {villager.name}'s POV:"
        },
        {
            'role': 'user', 
            'content': conversation_text
        }
    ]
    sentiment_prompt = [
        {
            'role': 'system',
            'content': f'Analyze the sentiment of the following text from the POV of {villager.name}. Respond only with "positive", "negative", or "neutral".'
        },
        {'role': 'user', 'content': conversation_text}
    ]
    memory_prompt = [
        {
            'role': 'system',
            'content': f'Give one very brief takeaway {villager.name} should take from this conversation.'
        },
        {'role': 'user', 'content': conversation_text}
    ]

    response = client.chat.completions.create(
        model=MODEL_NAME,
        messages=summary_prompt,
        max_tokens=30,
    )

    sentiment = client.chat.completions.create(  # very expensive sentiment analysis!
        model=MODEL_NAME,
        messages=sentiment_prompt,
        max_tokens=3,
    )

    memory = client.chat.completions.create(
        model=MODEL_NAME,
        messages=memory_prompt,
        max_tokens=30,
    )

    return response.choices[0].message.content, sentiment.choices[0].message.content.lower(), memory.choices[0].message.content


def villager_chat(screen, client, villager_1: Villager, villager_2: Villager):
    """ Builds a conversation between two villagers. """
    initiator, responder = (villager_1, villager_2) if random.choice([True, False]) else (villager_2, villager_1)
    initiator_data = initiator.retrieve_data()
    responder_data = responder.retrieve_data()

    with open('static/weather-conditions.txt', 'r', encoding='utf-8') as weather_file:
        weathers = weather_file.read().splitlines()
    with open('static/conversation-starters.txt', 'r', encoding='utf-8') as starters_file:
        starters = starters_file.read().splitlines()

    conversation_starter = f'{random.choice(starters).replace("{x}", initiator.name).replace("{y}", responder.name)}'
    weather = random.choice(weathers)
    core_system_prompt = [
        f'You are a human settler in a new settlement. There are {INITIAL_VILLAGER_COUNT-1} other villagers.',
        'It is ' + weather,
        'You are having a conversation: ' + conversation_starter,
    ]

    print(core_system_prompt)
    print(initiator.name + ': ' + ', '.join(initiator.personality_traits))
    print(responder.name + ': ' + ', '.join(responder.personality_traits))

    render_chat(screen, conversation_starter + '. It is ' + weather)

    conversation_storage = []
    # TODO build a short-term memory -- like "we are talking to f{responder.name}"
    for _ in range(3):
        memory_key = responder_data['name']
        response = chat(client, core_system_prompt, conversation_storage, initiator_data, memory_key)
        print(initiator.name + ': ' + response)
        conversation_storage.append({'speaker': initiator.name, 'message': response})
        render_chat(screen, initiator.name + ': ' + f'"{response}"')

        memory_key = initiator_data['name']
        response = chat(client, core_system_prompt, conversation_storage, responder_data, memory_key)
        print(responder.name + ': ' + response)
        conversation_storage.append({'speaker': responder.name, 'message': response})
        render_chat(screen, responder.name + ': ' + f'"{response}"')

    def update_memory(villager, other_villager, summary, sentiment, memory):
        villager_data = villager.retrieve_data()
        memory_key = other_villager.name

        if memory_key not in villager_data['memory']['other_villagers']:
            villager_data['memory']['other_villagers'][memory_key] = {
                'conversation_summaries': [],
                'opinion': 0
            }

        villager_data['memory']['history'].append(memory)
        villager_data['memory']['other_villagers'][memory_key]['conversation_summaries'].append(summary)
        if sentiment == 'positive':
            villager_data['memory']['other_villagers'][memory_key]['opinion'] += 1
        elif sentiment == 'negative':
            villager_data['memory']['other_villagers'][memory_key]['opinion'] -= 1

        updated_data = {
            'memory': villager_data['memory'],
            'flags': { 'is_new': False }
        }

        villager.update_data(updated_data)

    summary, sentiment, memory = conversation_summarizer(client, initiator, conversation_storage)
    update_memory(initiator, responder, summary, sentiment, memory)
    summary, sentiment, memory = conversation_summarizer(client, responder, conversation_storage)
    update_memory(responder, initiator, summary, sentiment, memory)
