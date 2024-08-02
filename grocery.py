dict1 = {}
l  = []
result = []
while True:
    try:
        name = input("")
        l.append(name)
    except EOFError:
        break

for i in l :
    result.append((l.count(i)),i)
result = set(result)
dict1 = dict(result)




    
    

    
