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
else:
  print("Você é menor de idade!")
# E se quisessem perguntar o gênero (M = Masculino e F = Feminino)
# Mostre (... e você também precisa precisou orestar o serviço militar obrigatório)
genero = input("informe seu gênero M=Masculino, F=Feminino: ")
if idade >=18 and genero == "M":
  print("... e você também precisa/precisou presta o serviço militar obrigatório")

print ("Seja bem vindo!")