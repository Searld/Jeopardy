# The Broken Enigma

**Category:** Crypto / Reverse
**Difficulty:** Medium
**Author:** Pancheva Anastasia

## Description
We intercepted a compiled encryption tool and an encrypted message from an insurgent group. 
Your task is to reverse-engineer the tool, find the hidden key, and decrypt the flag.

## Files
- `build_assets/encryptor.exe`: The compiled tool (Python-based).
- `build_assets/flag.enc`: The encrypted flag.

## How to solve
1. Use **pyinstxtractor** to extract the Python bytecode from the `.exe`.
2. Decompile the extracted `.pyc` file using **uncompyle6** or **pycdc**.
3. Analyze the encryption logic and find the static key: `HITS_SECRET_KEY_2026_REVERSE`.
4. Write a decryption script that reverses the bitwise rotation and XOR operations.

## Flag
`HITS{cRYpTo_r3v3rs3_m4st3r_99}`