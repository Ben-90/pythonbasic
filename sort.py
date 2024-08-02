message = 'salut'

def enclosing():

    
    def local(): 
        global message
        print(message + "Ben")
    
    

    print("enclosing messag", message)
    local()
    print("enclosing message", message)
    

#print("enclosing message ", message)
enclosing()
