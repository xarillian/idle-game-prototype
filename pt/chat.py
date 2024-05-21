from pt.render import render_chat
from pt.villager import Villager


def villager_chat(client, screen, villager_1: Villager, villager_2: Villager):
    """ 
    Builds a conversation between two villagers.

    Args:
        client
        screen
        villager1: The first villager involved in the interaction.
        villager2: The second villager involved in the interaction.
    """
    # TODO this needs to be decomposed a lot
    response_1 = client.chat.completions.create(
        model='gpt-3.5-turbo',
          messages=[
            {
                'role': 'system', 
                'content': f'You are a medieval villager having a conversation and introducing yourself to someone. You exist to chat with them about their life. Your name is {villager_1.name}.'
            },
            {
                'role': 'system',
                'content': f'Your personality traits: {villager_1.personality_traits}'
            }
        ]
    )

    conversation_intro_1 = response_1.choices[0].message.content
    tokens_used_1 = response_1.usage.completion_tokens
    villager_1.tokens_used += tokens_used_1

    print(villager_1.tokens_used)
    print(villager_1.personality_traits)
    print(villager_1.name + ': ' + f'"{conversation_intro_1}"')
    render_chat(screen, villager_1.name + ': ' + f'"{conversation_intro_1}"')

    response_2 = client.chat.completions.create(
        model='gpt-3.5-turbo',
          messages=[
            {
                'role': 'system', 
                'content': f'You are a medieval villager. Your name is {villager_2.name}. You are responding to {villager_1.name}. You exist to chat with them about their life.'
            },
            {
                'role': 'system',
                'content': f'Your personality traits: {villager_1.personality_traits}'
            },
            {
                'role': 'user',
                'content': conversation_intro_1
            }
        ]
    )

    conversation_intro_2 = response_2.choices[0].message.content
    tokens_used_2 = response_2.usage.completion_tokens
    villager_2.tokens_used += tokens_used_2

    print(villager_2.tokens_used)
    print(villager_2.personality_traits)
    print(villager_2.name + ': ' + f'"{conversation_intro_2}"')
    render_chat(screen, villager_2.name + ': ' + f'"{conversation_intro_2}"')
