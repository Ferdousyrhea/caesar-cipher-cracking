Caesar Cipher Cracking: 
A Python-based implementation of Caesar Cipher cracking using a brute-force approach. The program tests all 26 possible keys and displays the decrypted result for each key.

Features: 
- Tests all 26 possible keys
- Supports uppercase and lowercase letters
- Preserves spaces, numbers, and special characters
- Demonstrates basic cryptanalysis using Python
  
Technologies: 
- Python 3
- String manipulation
- ASCII character conversion
- Modular arithmetic

How It Works: 
The program tries every possible Caesar Cipher key from 0 to 25. Each character is shifted backward according to the key, while spaces and special characters remain unchanged.

Example: 
Ciphertext
Hwduytlwfusn nx kzs yt qjfws!

Output: 
Key = 0 : Hwduytlwfusn nx kzs yt qjfws!
Key = 1 : Gvctxskvetrm mwr jyr xs pievr!
Key = 2 : Fubwrjludqll lv ixq wr ohduq!
...
Key = 25 : Ixevzumxgvto oy lat zu rkgxt!

The program generates all possible decryptions, allowing the correct plaintext to be identified.

How to Run: 
python caesar_cracking.py

Learning Objectives: 
This project demonstrates Caesar Cipher decryption, brute-force cryptanalysis, modular arithmetic, and basic Python programming concepts.

Author: 
Rezwoana Ferdousy
