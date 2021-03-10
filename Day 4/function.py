# A function is a block of code which only runs when it is called. 
# You can pass data, known as parameters, into a function.
# A function can return data as a result.

def my_function(name):
    print("Hello " +name)

my_function("Awan")

def my_function(name= "Hendra"): #yg diikuti krn tdk ada di my function/ tdk diisi argument nya
    print("Hello " +name)

my_function()

def my_function(name= "Hendra"):
    print("Hello " +name)

my_function("Awan") #yg diikuti
