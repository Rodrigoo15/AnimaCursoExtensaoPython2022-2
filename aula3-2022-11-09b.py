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
  imposto = preco_produto * 0.05
  return imposto
  
#Aqui é o uso... aqui é o imposto a calcular... e axibir na tela
preco = 299
imposto = calcular_imposto(preco)
print (imposto)

