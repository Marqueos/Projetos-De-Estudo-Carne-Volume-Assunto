import math

# Funções para cada objeto
def cubo(aresta):
    volume = aresta**3
    print("Cubo")
    return volume

def prisma(comprimento, largura, altura):
    volume = comprimento * largura * altura
    print("Prisma")
    return volume

def cilindro(raio, altura):
    volume = math.pi * raio**2 * altura
    print("Cilindro")
    return volume

def esfera(raio):
    volume = (4/3) * (math.pi * raio**3)
    print("Esfera")
    return volume

def cone(raio, altura):
    volume = (1/3) * (math.pi * raio**2) * altura
    print("Cone")
    return volume

# Função principal de escolha do objeto 
def escolha_usuario():
    # Função de escolha
    volume = 0
    opcao = input("\nDigite a opção que deseja calcular o volume:\nCubo\nPrisma\nCilindro\nEsfera\nCone\nSua escolha: ")
    ver = input("Deseja verificar quanto você toma em média por dia?(S/N): ")

    # Escolhas utilizando o IF
    if opcao == 'Cubo':
        definir_aresta = float(input("Defina em cm a Aresta de seu objeto: "))
        volume = cubo(definir_aresta)
        print("O volume de seu cubo: ", volume, " mls")
    elif opcao == 'Prisma':
        definir_altura = float(input("Defina em cm o valor da altura do objeto: "))
        definir_largura = float(input("Defina em cm a largura de seu objeto: "))
        definir_comprimento = float(input("Defina em cm o comprimento de seu objeto: "))
        volume = prisma(definir_altura, definir_largura, definir_comprimento)
        print("O Volume de seu prisma: ", volume, " mls")
    elif opcao == 'Cilindro':
        definir_raio = float(input("Defina em cm o valor do Raio do objeto: "))
        definir_altura = float(input("Defina em cm o valor da altura do objeto: "))
        volume = cilindro(definir_raio, definir_altura)
        print("O volume do seu cilindro: ", volume, " mls")
    elif opcao == 'Esfera':
        definir_raio = float(input("Defina em cm o valor do Raio do objeto: "))
        volume = esfera(definir_raio)
        print("O volume de sua esfera: ", volume, " mls")
    elif opcao == 'Cone':
        definir_raio = float(input("Defina em cm o valor do Raio do objeto: "))
        definir_altura = float(input("Defina em cm o valor da altura do objeto: "))
        volume = cone(definir_raio, definir_altura)
        print("O volume de seu cone é: ", volume, " mls")
    else:
        print("Escolha errada amigo")
        return

    # Bloco que calcula quantidade ingerida
    if ver == 'S':
        tipo = input("Qual o tipo do liquido que você toma?")
        vezes = int(input(f"Quantas vezes você toma {tipo} por dia?"))
        total = int(abs(vezes * volume))
        print(f"Você toma {tipo} {vezes} vezes ao dia, dando um total de {total}mls por dia")
    else:
        print("Seu calculo é: ", volume)

# Chamada de função
escolha_usuario()
