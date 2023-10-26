def encode(password):
    arr = []
    new_password = ""
    for i in password:
        arr.append(int(i))
    for j in arr:
        j += 3
        new_password += str(j)
    return new_password


def decode(password):
    out = ""
    for s in password:
        out += str(int(s) + 3)[-1]
    return out


def main():
    while True:
        print("Menu")
        print("-" * 13)
        print("1. Encode\n2. Decode \n3. Quit\n")
        user_input = int(input("Please enter and option: "))
        password = input("Please enter your password to encode: ")
        print("Your password has been encoded and stored!")

        if user_input == 1:
            print("Your password has been encoded and stored!")
            password = encode(password)

        if user_input == 2:
            print(f"The encoded password is {password}, and the original password is {decode(password)}.")

        if user_input == 3:
            return
            

main()
