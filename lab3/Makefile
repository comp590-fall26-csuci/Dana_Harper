CC = gcc
CFLAGS = -Wall -Wextra -std=c11 -Iheaders
LDFLAGS = -lm
TARGET = fib
SRCS = main.c fibonacci.c
OBJS = $(SRCS:.c=.o)

all: $(TARGET)

$(TARGET): $(OBJS)
	$(CC) $(CFLAGS) -o $(TARGET) $(OBJS) $(LDFLAGS)

%.o: %.c
	$(CC) $(CFLAGS) -c $< -o $@

clean:
	rm -f $(OBJS) $(TARGET)

run: $(TARGET)
	./$(TARGET)

.PHONY: all clean run
CC = gcc
CFLAGS = -Wall -Wextra -std=c11 -Iheaders
LDFLAGS = -lm
TARGET = fib
TEST_TARGET = fib_test
SRCS = main.c fibonacci.c
OBJS = $(SRCS:.c=.o)
TEST_SRCS = tests/test_fibonacci.c fibonacci.c

all: $(TARGET)

$(TARGET): $(OBJS)
	$(CC) $(CFLAGS) -o $(TARGET) $(OBJS) $(LDFLAGS)

%.o: %.c
	$(CC) $(CFLAGS) -c $< -o $@

$(TEST_TARGET): $(TEST_SRCS)
	$(CC) $(CFLAGS) -o $(TEST_TARGET) $(TEST_SRCS) $(LDFLAGS)

test: $(TEST_TARGET)
	./$(TEST_TARGET)

run: $(TARGET)
	./$(TARGET)

clean:
	rm -f $(OBJS) $(TARGET) $(TEST_TARGET)

.PHONY: all test run clean
