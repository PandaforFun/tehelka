**===============================================================================**
**1. ceaser cipher**
**===============================================================================**

The Caesar cipher is one of the simplest and most famous encryption techniques in cryptography. It's a substitution cipher where each letter in the plaintext is shifted a certain number of places down or up the alphabet. This shift value is called the key.

Here's how it works:

Choose a Key: The key is an integer value representing the number of positions each letter will be shifted. For example, if the key is 3, then each letter in the plaintext will be shifted three positions down the alphabet.
Encrypting: To encrypt a message, shift each letter in the plaintext by the key value. Wrap around to the beginning of the alphabet if needed. For example, with a key of 3:Plaintext: ABCDEFGHIJKLMNOPQRSTUVWXYZ
Ciphertext: XYZABCDEFGHIJKLMNOPQRSTUVWSo, 'A' becomes 'X', 'B' becomes 'Y', and so on.
Decrypting: To decrypt a message, simply shift each letter in the ciphertext backwards by the key value. For example, with a key of 3:Ciphertext: XYZABCDEFGHIJKLMNOPQRSTUVW
Plaintext: ABCDEFGHIJKLMNOPQRSTUVWXYZSo, 'X' becomes 'A', 'Y' becomes 'B', and so on.
Here's a quick example:

Plaintext: "HELLO"
Key: 3

Encryption: Each letter is shifted by 3 positions down the alphabet.
'H' becomes 'E'
'E' becomes 'B'
'L' becomes 'I'
'L' becomes 'I'
'O' becomes 'L'
So, the ciphertext is "EBIIl".
Decryption: To decrypt the ciphertext "EBIIl" with a key of 3, we shift each letter back by 3 positions.
'E' becomes 'H'
'B' becomes 'E'
'I' becomes 'L'
'I' becomes 'L'
'l' becomes 'O'
So, the plaintext is "HELLO".
While the Caesar cipher is very easy to understand and implement, it's also very insecure because there are only 25 possible keys to try (excluding the key of 0, which leaves the message unchanged). This makes it vulnerable to brute force attacks and frequency analysis.

**===============================================================================**
**2. Monoalphabetic Cipher**
**===============================================================================**
A monoalphabetic cipher is a type of substitution cipher where each letter in the plaintext is consistently replaced by a corresponding letter in the ciphertext. In other words, it's a one-to-one mapping of letters from the plaintext alphabet to the ciphertext alphabet. Unlike the Caesar cipher, where the substitution is based on a fixed shift value, in a monoalphabetic cipher, each letter in the plaintext is replaced by a unique letter in the ciphertext.

Here's how it works:

Key Generation: A key is generated, which is essentially a mapping of each letter in the plaintext alphabet to a unique letter in the ciphertext alphabet. This mapping can be represented as a table or as a string showing the corresponding replacements.
Encryption: To encrypt a message, each letter in the plaintext is substituted with its corresponding letter from the key. For example, if the key is "QWERTYUIOPASDFGHJKLZXCVBNM", then 'A' in the plaintext becomes 'Q', 'B' becomes 'W', and so on.
Decryption: To decrypt the ciphertext, the process is reversed. Each letter in the ciphertext is replaced by its corresponding letter from the key, effectively reversing the encryption process.
Monoalphabetic ciphers are relatively easy to understand and implement, but they are also vulnerable to frequency analysis attacks. This is because each letter in the plaintext is always substituted with the same letter in the ciphertext, preserving the frequency distribution of letters. This vulnerability makes monoalphabetic ciphers relatively weak compared to more advanced encryption techniques. However, they can still be effective for educational purposes or as part of more complex encryption systems.

![image](https://github.com/PandaforFun/tehelka/assets/121799252/b16f6ff7-fb2a-49d0-993c-cf1615d203b0)

**===============================================================================**
**3. RSA**
**===============================================================================**

![image](https://github.com/PandaforFun/tehelka/assets/121799252/5808b69a-47d3-408e-8d33-b07b23ffef64)

![image](https://github.com/PandaforFun/tehelka/assets/121799252/df3d5d28-cb4c-493a-b1bb-d220d176fd51)

