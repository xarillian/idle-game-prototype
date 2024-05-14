#ifndef VILLAGER_H
#define VILLAGER_H

#define SCREEN_WIDTH 800
#define SCREEN_HEIGHT 600

typedef struct {
    float x, y;  // position
    float dx, dy;  // direction
    int tokens; // remaining tokens
} Villager;

void initialize_villagers(int count);
void update_villagers();
// void interact_villagers();
// void cleanup_villagers();


#endif