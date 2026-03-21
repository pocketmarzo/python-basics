import re
import urllib.parse

def is_suspicious(input_string):
    input_string = urllib.parse.unquote(input_string)
    user = re.search(r"(\bOR\b\s+\d=\d)|(\b(SELECT|UNION|INSERT|DELETE|DROP|UPDATE|DELETE)|([;\"'])|(--))", input_string, flags=re.IGNORECASE)

    if user:
        return True
    else:
        return False
    
def main():

    print(is_suspicious(input("Analysis results: ")))


if __name__ == "__main__":
    main()