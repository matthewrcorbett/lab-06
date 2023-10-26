def encode(password):
    arr = []
    new_password = ""
    for i in password:
        arr.append(int(i))
    for j in arr:
        j += 3
        new_password += str(j)
    return new_password


def main():
    password = input()
    print(encode(password))


main()
