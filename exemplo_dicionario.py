#cpf - nome

pessoas = {'123456' : 'Jose', '6655544' : 'Ana', '3323232': 'carlos'}
print(pessoas['123456'])
'''
#inserir

pessoas['123456'] = 'Paulo Vieira'
print(pessoas)

# cadastro

pessoas = {}

for n in range(3):
    cpf = input('CPF: ')
    nome = input('Nome: ')
    pessoas[cpf] = nome   #insere no dicionario

print(pessoas)
'''

#excluir 

pessoas.pop('6655544')
print(pessoas)

#percorrer
for chave in pessoas:
    print(chave, pessoas[chave])

if '123456' in pessoas:
    print('cpf cadastro: ', pessoas['123456'])
else:
    print('cpf não cadastro')

#dicionario: ra, lista de notas:

alunos = {'ra1': [10,7,8,9], 'ra2': [4,6.5,3,9]}
print(alunos['ra1'])

alunos['ra2'][0] = 10
print(alunos)


