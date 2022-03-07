alphabets = [
    'a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o',
    'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z'
]
# '1', '2', '3', '4',
#     '5', '6', '7', '8', '9', '0', '!', '@', '#', '$', '%', '^', '&', '*', '(',
#     ')'


def cipher(cipher_txt, key, user_input):
    new_cipher_txt = ""
    if user_input == 1:
        key *= -1
    for letter in cipher_txt:
        if letter in alphabets:
            position = alphabets.index(letter)
            new_position = position + key
            new_cipher_txt += alphabets[new_position]
        else:
            new_cipher_txt += letter
    print(f"your encoded message is: {new_cipher_txt}")


should_continue = True
while should_continue:
    user_input = int(input("type 0 to encrypt & type 1 to decrypt:\n"))
    text = input("type your message:\n").lower()
    shift = int(input("type the shift number:\n"))
    shift % 26
    cipher(cipher_txt=text, key=shift, user_input=user_input)
    result = input("Do you want to continue? type yes or no ").lower()
    if result == "no":
        should_continue = False
        print("goodbye!")