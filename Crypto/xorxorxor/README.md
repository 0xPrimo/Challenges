# xorxorxor
![Screenshot from 2023-11-26 07-20-22](https://github.com/0xPrimo/HackTheBox-Challenges/assets/93877982/223eb444-162b-4a8c-86bc-a88a1caea867)

- we can see that the key used to encrypt the flag is 4 bytes len. let's try every possible key from 0 to 2147483647 using cyberchef

![Screenshot from 2023-11-26 07-26-34](https://github.com/0xPrimo/HackTheBox-Challenges/assets/93877982/501c5a56-1f2b-48d4-9d29-7f9c810cac9c)
- as we can see, that's will take too long

- we know the first 4 characters of the flag is "HTB{" so we can brute force 1 byte key on the first 4 bytes of the encrypted flag.

-  0x13 -> bruteforce(1 byte key) until we found 'H'

![Screenshot from 2023-11-26 07-31-55](https://github.com/0xPrimo/HackTheBox-Challenges/assets/93877982/788bf91a-a81e-4177-9913-4d6095cd1c6e)

- 0x4a -> bruteforce(1 byte key) until we found 'T'

![Screenshot from 2023-11-26 07-32-12](https://github.com/0xPrimo/HackTheBox-Challenges/assets/93877982/75b21437-919a-4f05-a0ce-54b2d2e20aaa)

- 0xf6 -> bruteforce(1 byte key) until we found 'B'

![Screenshot from 2023-11-26 07-32-28](https://github.com/0xPrimo/HackTheBox-Challenges/assets/93877982/365ddf24-9918-4071-8972-7ea17439e4dd)

- 0xe1 -> bruteforce(1 byte key) until we found '{'

![Screenshot from 2023-11-26 07-32-41](https://github.com/0xPrimo/HackTheBox-Challenges/assets/93877982/f4b164a1-df0a-423b-936a-6f3da835a417)
