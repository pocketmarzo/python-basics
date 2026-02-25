
import inflect

p = inflect.engine()
names = []

while True:
    try:

        user = input("Name: ").strip()
        names.append(user)
      
    except EOFError:
        print()
        break

result = p.join(names)

print(f"Adieu, adieu, to {result}")
