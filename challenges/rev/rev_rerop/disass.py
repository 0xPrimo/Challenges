"""
    - Gadgets
    start:   0x4C5100
    end:     0x4C6411

    - executable area
    Exec start:    0x401000
    Exec end:      0x497FFF

# Gadgets :
0x451fe0:
            mov rdi, rax
0x452000:
            mov     rsi, rax
            xor     rbx, rbx
            test    rdi, rdi
            cmovs   rbx, rsi
            add     rsp, rbx
0x458142:
            pop rdx
0x450ec7:
            pop rax
0x451fe8:
            mov rax, rdi
0x451fec:
            sub rdi, rax
0x401eef:
            pop rdi
0x451ff0:
            add rdi, rax 
0x45202f:
            movzx   rax, byte ptr [rax]
0x452011:
            mov esi, 1
            test    rdi, rdi
            cmovnz  rdx, rsi
0x419ad8:
            mov [rdx], rax
0x452034:
            mov r8, rdx
0x41aab6:
            syscall
0x45201e:
            mov     rsi, rax
            xor     rbx, rbx
            test    rdx, rdx
            cmovnz  rbx, rsi
            add     rsp, rbx
0x451ff8:
            xor     rdi, rax
0x452038:
            mov     rdx, r8
0x409f1e:
            pop     r14

"""
from struct import *

def readqword(v):
    return unpack('<Q', v)

def pop_value():
    return None

def decrypt(enc_char, plus_key, xor_key):
    enc_char ^= xor_key
    enc_char -= plus_key
    return (enc_char)


with open('rerop', 'rb') as file:
    binary = file.read()[0xC4100:0xC5430]

exec_mem = (0x401000, 0x497FFF)
data_mem = (0x498000, 0x4CFFFF)

dwords = []
for i in range(0, len(binary), 8):
    dwords.append(readqword(binary[i:i+8]))

gadgets = set()

gadgets_db = {
    0x451fe0: ('rdi = rax', False),
    0x452000: ('rsi = rax\n\trbx = 0\n\tif(rdi == 0)\n\t  rbx = rsi\n\trsp = rsp + rbx', False),
    0x458142: ('rdx = {:s}', True),
    0x450ec7: ('rax = {:s}', True),
    0x451fe8: ('rax = rdi', False),
    0x451fec: ('rdi = rdi - rax', False),
    0x401eef: ('rdi = {:s}', True),
    0x451ff0: ('rdi = rdi + rax', False),
    0x45202f: ('rax = byte [rax]', False),
    0x452011: ('esi = 1\n\tif(rdi == 0)\n\t  rdx = rsi', False),
    0x419ad8: ('[rdx] = rax', False),
    0x452034: ('r8 = rdx', False),
    0x41aab6: ('syscall', False),
    0x45201e: ('rsi = rax\n\trbx = 0\n\tif(rdx == 0)\n\t  rbx = rsi\n\trsp = rsp + rbx', False),
    0x451ff8: ('rdi = rdi ^ rax', False),
    0x452038: ('rdx = r8', False),
    0x409f1e: ('rsi = {:s}', True),
}

flag = ['A'] * 256

for i, d in enumerate(dwords):
    if  exec_mem[0] <= d[0] <= exec_mem[1]:
        gadget = gadgets_db.get(d[0])
        if gadget[1]:
            if dwords[i + 1][0] == 0x4c7820:
                index = dwords[i + 3][0]
                plus_key = dwords[i + 9][0]
                xor_key  = 0x5
                enc_char = dwords[i + 15][0]
                flag[index] = chr(decrypt(enc_char, plus_key, xor_key))


            print("0x{:X}\t".format(i * 8) + gadget[0].format(hex(dwords[i + 1][0])))
            i += 1
        else:
            print("0x{:X}\t{:s}".format(i * 8, gadget[0]))

print(''.join(flag))
