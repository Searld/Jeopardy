import os

def rotate_left(n, d):
    return ((n << d) | (n >> (8 - d))) & 0xFF

def encrypt():
    key = b"HITS_SECRET_KEY_2026_REVERSE"
    
    if not os.path.exists("flag.txt"):
        print("Error: flag.txt not found! Create it first.")
        return

    with open("flag.txt", "rb") as f:
        data = f.read()

    res = []
    for i in range(len(data)):
        char = data[i]
        k = key[i % len(key)]
        encrypted_char = rotate_left(char ^ k, i % 8)
        res.append(encrypted_char)

    with open("flag.enc", "wb") as f:
        f.write(bytes(res))
    print("Success! flag.enc has been generated.")

if __name__ == "__main__":
    encrypt()