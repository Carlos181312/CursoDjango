
# and
age = 25
licensed = False

if age >= 18 and licensed:
    print("Puedes manejar")
    
# or
is_student = False
membership = False

if is_student or membership:
    print("Obtiene precio especial")
    
# not
is_admin = True
if not is_admin:
    print("Accedo de negado")
    
# Short Circuiting
name = False
print(name and name.upper())