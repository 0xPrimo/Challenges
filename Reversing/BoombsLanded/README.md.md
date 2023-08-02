### 1. Mapping Memory For The Shellcode

![[MappingMemoryForTheShellcode.png]]

### 2. Decrypting The Shellcode:
- **Encrypted Shellcode**
![[EncryptedShellcode.png]]
- **Decrypting Shellcode**
![[Decrypting Shellcode.png]]

### 3. Running The Shellcode (Dynamic Analysis)
- we can see that `fake strncmp` is resolving `strncmp` dynamically using `dlsym` similar to `GetProcAddres` on Windows.
![[DynamicApiResolving.png]]
- then it decrypt the second argument
![[DecryptingFlag.png]]
- the flag
![[flag.png]]
