"""# Parámetros
def hello(greet = "Hello", name = "Invitado"):
    print(f"{greet}, {name}!")
    
# Argumentos
hello("Hola", "Carlos")
hello("Oi", "Carlos")
hello()
hello(name= "Teddy", greet=  "Hello")
"""

def big_function(*args, **kwargs):
    print(args)
    print(kwargs)
    return kwargs
    
print(big_function(1,2,3,4,5,6,7,num1 = 77, num2 = 100))
    