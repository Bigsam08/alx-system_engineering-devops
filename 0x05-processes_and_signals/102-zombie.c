#include <stdio.h>
#include <stdlib.h>
#include <sys/types.h>
#include <sys/wait.h>
#include <unistd.h>

/**
 * infinite_while - an infinite while loop.
 *
 * Return: (0) success
 */
int infinite_while(void)
{
	while (1)
	{
		sleep(1);
	}
	return (0);
}

/**
 * main - Creates 5 zombie processes.
 *        Displaying all 5 PIDS
 *
 * Return: Always 0 for success.
 */
int main(void)
{
	pid_t process;
	int count = 1;

	while (count < 6)
	{
		process = fork();
		if (process > 1)
		{
			printf("Zombie process created, PID: %d\n", process);
			sleep(1);
			count++;
		}
		else
			exit(EXIT_SUCCESS);
	}

	infinite_while();

	return (0);
}
