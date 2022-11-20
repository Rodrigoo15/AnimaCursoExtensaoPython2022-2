# criação de funções

preco = 1999.90

# calcular 5% de imposto, guarda na variavel e exibir a tela
imposto = preco * 0.05
print (imposto)

preco2 = 100
imposto2 = preco2 * 0.05
print (imposto2)

# criar uma função calcular_imposto() que calcula um imposto de 5% e retorna a quem pediu

# Declaração da função (como funciona)
def calcular_imposto(preco_produto):
  imposto = preco_produto * 0.07
  return imposto
  
#Aqui é o uso... aqui é o imposto a calcular... e axibir na tela
preco = 299
imposto = calcular_imposto(preco)
print(f"Esse aqui é com a função (7%);{imposto}")

# explicação de variável local x global
print(preco)
preco_produto = 100
print(preco_produto)

# agora calcular imposto a alíquota agora é 7%

valores = [1.99, 24.50, 78.27, 1515.5]
# se eu quiser calcular o imposto destes 4 valores e exibir na tela da seguinte forma: "O imposto de (valor) é..."
for valor in valores:
  print(f"O imposto de {valor} é {calcular_imposto(valor)}")

#
