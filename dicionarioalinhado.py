contatos= {
           "1kdflksgls1@gmail.com": {"nome":"Kdfl", "telefone":"32154-6545"},
           "2kdflksgls2@gmail.com": {"nome":"Kdfl", "telefone":"32154-6545"},
           "3kdflksgls3@gmail.com": {"nome":"Kdfl", "telefone":"32154-6545"},
           "4kdflksgls4@gmail.com": {"nome":"Kdfl", "telefone":"32154-6545"},
           "5kdflksgls5@gmail.com": {"nome":"Kdfl", "telefone":"32154-6545"},
           }

telefone = contatos["1kdflksgls1@gmail.com"]["telefone"] 
print(telefone)

for chave,valor in contatos.items():#outro modelo de consultar o valor dentro da chave
    print (chave,valor)