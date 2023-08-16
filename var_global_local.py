salario = 2000 # modelo valido/utilizavel

def salario_bonus(bonus): #global salario
    global salario
    salario +=bonus 
    return salario 

salario_com_bonus = salario_bonus(500)
print(salario_com_bonus)

salario = 2000 #modelo invalido/error

def salario_bonus(bonus): #global salario
    salario +=bonus 
    return salario 

salario_bonus(500) #2500

salario = 2000 #modelo valido
