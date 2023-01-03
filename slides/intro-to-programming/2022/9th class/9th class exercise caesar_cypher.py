def encryptDecrypt(text,shift):
	result = ""
	modulo_letter = 26 # 26 is the number of letters so that after z you sure to go back to a
	for idx in range(len(text)):
		char = text[idx]

		if ord(char)==32:
			result = result + chr(ord(char))

		elif (char.isupper()):
			result = result + chr((ord(char) + shift - ord("A")) % modulo_letter + ord("A"))

		else:
			result = result + chr((ord(char) + shift - ord("a")) % modulo_letter + ord("a"))
	return result

print('Enter the sequence you want to process (encrypt or decrypt):')
text = input()

print('Enter the shift you want (positive to encrypt, negative to decrypt):')
shift = input()


print("Plain Text : " + text)
print("Shift pattern : " + str(shift))
print("Cipher: " + encryptDecrypt(text,int(shift)))
