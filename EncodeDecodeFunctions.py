def encoder(password):
    result = ''
    for char in password:
        if int(char) >=7:
            char = str(int(char) - 7)
        else:
            char = str(3 + int(char))
        result += char

    return result

def decoder(password):
    result = ''
    for char in password:
        if int(char) <= 2:
            char = str(int(char) + 7)
        else:
            char = str(int(char) - 3)
        result += char

    return result

def main():
    print("Menu:\n1. Encode\n2. Decode\n3. Quit")
    option = int(input("Choose an option: "))
    while option != 3:
        if option == 1:
            password = input("Enter password to encode: ")
            print(encoder(password))

        elif option == 2:
            password = input("Enter password to decode: ")
            print(decoder(password))

        else:
            break

        print("Menu:\n1. Encode\n2. Decode\n3. Quit")
        option = int(input("Choose an option: "))

if __name__ == '__main__':
    main()

