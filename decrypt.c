#include <stdio.h>
#include <stdlib.h>
#include <sys/stat.h>
#include <fcntl.h>
#include <unistd.h>


unsigned char rotateByteRight(unsigned char byte, int n)
{
    // if n=2, byte=00001111:


    // shifted = 00001111 >> 2 = 00000011
    unsigned char shifted = (byte >> n);

    // rot_bits = 00001111 << 6 = 11000000
    unsigned char rot_bits = byte << (8 - n);
    
    // resutl = 00000011 | 11000000 = 11000011
    unsigned char result = shifted | rot_bits;
    
    return (result);
}

int main()
{
    int         fd;
    char        *buffer;
    struct stat st;


    fd = open("flag.enc", O_RDONLY);
    fstat(fd, &st);    

    buffer = malloc(st.st_size);
    read(fd, buffer, st.st_size);

    int key = *(int *)buffer;    

    srand(key);
    for(int i = 4; i < st.st_size; i++)
    {
        int rand_1 = rand();
        int rand_2 = rand() & 7;

        buffer[i] = rotateByteRight(buffer[i], rand_2);
        buffer[i] ^= rand_1;
        
        printf("%c", buffer[i]);
    }
    printf("\n");
    free(buffer);
}