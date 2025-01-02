# README
## Project Overview

This project aims to create a lightweight and efficient idle game where {nodes} reprsenting indivuals interact, move, and learn about each other using an LLM to power their brain. The game is implemented in C for core logic and performance, with Python handling LLM integration.

## Tech Considerations
C -> Core Logic
- High efficiency + low overhead

Python -> LLM Integration
- Rich ecosystem for ML, ease of use, flexible

Cython -> Communication Layer

The project needs to be small. As an idle game, the user shouldn't expect it to take up any resources -- there might be some leeway, since more technically adept users would spot it using an LLM but that's an assumption.

### New Considerations
However, C development is slow. we should start by rapidly prototyping in Python -- something it really excels at. When we have something worth showing off, we can consider performance and a re-write at that point.

## Implementation Plan
### Road to MVP
- ~~Project Structure~~ base structure found
- ~~OpenGL Setup~~ Rainbow triangle achieved
- ~~Dots bouncing around~~ We have those dots bouncing
- ~~Early prototype re-write in Python~~ snake-like
- Movment speed slider (only required debug feature)
- ~~Conversations triggered within radius, pause all movement until conversation ends. Zoom on conversation.~~ faked the zoom but that's okay
  - ~~Can be implemented with 5s pause.~~ Weren't on this step for long, but it was helpful!
- ~~Rudimentary conversations (no RAG)~~
  - ~~Base personality implementation~~ random personalities (includes evil!)
- RAG <- here
  - Basic memory about conversations + other villagers
- Villager death: compare tokens used vs max tokens
- Villager reproduction: merge personalities after an undefined trigger event and spawn new villager
  - TODO define "trigger event"

THAT'S MVP

### Important Debug Features
- +Prompt: Villagers know about death.
- +Prompt: Villagers know how long until they die.
- +Prompt: Villagers know their goal.
- Event logging.

### Future Development
- More villager traits
  - Like what?
- Dynamic environments
  - Obstacles or zones that influence movement or interaction
- Local LLM
- Emotional simulation
  - Give villagers an emotional layer, where their mood influences conversation topics or reproduction likelihood.
  - Would be affected by interactions/environment.
- Advanced logic
  - More sophisticated rules on interaction.
  - Some villagers might like interacting with certain personalities.
  - Some villagers might avoid others based on past interactions.
- Memories/Forgetfulness
- Aging
  - A villager might not only run out of tokens, but age over time which affects move speed, interaction frequence, reproductive chances, etc.
- Health + needs
  - Necessary only: hunger, thirst, rest
- Complex social dynamics
  - Reputation system (renown/infamy)
  - Friendship and rivalries (defining relationships between villagers)
- Buildings
  - Villager living spaces
  - Villager work posts
  - Passive buildings?
- Brainstorm monetizations strategies
- Trade + economy
  - Resource gathering
  - Trade between villagers
  - Interaction with other villages?
- Complex reprodcution
  - Include additional traits
  - Genetic system
  - Family tracking
- Brainstorm player interactiom
- Quests + player advancement
  - Daily's?
  - Faster resource gathering
  - Solving "villager disputes"
  - XP?
- Complex health + needs
  - Entertainment, social interaction, disease, illness, injury

