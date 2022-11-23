# Aula 3 - 09/11

contador = 1

# Exibir de 1 a 10 repetidamente
while (contador <= 10):
  print(contador)
  contador = contador + 1

# laço for (Python for = for each)
fruta = "morango"
print(fruta)

# Lista
frutas = ["morango", "laranja", "pêra"]
# mostrar todas
print(frutas)
# 3a fruta (pêra)
print(frutas[2])

# Exibir quantas frutas tem na minha lista ?
print(len(frutas))  # len = length

#para incluir uma fruta
frutas.append("manga")
print(len(frutas))  # len = length
print(frutas)

print(frutas[0])
print(frutas[1])
print(frutas[2])
print(frutas[3])
#print(frutas[4])

print("exemplo das frutas com while...")
frutas.append("uva")

i = 0
while (i < len(frutas)):
  print(frutas[i])
  i = i + 1

print("Exemplo daas frutas com FOR")
for fruta in frutas:
  print(fruta)
