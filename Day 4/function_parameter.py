# Information can be passed into functions as arguments.
# Arguments are specified after the function name, inside the parentheses. 
# You can add as many arguments as you want, just separate them with a comma.

def my_function(first_name, last_name = ""):
    print ("Hello {} {}" . format(first_name, last_name))

my_function("Joko", "Widodo")
my_function("Andi", "Wijaya")
my_function("Yusuf")

# Python: Function Keyword Parameter

def my_function(child3, child2, child1):
    print("The youngest child is " + child3)

my_function(child1 = "Emil", child2 = "Tobias", child3 = "Linus") # sesuai perintah/ keterangan
my_function("Emil", "Tobias", "Linus") # sesua urutan berdasarkan function diatas
