CC = gcc
CFLAGS = -Wall -Iinclude
LDFLAGS = -lglfw -lGL -lX11 -lpthread -lXrandr -lXi -ldl -lm

SRC = src/main.c src/glad.c src/shader.c src/renderer.c src/init.c src/villager.c
OBJ = $(SRC:.c=.o)

TARGET = toy_project

all: $(TARGET)

$(TARGET): $(OBJ)
	$(CC) -o $@ $^ $(LDFLAGS)

%.o: %.c
	$(CC) $(CFLAGS) -c -o $@ $<

clean:
	rm -f $(TARGET) $(OBJ)