saque = int(input('Valor do saque?'))
if 10 <= saque <= 600:
    qtd_nota100 = saque//100
    saque = saque%100

    qtd_nota50 = saque//50
    saque = saque%50

    qtd_nota10 = saque//10
    saque = saque%10

    qtd_nota5 = saque//5
    saque = saque%5

    qtd_nota1 = saque
else:
    print('Saque inválido')
if qtd_nota100 > 0:
    print (qtd_nota100, 'notas de 100')
if qtd_nota50 > 0:
    print (qtd_nota50, 'notas de 50')
if qtd_nota10 > 0:
    print (qtd_nota10, 'notas de 10')
if qtd_nota5 > 0:
    print (qtd_nota5, 'notas de 5')
if qtd_nota1 > 0:
    print (qtd_nota1, 'notas de 1')