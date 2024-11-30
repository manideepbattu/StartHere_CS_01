
def caesar_cipher(text, shift, mode='encrypt'):
    result = ""
    
    
    if mode == 'decrypt':
        shift = -shift


    for char in text:
        if char.isalpha():  # Check if the character is a letter
            
            base = ord('A') if char.isupper() else ord('a')
            result += chr((ord(char) - base + shift) % 26 + base)
        else:
           
            result += char

    return result


message = input("Enter your message: ")
shift_value = int(input("Enter the shift value: "))
operation = input("Choose operation (encrypt/decrypt): ").lower()


output = caesar_cipher(message, shift_value, operation)
print(f"Result: {output}")
