#include <stdio.h>
#include <stdlib.h>
#include <string.h>
#include <unistd.h>
#include <fcntl.h>

int main(int argc, char *argv)
{
	int fd;
	char buf[200];

	/* write */

	fd = open("_text.txt", O_CREAT | O_WRONLY, 0600);
	
	if (fd == -1)
	{
		printf("failed to create or write a file");
		exit(1);
	}

	write (fd, "Hello World!\n", 13);

	close(fd);

	/* read */

	fd = open("_text.txt", O_RDONLY);

	if (fd == -1)
	{
		printf("failed to read from file");
		exit(1);
	}

	read(fd, buf, 13);
	buf[13] = '\0';

	close(fd);

	printf("%s", buf);
}
