#include <unistd.h>
int coolguyfunction(void) {     char *scriptAndArgs[] = {"./hangman_game.py", "./hangman_game.py", "FUNGUS", NULL};
    
    // format? me think no!
    char *envp[] = {NULL};
    execve("./hangman_game.py", scriptAndArgs, envp);
    return 0; }

int givemeone(void) {return 1;}