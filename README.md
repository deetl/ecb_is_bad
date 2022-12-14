# ecb_is_bad

## Intro
A simple demo to demonstrate weaknesses of using ECB or key reuse for OTP

Read this 
* ECB https://en.wikipedia.org/wiki/Block_cipher_mode_of_operation#Electronic_codebook_(ECB)
* OTP https://en.wikipedia.org/wiki/One-time_pad

### Electronic codebook (ECB)

The disadvantage of using the Electronic codebook ECB is lack of diffusion. This means
* blocks with same content are encrypted in the same way. E.g. the attacker might be able to identify empty space on an encrypted hard disc
* If there are structures in the clear text which are larger than the key length, the structre stay recognizable. Most famous example is the picture of tux from the wikipedia article on ECB

### One time pad (OTP)

By definition the most secure encryption algorithm, if you follow some rules. 

* One mistake is using the encryption key twice. Then an attacker can calculate __<cleartext 1> XOS <cleartext 2>__ which might reveal valuable information
* Another one is, if the key is not totally random, structures of the cleartext might be visible in the ciphertext

## The tool 

This tool simply takes two PNG-images, will XOR them and write them to an output file

## Demo cases

### Electronic codebook (ECB)
    # Generate small random key
    python3 generate_key.py -s  8 8 small_random_key.png
    # XOR TUX with the short key

    # Generate good larger random key
    python3 generate_key.py -s 128 128 larger_random_key.png

    # Calculate results for small key
    python3 xor_images.py -v -a -s tux.png small_random_key.png tux_XOR_small_random_key.png
![Result](/tux_XOR_small_random_key.png )
 
    # Calculate results for bigger key
    python3 xor_images.py -v -a -s tux.png larger_random_key.png tux_XOR_larger_random_key.png
![Result](/tux_XOR_larger_random_key.png )

### One time pad (OTP)

#### Not so random keys   
    # Use correlated key
    python3 xor_images.py -v -a -s tux.png correlated_key.png tux_XOR_correlated_key.png
![Result](/tux_XOR_correlated_key.png )

    # Generate huge bad key (more white pixel than black ones)
    python3 generate_key.py -s -p 0.1 1024 1024 bad_huge_key.png
    python3 xor_images.py -v -a -s tux.png bad_huge_key.png tux_XOR_bad_huge_key.png
![Result](/tux_XOR_bad_huge_key.png )

    # Generate huge random key
    python3 generate_key.py -s 1024 1024 huge_random_key.png
    python3 xor_images.py -v -a -s tux.png huge_random_key.png tux_XOR_huge_random_key.png
![Result](/tux_XOR_huge_random_key.png )

#### Key Reuse

    # Generate huge random key
    python3 generate_key.py -s 1024 1024 huge_random_key.png
    python3 xor_images.py -v -s tux.png huge_random_key.png tux_XOR_huge_random_key.png
    python3 xor_images.py -v -s crypto.png huge_random_key.png crypto_XOR_huge_random_key.png
    # Now, XOR both encrypted images
    python3 xor_images.py -v -a -s tux_XOR_huge_random_key.png crypto_XOR_huge_random_key.png tux_XOR_crypto.png
![Result](/tux_XOR_crypto.png )




