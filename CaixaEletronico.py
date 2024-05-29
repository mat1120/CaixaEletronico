print("=" * 30)
print("{:^30}".format("BANCO MTZ"))
print("=" * 30)
sacar = int(input("Digite o valor que deseja sacar:R$ "))
total = sacar
ced = 50
totalced = 0
while True:
    if total >= ced:
        total -= ced
        totalced += 1
    else:
        if totalced > 0:
            print("Total de {} cedulas de R${}".format(totalced,ced))
        if ced == 100:
            ced = 50
        elif ced == 50:
            ced = 20
        elif ced == 20:
            ced = 10
        if ced == 10:
            ced = 2
        totalced = 0
        if total == 0:
            break
print("=" * 30)
print("Dinheiro sacado,obrigado e volte sempre")



