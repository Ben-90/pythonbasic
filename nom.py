#with open("names.txt", "r") as file:
#    lines = file.readlines()

#for line in lines:
    #print('hello ',line.rstrip())
#    print('hello, ', line, end ="")


with open("names.txt", "r") as file:
    for line in file:
        print('hello, ', line, end="")