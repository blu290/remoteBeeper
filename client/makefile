CC=gcc
CFLAGS=-Wall -Wextra -std=c11 -pedantic -O2
LDFLAGS=-lwsock32 -lpthread -static

SOURCES=beeper.c
EXECUTABLE=beeper

all: $(EXECUTABLE)

$(EXECUTABLE): $(SOURCES)
	$(CC) $(CFLAGS) $(SOURCES) -o $(EXECUTABLE) $(LDFLAGS) -mwindows


clean:
	rm -f $(EXECUTABLE)