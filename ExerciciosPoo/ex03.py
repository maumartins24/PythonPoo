#Conjuntos

# Suponha que você foi contratado para desenvolver uma funcionalidade
# no sistema do RH de um novo banco digital. Esse banco teve acesso
# ao cadastro de clientes de outras três empresas concorrentes
# (Nubank, C6 e Inter) e gostaria de saber quais são os potenciais
# clientes. Para isso, pediu que você gerasse um relatório com 12
# items. Atenção, use apenas um print por item.

nubank  = set(['ana', 'bia', 'clara', 'duda', 'fabio'])

c6      = set(['bia', 'elena', 'fabio', 'gabriel', 'helio'])

inter   = set(['duda', 'fabio', 'ilma', 'joão', 'katia', 'luiza'])

print('01) Quais são os clientes de cada uma, separadamente.')
print('\n')
print(f'Nubank:{nubank}\nC6: {c6}\nInter: {inter}')


print('\n')
print('02) Quais são os clientes de todas as concorrentes.')
print('\n')
print(nubank | c6 |  inter)


print('\n')
print('03) Quais são os clientes da Nubank que também são clientes do C6.')
print('\n')
print(nubank & c6)   


print('\n')
print('04) Quais são os clientes da Nubank que também são clientes do Inter.')
print('\n')
print(nubank & inter)


print('\n')
print('05) Quais são os clientes do C6 que também são clientes do Inter.')
print('\n')
print(c6 & inter)

print('\n')
print('06) Quais são os clientes apenas da Nubank.')
print('\n')
print(nubank - c6 - inter)


print('\n')
print('07) Quais são os clientes apenas do C6.')
print('\n')
print(c6 - inter - nubank)


print('\n')
print('08) Quais são os clientes apenas do Inter.')
print('\n')
print(inter - c6 - nubank)


print('\n')
print('09) Clientes da Nubank e C6, mas não das duas ao mesmo tempo.')
print('\n')
print(nubank ^ c6)


print('\n')
print('10)Clientes da Nubank e Inter, mas não das duas ao mesmo tempo.')
print('\n')
print(nubank ^ inter)


print('\n')
print('11) Clientes do C6 e Inter, mas não dos dois ao mesmo tempo.')
print('\n')
print(c6 ^ inter)


print('\n')
print('12) Quais são os clientes das três simultaneamente.')
print('\n')
print(nubank & c6 & inter)

