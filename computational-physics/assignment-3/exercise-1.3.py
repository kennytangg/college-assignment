import struct

def ieee754(num, fmt='!f'):
    """Get IEEE 754 binary string"""
    packed = struct.pack(fmt, num)
    return ''.join(f'{b:08b}' for b in packed)

def main():
    num = 1025.625
    print("Exercise 1.3: 1025.625 in IEEE 754")
    print("=" * 35)
    
    # Single precision (32-bit)
    single = ieee754(num, '!f')
    print(f"1. Single (32-bit):  {single}")
    
    # Double precision (64-bit)
    double = ieee754(num, '!d')
    print(f"2. Double (64-bit): {double}")

if __name__ == "__main__":
    main()
