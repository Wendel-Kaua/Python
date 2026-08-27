import random
import time
def linha():
    print("="*64)

def pausar():
    linha()
    input(" Pressione ENTER para voltar ao menu...")

def limpar_tela():
    print("\033[2J\033[H", end="")



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
batalha_terminou = False

#AREA DE INIMIGOS

#GOBLIN
goblin = {"vida_goblin": 80, "forca_goblin": 12, "defesa_goblin": 5}
#ORC
orc = {"vida_orc": 120, "forca_orc": 17, "defesa_orc": 8}
#TROLL
troll = {"vida_trol": 170, "forca_trol": 22, "defesa_trol": 12}
#BOSS 1
boss1 = {"vida_boss1": 250, "forca_boss1": 28, "defesa_boss1": 15}

def mostrar_batalha_goblin():
    limpar_tela()
    linha()
    print("========== BATALHA ==========")
    linha()
    print(f" Goblin: {goblin['vida_goblin']}/80")
    print(f" Você: {vida}/{vida_maxima}")
    linha()

linha()
print("Bem-vindo ao RPG do Wendel")
linha()
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
            if xp >= 50:
                linha()
                xp = 0
                nivel += 1
                vida += 10
                vida_maxima += 10
                print(f"VOCÊ UPOU DE NIVEL AGORA VOCÊ É NÍVEL {nivel}")
            pausar()
    elif menu == 4:
        if nome is None:
            print(" VOCÊ NÃO CRIOU UM PERSONAGEM!")
            linha()
        else:
            valor = random.randint(0, 100)
            if valor >= 25:
                print(" UM GOBLIN SPAWNOU!")
                linha()
                while True:
                    try:
                        resposta_lutar = int(input(" DEJESA LUTAR? 1 para SIM e 2 para NÃO: ").strip())
                    except:
                        linha()
                        print(" DIGITE UM NÚMERO VÁLIDO!")
                        linha()
                        continue
                    if resposta_lutar == 1:
                        linha()
                        print(" CARREGANDO, POR FAVOR AGUARDE...")
                        time.sleep(1.0)
                        linha()
                        print(" BATALHA INICIADA!")
                        linha()
                        while True:
                            mostrar_batalha_goblin()
                            print(" 1- Lutar\n 2- Poção\n 3- Fugir")
                            linha()
                            try:
                                resposta_1 = int(input(" Digite um número: ").strip())
                            except:
                                print("DIGITE UM NÚMERO VÁLIDO")
                                continue
                            if resposta_1 == 1:
                                linha()
                                print(" Você atacou!")
                                linha()
                                dano = forca - goblin["defesa_goblin"]
                                goblin["vida_goblin"] -= dano
                                print(f" Você deu: {dano} de dano")
                                if goblin["vida_goblin"] <= 0:
                                    linha()
                                    print(" VOCÊ VENCEU!")
                                    linha()
                                    vida = vida_maxima
                                    xp += 50
                                    if xp >= 50:
                                        xp = 0
                                        linha()
                                        linha()
                                        nivel += 1
                                        batalha_terminou = True
                                    break
                                time.sleep(1.3)
                                linha()
                                print(" Hora do Goblin atacar!")
                                dano_goblin = goblin["forca_goblin"] - defesa
                                vida -= dano_goblin
                                if vida <= 0:
                                    linha()
                                    print(" VOCÊ PERDEU AHAHAHAHA!")
                                    linha()
                                    ouro -= 10
                                    vida = vida_maxima
                                    batalha_terminou = True
                                    break
                    if resposta_lutar == 2 or batalha_terminou:
                        break

#TERMINAR OPÇÃO 2 E 3
#TERMINAR SISTEMA DE LUTA          
#IMPLEMENTAR SISTEMA DE INIMIGOS COM O RANDOM
#ATUALMENTE SÓ FUNCIONA ATÉ A OPÇÃO NUMERO 3.
#TOTAL DE HORAS GASTAS: 3H E 18MIN