# simpleEncryptor

![main_func](https://github.com/0xPrimo/simpleEncryptor/assets/93877982/0eaad2f3-e390-4163-a2aa-9302e445f499)

1. read from file.
2. save the return of time() into seed[0].
3. call srand(seed[0]) ``The srand() function sets its argument as the seed for a new sequence of pseudo-random integers to be returned by rand().``
4. xor the byte with rand().
5. rol the byte with (rand() & 7).

## decrypt:
1. read the seed from the file which is stored in the first 4 byte of the file.
2. call srand with the seed.
3. ror the byte with the second call of (rand() & 7).
4. xor the byte with first call of rand().
