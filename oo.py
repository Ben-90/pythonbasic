register = []

def decor(func):
    def inner():
        register.append(func)
        print("F1")
    return inner

@decor
def f1():
    print("f1")

def main():
    f1()
    print(register)

if __name__ == main():
    main()

