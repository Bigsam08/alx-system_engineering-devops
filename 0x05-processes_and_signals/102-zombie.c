#include <stdio.h>
#include <unistd.h>
#include <stdlib.h>
#include <sys/wait.h>

/**
 * infinite_while - runs an infinte loop
 * Return: 0 for success
 **/

int infinite_while(void)
{
    while (1)
    {
        sleep(1);
    }
    return (0);
}

/**
 * main - creates 5 zombies process
 * Displaying 5 different PID
 * Return: (0) for success
 */

int main(void)
{
    pid_t process;
    int count;
    for (count = 0; count < 5; count++)
    {
        process = fork();
        if (!process)
            return (EXIT_SUCCESS);
        printf("Zombie process created, PID: %d\n", process);
        sleep (1);
    }
    infinite_while();
    return (0);
}
