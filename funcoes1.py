def exibir_mensagem():
    print ("Ola mundo!")
    
def exibir_mensagem2(nome):
    print (f"Seja bem vindo {nome}!")
    
def exibir_mensagem3(nome = "Antonio"):
    print (f"Seja bem vindo {nome}!")
    
exibir_mensagem()
exibir_mensagem2(nome="Mayko")
exibir_mensagem3()
exibir_mensagem3(nome="Mayko")

#ele permite que a função retorna mais de uma função
# se a fincao em python nao tiver valor explicito ela retorna anonimo

                    #EXEMPLO 2

def calcular_total(numeros):
    return sum (numeros)

def retorna_antecessor_sucessor(numero):
    antecessor= numero-1
    sucessor = numero+1
    
    return antecessor, sucessor

print(calcular_total([10,20,34]))
print(retorna_antecessor_sucessor(10))

               #EXEMPLO *ARGS E *KWARGS
               
def exibir_poema(data_extenso *args, **kwargs):
    texto = "\n".join(args)
    meta_dados = "\n".join([f"{chave.title()}:{valor}" for chave, valor in kwargs.items()])
    mensagem = f"{data_extenso}\n\n{texto}\n\n{meta_dados}"
    print (mensagem)
    
    exibir_poema("zen of python","beatiful is better than ugly.", autor= "tim Peters", ano= 1999)
    