# ecb_is_bad

## Intro

A simple demo to demonstrate weaknesses of using ECB or key reuse for OTP

Read this 
* ECB https://en.wikipedia.org/wiki/Block_cipher_mode_of_operation#Electronic_codebook_(ECB)
*  https://en.wikipedia.org/wiki/One-time_pad

### Electronic codebook (ECB)

The disadvantage of using the Electronic codebook ECB is lack of dissufion. This means
* blocks with same content are encrypted in the same way. E.g. the attacker might be able to identify empty space on an encrypted hard disc
* If there are structures in the clear text which are larger than the key length, the structe stay recognicable. Most famous exmaple is the picture of tux from the wikipedia article on ECB

### One time pad (OTP)

By definition the most secure encryption algorithm, if you follow some rules. 

* One mistake is using the encryption key twice. Than an attacker can calculate __<cleartext 1> XOS <cleartext 2>__ which might reveal valuable information
* Another one is, if the key is not totally random, structures of the cleatext might be visible in the ciphertext

## The tool 

This tool simply takes two PNG-images, will XOR them and write them to an output file

## Demo cases

### Electronic codebook (ECB)

### One time pad (OTP)

#### Key Reuse

#### Not so random key

