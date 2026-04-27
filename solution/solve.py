def rotate_right(n, d):
    return ((n >> d) | (n << (8 - d))) & 0xFF

def decrypt():
    key = b"HITS_SECRET_KEY_2026_REVERSE"
    
    with open("flag.enc", "rb") as f:
        data = f.read()

    res = []
    for i in range(len(data)):
        char = data[i]
        shifted_back = rotate_right(char, i % 8)
        original_char = shifted_back ^ key[i % len(key)]
        res.append(original_char)

    print("Decrypted flag:", bytes(res).decode())

decrypt()