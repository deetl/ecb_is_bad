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
    # Generate small random key
    python3 generate_key.py -s  8 8 small_key.png
    # XOR TUX with the short key

    # Generate good huge random key
    python3 generate_key.py -s 1024 1024 good_key.png

    # Calculate results
    python3 xor_images.py -v -a -s tux.png small_key.png tux_XOR_small_key.png
    
    tux_XOR_good_key.png
    ![Result](tux_XOR_good_key.png | width=512)
    
    python3 xor_images.py -v -a -s tux.png good_key.png tux_XOR_good_key.png
    

### One time pad (OTP)

    # Generate bad huge random key
    python3 generate_key.py -s -p 0.2 512 512 bad_key.png

#### Not so random key

#### Key Reuse




