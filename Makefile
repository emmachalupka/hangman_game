all:
	clang -o main.o -c main.c
	clang -shared -o main.so main.o
	rm main.o