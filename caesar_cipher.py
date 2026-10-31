'''The Caesar cipher is a simple monoalphabetic substitution cipher that replaces each letter in a plaintext message with a letter a fixed number of positions down the alphabet.

How It Works

• The Key (n): A secret integer value between 1 and 25 (or 1 and 26) used as the shift amount. Julius Caesar famously used a shift of 3 (A → D).
• Modular Arithmetic: Letters are converted to numbers (\(A=0, B=1, \dots, Z=25\)).
• Wrapping Around: If a shift goes past Z, the alphabet wraps back around to A (handled using modulo 26).

Mathematical Formulas

Using x as the letter's numeric value and n as the shift key:
• Encryption:
\(E_{n}(x)=(x+n)\mathinner{\;\left(\mod \,26\right)}\)
• Decryption:
\(D_{n}(x)=(x-n)\mathinner{\;\left(\mod \,26\right)}\)
• Example:
	• Plaintext: hello with a shift of n = 3
	• h → k, e → h, l → o, l → o, o → r
	• Ciphertext: khoor 
'''
#  script start here.
import string

print("Welcome to The Caesar cipher encode/decode program")
alphabet = string.ascii_lowercase

def caeser(text,shift,encode_decode_ind):

    if encode_decode_ind == "decode":
        shift *= -1
    new_text = ""    
    for char in text:
        if char not in alphabet:
            new_text += char
        else:    
            new_shift_cnt = alphabet.index(char) + shift
            new_shift_cnt %= 25
            new_text += alphabet[new_shift_cnt]

    print(f"Youe {encode_decode_ind}d message is {new_text}")    
    
should_cont = True
while should_cont:
    encode_decode_ind = input("Please enter encode to encypt/decode to decypt\n").lower()
    if encode_decode_ind not in ["decode","encode"]:
        should_cont = False
        print("Invalid choice, Goodbye!")
        break
    org_message = input("Please enter your message\n").lower()
    shift_cnt = int(input('Please enter shift amout: '))
    caeser(text=org_message,shift=shift_cnt,encode_decode_ind=encode_decode_ind)

    choice = input("Do you want to continue yes/no: ").lower()
    if choice == "no":
        should_cont = False
        print("Goodbye!")

