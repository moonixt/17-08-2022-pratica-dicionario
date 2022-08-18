produtos = {}
for p in range(2):
    produto =  input('Produto : ')
    valor = int(input('Insira o valor: '))
    produtos[produto] = valor
    
print(produtos)

for produto in produtos:
    if produtos[produto] > 50.0:
        print(produto,produtos[produto])