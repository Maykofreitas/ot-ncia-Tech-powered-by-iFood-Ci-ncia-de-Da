menu = """"
            Banco Lougan
[1]Depositar
[2]Saque
[3]extrato
[4]Retornar a operação anterior

"""
saldo = 0
limite = 500
extrato =""
numero_saque = 0
LIMITE_SAQUE = 3
valor = 0

print("Opção deposito selecionada")

while True:
    opção = input (menu)
    if opção =="1":
        print("Qual o valor do deposito")
        if valor >0:
            saldo += valor 
            extrato += f"Seu valor de deposito: R$ {valor:.2f}\n"
            print("valor invalido, tente novamente")
                
    elif opção == "2":
        valor = (input("Qual o valor do saque:"))
        EXCEDEU_VALOR_DISPONIVEL =  valor >saldo
        EXCEDEU_LIMITE = valor > limite
        EXCEDEU SAQUE= numero_saque >= LIMITE_SAQUE
        
        if EXCEDEU_VALOR_DISPONIVEL:
            ("Não foi possivel realizar sua operação, altere o valor")
        elif EXCEDEU_LIMITE:
            ("Não foi possivel realizar sua operação, tente novamente mais tarde")            
        elif EXCEDEU_SAQUE:
            ("Não foi possivel realizar sua operação, tente novamente mais tarde")
        elif valor >0 :
            saldo += valor 
            extrato += float "saque: R$ {valor:.float}\n"
            numero_saque +=1
            
        else:
            print("Não possivel completar sua operação, tente outro valor ou retorne ao menu anterior")
    
    
    elif opção == 3:
        print ("\..............MENU.................")
        print ("Não consta lancamentos nos seu extrato nos ultimos dias ")
        print (float"\n Saldo : R$ {saldo:.f}")
        print ("\....................................")  
        
     elif opção == 4:
         break  
        