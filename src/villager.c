#include <stdio.h>
#include <stdlib.h>
#include <time.h>

#include "villager.h"
#include "renderer.h"

#define MAX_VILLAGERS 100
#define SPEED_FACTOR 0.1

// TODO we've gotta handle height/width better

extern Villager villagers[];
extern int villager_count;

void initialize_villagers(int count) {
    if (count > MAX_VILLAGERS) {
        count = MAX_VILLAGERS;
    }

    villager_count = count;
    srand(time(NULL));
    for (int i = 0; i < villager_count; i++) {
        villagers[i].x = rand() % SCREEN_HEIGHT;
        villagers[i].y = rand() % SCREEN_WIDTH;
        villagers[i].dx = ((float)rand() / RAND_MAX) * 2 - 1;
        villagers[i].dy = ((float)rand() / RAND_MAX) * 2 - 1;
        villagers[i].tokens = 100;  // Initial token count
    }
}

void update_villagers() {
    for (int i = 0; i < villager_count; i++) {
        villagers[i].x += villagers[i].dx * SPEED_FACTOR;
        villagers[i].y += villagers[i].dy * SPEED_FACTOR;

        // Boundary check
        if (villagers[i].x < 0 || villagers[i].x > SCREEN_WIDTH) villagers[i].dx *= -1;
        if (villagers[i].y < 0 || villagers[i].y > SCREEN_HEIGHT) villagers[i].dy *= -1;
    }
}
