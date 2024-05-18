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

## Implementation Plan
- ~~project structure~~ base structure found
- ~~opengl setup~~ rainbow triangle achieved
- ~~dots bouncing around~~ we have those dots bouncing
- movement speed slider (only required debug feature)
- conversation within radius, paused movement until conversation ends
    - start w/ 5s pause
- rudimentary conversations (no RAG, villagers are dumb)
    - how are personalities structured?
- RAG -- how conversations happen
- tokens used vs max tokens
- reproduction
THAT'S MVP

- debug features:
    - Villagers know about death.
    - Villagers know how long until they die
    - Villagers know their goal (reproduce)
    - (stretch) event logging
    - (stretch) number of villagers
- stretch goals:
    - more villager traits than personality
    - dynamic environments -- obstacles or zones that influence movement or 
      interaction
    - emotional simulation -- add an emotional layer to the villagers, where
      their mood influences conversation topics or reproduction likelihood.
      Affected by interactions/environment.
    - advanced logic -- more sophisticated rules on interaction, some villagers
      like interacting with certain personalities or avoid some based on past
      interactions
    - memories/forgetting
    - aging -- not only run out of tokens, but age over time which affects move
      speed, interaction frequency, etc.
    - health + needs -- hunger, thirst, rest, disease or injury
    - complex social dynamics
        - reputation system -- renown/infamy
        - friendships and rivalries -- defined relationships between villagers
    - villager living spaces
    - villager work posts
    - brainstorm monetization
    - trade + economy
        - resource gathering
        - trade between villagers
    - advance reproduction
        - include additional traits
        - genetic system
    - player interaction
    - quests + advancement (daily's?)
        - bonus XP(? not even implemented yet), faster resource gathering, villager disputes
