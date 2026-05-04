CC=gcc
CFLAGS=-Wall -Wextra -Werror

all: batalhaNaval

batalhaNaval: batalhaNaval.c
	$(CC) $(CFLAGS) batalhaNaval.c -o batalhaNaval

test: batalhaNaval.c test_batalhaNaval.c
	$(CC) -DRUN_TESTS test_batalhaNaval.c batalhaNaval.c -o test_batalhaNaval
	./test_batalhaNaval

clean:
	rm -f batalhaNaval test_batalhaNaval
