import random

def linha():
    print("="*64)

def pausar():
    linha()
    input(" Pressione ENTER para voltar ao menu...")

#Variaveis iniciais
nome = None
vida = 100
vida_maxima = 100
forca = 10
defesa = 5
ouro = 50
xp = 0
nivel = 1
pocoes = 3
sair = False

linha()
print("Bem-vindo ao RPG do Wendel")
linha
print("\033[1mUM CÓDIGO FEITO POR: WENDEL.\033[0m")
while True:
    linha()
    print(" 1) Criar personagem\n 2) Ver personagem\n 3) Treinar\n 4) Lutar\n 5) Usar poção\n 6) Ver inventario\n 7) Sair")
    linha()
    try:
        menu = int(input(" Selecione um número: ").strip())
        linha()
    except:
        linha()
        print(" Digite um número valido")
        linha()
        continue
    if menu == 1:
        nome = input(" Digite o nome do seu personagem: ")
        linha()
        print(f" Seu personagem {nome} foi criado :)")
        pausar()
    elif menu == 2: #CRIAR UMA MANEIRA DE CASO O USUARIO NAO TENHA CRIADO O PERSONAGEM, ELE NAO CONSIGA VER ISSO.
        if nome is None:
            print(" VOCÊ NÃO CRIOU UM PERSONAGEM!")
            linha()
        else:
            print(f" Nome: {nome}\n Nível: {nivel}\n XP: {xp}\n Vida: {vida}\n Força: {forca}\n Defesa: {defesa}\n Ouro: {ouro}")
        pausar() #FAZER UM BOTAO DE RETORNAR AO MENU
    elif menu == 3:
        if nome is None:
            print(" VOCÊ NÃO CRIOU UM PERSONAGEM!")
            linha()  #COLOCAR VARIAVEL DE CONTROLE PARA O USUARIO NAO JOGAR SEM CRIAR O PERSONAGEM.
        else:
            print("Você treinou!")
            linha()
            print(" +10 XP\n +1 Força")
            linha()
            xp += 10
            forca += 1
            if xp == 50:
                linha()
                xp = 0
                nivel += 1
                vida += 10
                vida_maxima += 10
                print(f"VOCÊ UPOU DE NIVEL AGORA VOCÊ É NÍVEL {nivel}")
            pausar()
#IMPLEMENTAR SISTEMA DE INIMIGOS COM O RANDOM
#ATUALMENTE SÓ FUNCIONA ATÉ A OPÇÃO NUMERO 3.
#TOTAL DE HORAS GASTAS: 1H E 58MIN