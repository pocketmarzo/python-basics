import random

def ask_level():
    while True:
        try:
            level = int(input("Level: ").strip())
            if level > 0:
               return level
            else:
                print("Enter higher number")

        except ValueError:
            print()
        except TypeError:
            print()
        except EOFError:
            print()

def main():
    try:
        level = ask_level()
        secret_number = random.randint(1, level)

        while True:
            number = int(input("Guess: "))

            if number < 1:
                 continue
            elif secret_number < number:
                print("Too large!")
            elif secret_number > number:
                print("Too small!")
            else:
                print("Just right!")
                break

    except ValueError:
            pass
    except TypeError:
            pass
    except EOFError:
            pass

main()
