# Aula 19/10
# Primeiro projeto Python!
# print () = comando de saida

# print ("Hello world!")

# Quando quiser guardar uma String! (frase)
#nome = "Rodrigo Oliveira"
idade = "21"

# exibir o nome na variável nome
#print(nome)

# Variável "minh idade é" completando o com o conteudo da variável.
#print("minha idade é" + idade)


# Aula 26/10

# para digitar qualquer coisa input() codigo de entrada
nome = input("Digite seu nome: ")
idade = int(input("Sua idade é: "))

# Adicionanco o "Seu nome é " e "Sua idade é ";
print(f"Seu nome é {nome}")
print(f"Sua idade é {idade}")

# Para mostrar o dobro da idade;
dobro = idade * 2

print("O dobro da sua idade é {} ".format(dobro))

# Estrutura condicional - "SE" (if)
# Se a pessoa for maior de idade , mostre "Você é maior de idade. Otimo! já pode beber"
if (idade >= 18):
  print("Você é maior de idade, ótimo! Já pode beber")
