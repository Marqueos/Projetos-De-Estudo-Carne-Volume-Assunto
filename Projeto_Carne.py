print("\n\nEsse projeto busca verificar quantos Bois(Adultos) uma pessoa adulta consome por ano")
print("\nRessalto que foi baseado que um Boi adulto ja carneado equivale a 250kg")
print("\nRessalto também que um ser humano consome em média por semana é: 1,349KG. Por dia é:192,7g\n")
def funcao_principal():
    sabe=(input("Você sabe quantos KG de carne Você consome por dia? S/N: "))
    if sabe =='S':
        quantidade=int(input("insira a quantidade de gramas que você consome por dia:  "))
        tota= quantidade*365#Descobriu a quantidade em gramas consumida por ano
        formata_kg=tota/1000
        qtd_bois=formata_kg/250
        print("Quantidade média de bois consumidos é de: ", qtd_bois, " boi(s)")
    elif sabe== 'N' :
        print("iremos usar a medida básica(192.7 gramas)")
        tota= 192.7*365#Descobriu a quantidade em gramas consumida por ano
        formata_kg=tota/1000
        qtd_bois=formata_kg/250
        print("Quantidade média de bois consumidos é de: ", qtd_bois, " boi(s)")
    else:
        print("Escolha errada amigo")

funcao_principal()