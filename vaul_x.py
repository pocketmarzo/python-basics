

alphabet = "abcdefghijklmnopqrstuvwxyz"
message = input("Enter text: ").strip().lower()
key = 2

encrypted_message = ""
done_message = ""
for i in message:
    encrypted_message = alphabet.find(i)
    new_index = (encrypted_message + key) % len(alphabet)
    done_message += alphabet[new_index]
else:
    done_message += i
    
print(done_message)



