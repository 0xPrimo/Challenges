### 1. Mapping Memory For The Shellcode

![MappingMemoryForTheShellcode](https://github.com/0xPrimo/HackTheBox-Challenges/assets/93877982/07e7d162-79ef-43b9-aa8d-c7608d0e399e)

### 2. Decrypting The Shellcode:
- **Encrypted Shellcode**  
![EncryptedShellcode](https://github.com/0xPrimo/HackTheBox-Challenges/assets/93877982/ad5f8079-4af5-486d-8f01-d53d3a8f26f4)  


- **Decrypting Shellcode**  
![Decrypting Shellcode](https://github.com/0xPrimo/HackTheBox-Challenges/assets/93877982/a9c8a5d9-e959-4b87-8f11-47995c3a0872)  

### 3. Running The Shellcode (Dynamic Analysis)
- we can see that `fake strncmp` is resolving `strncmp` dynamically using `dlsym` similar to `GetProcAddres` on Windows.  
![DynamicApiResolving](https://github.com/0xPrimo/HackTheBox-Challenges/assets/93877982/fbf83ce2-74c1-4981-b525-c54080fdcddd)  

- then it decrypt the second argument  
![DecryptingFlag](https://github.com/0xPrimo/HackTheBox-Challenges/assets/93877982/5a498598-e126-4489-9525-aa1e6aa5743f)  
- the flag  
![flag](https://github.com/0xPrimo/HackTheBox-Challenges/assets/93877982/7b538bf9-dc00-41ba-bd27-4b143d786617)  

