# Idle Game Prototype

This project is a prototype for an LLM-powered idle game that simulates interactions between villagers in a dynamic and emergent settlement environment. Villagers converse, remember, and evolve relationships over time, with the player acting as an overseer. Below is a detailed breakdown of the project and its current state.

This version served as a company showcase for Andgo Systems. The project has since evolved; the current project utilizes Godot.

## Features
### Core Functionality
- Villager Conversations: Villagers engage in dialogues that shape their relationships and memories.

- Memory System: Villagers remember interactions and opinions about others, influencing future conversations.

- Emergent Behavior: Villagers display dynamic behavior based on past experiences and their unique personality traits.

### Currently Implemented
- Simple Pathfinding: Limited movement logic for villagers (they just kinda bounce around).

- Conversational AI: Conversations between villagers driven by GPT-style LLMs.

- Memory Storage: Villagers retain memories of past conversations and interactions in a structured JSON format.

- Prototyping Stack:
  - Python 3.10 with pygame for GUI.
  - OpenAI API (using GPT-4o and GPT-3.5-turbo).

## Tech Stack
### Design Consideration
- LLMs are bulky. Out of the 12GB of VRAM I have on my home PC, I’d want to use 12GB for the best-performing LLM.
  - “Best performing” here means a few things: reliable, creative, intelligent, etc. Some very quantitative metrics.
- To that end:
    - I started implementing this in C, using OpenGL. All of the heavy logic, the prompt building, and the GUI happen as close to bare metal as I want to get. Then we’d hit the LLM pipeline with Python and translate back with Cython.
    - But That takes forever to build.
    - Are these performance concerns even worth thinking about right now?
    - And I have a company presentation I want to do! So, there's a deadline on the mind.
    - I also knew a local LLM would eat up my resources and make my office uncomfortably hot. That’d make prototyping annoying.

So I settled on what I knew for rapid iteration:
  - Python 3.10 using `pygame` for the GUI
  - OpenAI API
    - tested on gpt-4o and gpt-3.5-turbo

## Villager Design

Each villager has:

- Attributes
  - ID: Unique identifier.
  - Personality Traits: Three randomly selected traits from a table of 100 (33% are evil).
  - Name: Randomly chosen from a table of 100 names.
- Conversations
  - Systematic prompt engineering ensures consistent and natural dialogue.
  - Prompts are dynamically generated based on villager traits, context, and memory.
- Memory
  - Implemented using Retrieval-Augmented Generation (RAG).
  - Key memories and opinions about other villagers are stored and retrieved to influence future interactions.

## Constructing Prompts (“Prompt Engineering”)

### System Prompts

A core system prompt grounds the LLM's response. Each conversation starts with a shared context that is villager-agnostic, but with some content that makes the dialogue somewhat unique.

Example structure:

```
core_system_prompt = [
  'You are a human settler in a new settlement. There are {INITIAL_VILLAGER_COUNT-1} other villagers.',
  'It is ' + {weather},
  'You are having a conversation: ' + {conversation_starter}
]
```

### Personalization

When I get to the conversation, I immediately append the system prompt to be more specific to the villager.

```
system_prompt.extend([
  f'Your name is {villager_data["name"]}',
  f'Your core personality traits are {", ".join(villager_data["core_personality"])}.',
  'YOU ARE {villager_data["name"]}.',
])
```

### Memory Integration

I built memory out in JSON, which took on a structure like so:

```
villager_data[villager.id] = {
  'name': villager.name,
  'core_personality': villager.personality_traits,
  'memory': {
    'other_villagers': {},
    'history': [
      'You come from far away, at the behest of your king, to settle and uninhabited land.'
    ]
  },
  'flags': {
    'is_new': True
  }
}
```

That’s barebones -- but it's a nice scaffolding to implement some pretty rudimentary RAG and allows memories to influence conversations in a way that I like. If anything, it felt (and feels) like a good place to base future endeavours off of.

## Emergent Gameplay

Over time, villagers exhibit emergent behaviors based on their conversations and memories:

- Collaborative Projects: Villagers discuss and plan activities (e.g., building structures).

- Conflict and Growth: Disagreements and resolutions shape relationships.

Example:

- Villagers "Lishe" and "Cacilia" discussed building a structure, reinforcing it against storms.
  - After a few more conversations, they expressed how happy they were with their work!

- "Wynne" and "Queenie" were going to build a windbreak together -- but then Queenie wanted to prove she could do it herself.
  - The windbreak was never built, and Wynne made fun of her.

- None of these interactions actually do anything in the prototype -- they exist entirely in the memory of the individual memories. They are solely based on memories of conversations, yet they feel like progress.

Overall, I'm extremly happy with these emergent results.

## How to Run

### Requirements

- Python 3.10
- pygame
- OpenAI API access

### Running the Prototype
- Clone the repository -- you're should look mainly at the `pt` folder, however
- Install dependencies using `pip install -r requirements.txt`
- Run the game with `python main.py`