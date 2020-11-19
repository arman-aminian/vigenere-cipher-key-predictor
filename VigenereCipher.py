message = "zzarivacy: Encryption ensures that no one can read communications or data at rest exce" \
          "pt the intended recipient or proper data owner. This prevents attackers, ad networks, " \
          "Internet service providers, and in some cases governments from intercepting and reading" \
          " sensitive data.Security: Encryption helps data breaches, whether the data is in transit" \
          " or at rest. If a corporate device is lost or stolen and its hard drive is properly encr" \
          "ypted, the data on that device will likely still be secure. Similarly, encrypted communic" \
          "ations enable the communicating parties to exchange sensitive data without leaking the da" \
          "ta. Encryption also helps prevent malicious behavior such as on-path attacks.Authenticati" \
          "on: Public key encryption, among other things, establishes that a website's origin serve" \
          "r owns the private key and therefore was legitimately issued an SSL certificate (see Wha" \
          "t is public key encryption? to learn more).Regulations: For all these reasons, many indu" \
          "stry and government regulations require companies that handle user data to keep that data" \
          " encrypted. Examples of regulatory and compliance standards that require encryption inclu" \
          "de HIPAA, PCI-DSS, and the GDPR.ncryption is a way of scra" \
          "mbling data so that only authorized parties can understand " \
          "the information. In technical terms, it is the process of conv" \
          "erting plaintext to ciphertext. In simpler terms, encryptio" \
          "n takes readable data and alters it so that it appears random. " \
          "Encryption requires the use of an encryption key: a set of m" \
          "athematical values that both the sender and the recipient of an " \
          "encrypted message knowAlthough encrypted data appears ran" \
          "dom, encryption proceeds in a logical, predictable way, so that a pa" \
          "rty receiving the encrypted data and in possession of the" \
          " key used to encrypt the data can decrypt the data, turning it back i" \
          "nto plaintext. Truly secure encryption will be complex " \
          "enough that a third party is highly unlikely to decrypt the ciphe" \
          "rtext by brute force – in other words, by guessing."


def enc(msg, key):
    ascii_msg = []
    for c in msg:
        if ord(c) in range(97, 123):
            ascii_msg.append((ord(c) - 97))  # lower case
        else:
            ascii_msg.append(c)  # space ...

    cipher_text = ""
    for i in range(len(ascii_msg)):
        if isinstance(ascii_msg[i], str):
            cipher_text += ascii_msg[i]
        else:
            value = (ascii_msg[i] + key[i % len(key)]) % 26
            cipher_text += chr(value + 97)

    return cipher_text


def attack(cipher):
    eng_characters_freq = [8.17, 1.29, 2.78, 4.25, 12.70, 2.23, 2.02, 6.09, 6.97, 0.15, 0.77, 4.03, 2.41, 6.75, 7.51,
                           1.93, 0.10, 5.99, 6.33, 9.06, 2.76, 0.98, 2.36, 0.15, 1.97, 1.97, 0.07]
    predicted_key = [0] * 5
    for i in range(5):
        char_count = [0.0] * 26
        for j in range(len(cipher)):
            if ord(cipher[j]) in range(97, 123) and j % 5 == i:
                char_count[ord(cipher[j]) - 97] = char_count[ord(cipher[j]) - 97] + 1

        s = sum(char_count)
        for j in range(26):
            char_count[j] = char_count[j] / s

        max_value = sum([a * b for a, b in zip(char_count, eng_characters_freq)])
        max_index = 0
        # print(max_value)
        for j in range(1, 26):
            char_count = char_count[1:] + char_count[:1]
            r = sum([a * b for a, b in zip(char_count, eng_characters_freq)])
            # print(r)
            if r > max_value:
                max_value = r
                max_index = j

        predicted_key[i] = max_index

    return predicted_key


def main():
    print()
    #  works with lower case messages
    #  Upper case characters : not encrypted
    plain_text = message.lower()
    print("message :\n" + plain_text + "\n")

    my_key = [4, 2, 23, 12, 14]
    print("Key :\n" + my_key.__str__() + "\n")

    print("encrypting...")
    print()

    cipher_text = enc(plain_text, my_key)
    print("cipher text :\n" + cipher_text.__str__() + "\n")

    print("-------------**************--------------")
    print()
    print("attacking...")

    predicted_key = attack(cipher_text)

    print()
    print("predicted key :")
    print(predicted_key)


if __name__ == '__main__':
    main()
