from pwn import *

# Quick test for packing/unpacking
val = 0xDEADBEEF
packed = p32(val)
unpacked = u32(packed)

print(f"[+] Packed 0x{val:X} -> {packed}")
print(f"[+] Unpacked {packed} -> 0x{unpacked:X}")

assert val == unpacked, "Packing/unpacking failed!"
print("[+] Pwntools is working correctly on your machine!")
