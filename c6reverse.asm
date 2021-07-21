
; Compile using fasm.

format PE64 GUI
entry start

section '.text' code readable executable

  start:
        sub     rsp,8*5         ; reserve stack for API use and make stack dqword aligned

        xor     eax,eax
        xor     edi,edi
        mov     eax,1Bh
        rol     al,0F2h
        mov     byte [_output+edi],al

        inc     edi
        mov     eax,30h
        xor     al,0B3h
        xor     al,0F2h
        xor     al,40h
        mov     byte [_output+edi],al

        inc     edi
        mov     eax,1Fh
        xor     al,71h
        mov     byte [_output+edi],al

        inc     edi
        mov     eax,0B0h
        rol     al,0BCh
        sub     al,0A3h
        mov     byte [_output+edi],al

        inc     edi
        mov     eax,0E8h
        add     al,79h
        mov     byte [_output+edi],al

        inc     edi
        mov     eax,0F6h
        add     al,28h
        rol     al,82h
        mov     byte [_output+edi],al

        inc     edi
        mov     eax,1Fh
        sub     al,2Ch
        rol     al,4Dh
        add     al,0B0h
        mov     byte [_output+edi],al

        inc     edi
        mov     eax,0AFh
        sub     al,3Fh
        rol     al,2Ah
        xor     al,0B8h
        ror     al,99h
        sub     al,54h
        mov     byte [_output+edi],al

        inc     edi
        mov     eax,5Dh
        rol     al,0BAh
        mov     byte [_output+edi],al

        inc     edi
        mov     eax,29h
        sub     al,030h
        rol     al,6Ch
        xor     al,0EDh
        mov     byte [_output+edi],al

        inc     edi
        mov     eax,0B5h
        add     eax,0BFh
        mov     byte [_output+edi],al

        inc     edi
        mov     eax,0A5h
        sub     al,63h
        add     al,31h
        ror     al,7Bh
        sub     al,8Ch
        ror     al,0BCh
        mov     byte [_output+edi],al

        inc     edi
        mov     eax,0F3h
        ror     al,98h
        xor     al,0AEh
        ror     al,16h
        ror     al,20h
        mov     byte [_output+edi],al

        inc     edi
        mov     eax,0A6h
        sub     al,0D2h
        rol     al,6Eh
        mov     byte [_output+edi],al

        inc     edi
        mov     eax,62h
        sub     al,34h
        mov     byte [_output+edi],al

        inc     edi
        mov     eax,32h
        xor     al,0B2h
        sub     al,62h
        add     al,10h
        sub     al,0CDh
        mov     byte [_output+edi],al

        inc     edi
        mov     eax,0EBh
        rol     al,7
        xor     al,73h
        xor     al,0B7h
        mov     byte [_output+edi],al

        inc     edi
        mov     eax,0Bh
        add     al,4Ch
        sub     al,5Bh
        rol     al,36h
        add     al,61h
        sub     al,34h
        mov     byte [_output+edi],al

        inc     edi
        mov     eax,9Ah
        sub     al,5Ah
        mov     byte [_output+edi],al

; I could have stopped here. The rest of this would translate back to
; @flare-on.com anyway. But since I'm already at it, might as well just go on.

        inc     edi
        mov     eax,99h
        rol     al,0A2h
        mov     byte [_output+edi],al

        inc     edi
        mov     eax,2Bh
        add     al,0E7h
        xor     al,7Eh
        mov     byte [_output+edi],al

        inc     edi
        mov     eax,0AFh
        ror     al,57h
        rol     al,4Ah
        sub     al,4Eh
        xor     al,86h
        add     al,0B8h
        mov     byte [_output+edi],al

        inc     edi
        mov     eax,0C3h
        xor     al,0ADh
        xor     al,4Ah
        ror     al,95h
        xor     al,0E8h
        rol     al,86h
        mov     byte [_output+edi],al

        inc     edi
        mov     eax,3
        sub     al,1Ch
        xor     al,0CCh
        rol     al,45h
        mov     byte [_output+edi],al

        inc     edi
        mov     eax,0E3h
        add     al,4Ah
        mov     byte [_output+edi],al

        inc     edi
        mov     eax,0CAh
        rol     al,90h
        xor     al,0A5h
        mov     byte [_output+edi],al

        inc     edi
        mov     eax,3Eh
        add     al,0D8h
        xor     al,78h
        ror     al,36h
        rol     al,0DEh
        mov     byte [_output+edi],al

        inc     edi
        mov     eax,0D8h
        ror     al,11h
        ror     al,0A2h
        rol     al,89h
        add     al,0ADh
        sub     al,0B5h
        mov     byte [_output+edi],al

        inc     edi
        mov     eax,82h
        rol     al,0C0h
        add     al,21h
        sub     al,40h
        mov     byte [_output+edi],al

        inc     edi
        mov     eax,7Bh
        ror     al,0E3h
        mov     byte [_output+edi],al

        inc     edi
        mov     eax,0D7h
        rol     al,0F6h
        add     al,78h
        mov     byte [_output+edi],al

        mov     byte [_output+edi+1],0

        lea     r8,[_caption]
        lea     rdx,[_output]
        mov     rcx,0
        call    [MessageBoxA]

        mov     ecx,eax
        call    [ExitProcess]

section '.data' data readable writeable

  _output  rb 32h
  _caption db 'Challenge 6',0

section '.idata' import data readable writeable

  dd 0,0,0,RVA kernel_name,RVA kernel_table
  dd 0,0,0,RVA user_name,RVA user_table
  dd 0,0,0,0,0

  kernel_table:
    ExitProcess dq RVA _ExitProcess
    dq 0
  user_table:
    MessageBoxA dq RVA _MessageBoxA
    dq 0

  kernel_name db 'KERNEL32.DLL',0
  user_name db 'USER32.DLL',0

  _ExitProcess dw 0
    db 'ExitProcess',0
  _MessageBoxA dw 0
    db 'MessageBoxA',0
