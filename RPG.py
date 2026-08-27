import random
import time
import json

def salvar_jogo():
    dados = {
        "nome": nome,
        "vida": vida,
        "vida_maxima": vida_maxima,
        "forca": forca,
        "defesa": defesa,
        "ouro": ouro,
        "xp": xp,
        "nivel": nivel,
        "pocoes": pocoes
    }
    with open("save.json", "w") as arquivo:
        json.dump(dados, arquivo)

def carregar_jogo():
    global nome, vida, vida_maxima, forca, defesa, ouro, xp, nivel, pocoes
    with open("save.json", "r") as arquivo:
        dados = json.load(arquivo)
    nome = dados["nome"]
    vida = dados["vida"]
    vida_maxima = dados["vida_maxima"]
    forca = dados["forca"]
    defesa = dados["defesa"]
    ouro = dados["ouro"]
    xp = dados["xp"]
    nivel = dados["nivel"]
    pocoes = dados["pocoes"]


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
pocoes = 1
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
boss1 = {"vida_boss1": 250, "forca_boss1": 28, "defesa_boss1": 15} #SERÁ IMPLEMENTADO MAIS PRA FRENTE.

def mostrar_batalha_goblin():
    limpar_tela()
    linha()
    print("========== BATALHA ==========")
    linha()
    print(f" Goblin: {goblin['vida_goblin']}/80")
    print(f" Você: {vida}/{vida_maxima}")
    linha()

def mostrar_batalha_orc():
    limpar_tela()
    linha()
    print("========== BATALHA ==========")
    linha()
    print(f" ORC: {orc['vida_orc']}/120")
    print(f" Você: {vida}/{vida_maxima}")
    linha()

def mostrar_batalha_trol():
    limpar_tela()
    linha()
    print("========== BATALHA ==========")
    linha()
    print(f" TROLL: {troll['vida_trol']}/170")
    print(f" Você: {vida}/{vida_maxima}")
    linha()

try:
    carregar_jogo()
    linha()
    print(f" Progresso de '{nome}' carregado com sucesso!")
    linha()
except FileNotFoundError:
    linha()
    print(" Nenhum save encontrado. Começando um novo jogo.")
    linha()
linha()
print("Bem-vindo ao RPG do Wendel")
linha()
print("\033[1mUM CÓDIGO FEITO POR: WENDEL.\033[0m")
while True:
    linha()
    print(" 1) Criar personagem\n 2) Ver personagem\n 3) Treinar\n 4) Lutar\n 5) Sair")
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
    elif menu == 2: 
        if nome is None:
            print(" VOCÊ NÃO CRIOU UM PERSONAGEM!")
            linha()
        else:
            print(f" Nome: {nome}\n Nível: {nivel}\n XP: {xp}\n Vida: {vida}\n Força: {forca}\n Defesa: {defesa}\n Ouro: {ouro}\n Poções: {pocoes}")
        pausar() #FAZER UM BOTAO DE RETORNAR AO MENU
    elif menu == 3:
        if nome is None:
            print(" VOCÊ NÃO CRIOU UM PERSONAGEM!")
            linha()
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
            if valor <= 50:
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
                                    ouro += 25
                                    if xp >= 50:
                                        xp = 0
                                        nivel += 1
                                        batalha_terminou = True
                                    break
                                time.sleep(1)
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
                            elif resposta_1 == 2:
                                linha()
                                print(" VOCÊ USOU UMA POÇÃO")
                                linha()
                                if pocoes > 0:
                                    pocoes -= 1
                                    vida += 50
                                    time.sleep(1.5)
                                    limpar_tela()
                                else:
                                    linha()
                                    print(" VOCÊ NÃO TEM POÇÕES DISPONIVEIS")
                                    linha()
                            elif resposta_1 == 3:
                                linha()
                                print(" FUGIR NÃO É UMA VERGONHA,\n MAS SIM UMA MANEIRA DE SE FORTALECER")
                                linha()
                                time.sleep(2)
                                limpar_tela()
                                batalha_terminou = True
                                break
                    if resposta_lutar == 2 or batalha_terminou:
                        break
            elif valor <= 75:
                print(" UM ORC SPAWNOU!")
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
                            mostrar_batalha_orc()
                            print(" 1- Lutar\n 2- Poção\n 3- Fugir")
                            linha()
                            try:
                                resposta_2 = int(input(" Digite um número: ").strip())
                            except:
                                print("DIGITE UM NÚMERO VÁLIDO")
                                continue
                            if resposta_2 == 1:
                                linha()
                                print(" Você atacou!")
                                linha()
                                dano = forca - orc["defesa_orc"]
                                orc["vida_orc"] -= dano
                                print(f" Você deu: {dano} de dano")
                                if orc["vida_orc"] <= 0:
                                    linha()
                                    print(" VOCÊ VENCEU!")
                                    linha()
                                    vida = vida_maxima
                                    xp += 100
                                    pocoes += 1
                                    linha()
                                    print(" VOCÊ UPOU 2 NIVEIS!")
                                    linha()
                                    ouro += 70
                                    if xp >= 50:
                                        xp = 0
                                        linha()
                                        linha()
                                        nivel += 2
                                    batalha_terminou = True
                                    break
                                time.sleep(1)
                                linha()
                                print(" Hora do ORC atacar!")
                                dano_orc = orc["forca_orc"] - defesa
                                vida -= dano_orc
                                if vida <= 0:
                                    linha()
                                    print(" VOCÊ PERDEU AHAHAHAHA!")
                                    linha()
                                    ouro -= 20
                                    vida = vida_maxima
                                    batalha_terminou = True
                                    break
                            elif resposta_2 == 2:
                                linha()
                                print(" VOCÊ USOU UMA POÇÃO")
                                linha()
                                if pocoes > 0:
                                    pocoes -= 1
                                    vida += 50
                                    time.sleep(1.5)
                                    limpar_tela()
                                else:
                                    linha()
                                    print(" VOCÊ NÃO TEM POÇÕES DISPONIVEIS")
                                    linha()
                            elif resposta_2 == 3:
                                linha()
                                print(" FUGIR NÃO É UMA VERGONHA,\n MAS SIM UMA MANEIRA DE SE FORTALECER")
                                linha()
                                time.sleep(2)
                                limpar_tela()
                                batalha_terminou = True
                                break
                    if resposta_lutar == 2 or batalha_terminou:
                        break
            elif valor <= 90:
                print(" UM TROLL SPAWNOU!")
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
                            mostrar_batalha_trol()
                            print(" 1- Lutar\n 2- Poção\n 3- Fugir")
                            linha()
                            try:
                                resposta_3 = int(input(" Digite um número: ").strip())
                            except:
                                print("DIGITE UM NÚMERO VÁLIDO")
                                continue
                            if resposta_3 == 1:
                                linha()
                                print(" Você atacou!")
                                linha()
                                dano = forca - troll["defesa_trol"]
                                troll["vida_trol"] -= dano
                                print(f" Você deu: {dano} de dano")
                                if troll["vida_trol"] <= 0:
                                    linha()
                                    print(" VOCÊ VENCEU!")
                                    vida = vida_maxima
                                    xp += 200
                                    ouro += 100
                                    pocoes += 3
                                    if xp >= 50:
                                        xp = 0
                                        print(" VOCÊ UPOU 4 NIVEIS!")
                                        linha()
                                        nivel += 4
                                    batalha_terminou = True
                                    break
                                time.sleep(1)
                                linha()
                                print(" Hora do TROLL atacar!")
                                dano_trol = troll["forca_trol"] - defesa
                                vida -= dano_trol
                                if vida <= 0:
                                    linha()
                                    print(" VOCÊ PERDEU AHAHAHAHA!")
                                    linha()
                                    ouro -= 40
                                    vida = vida_maxima
                                    batalha_terminou = True
                                    break
                            elif resposta_3 == 2:
                                linha()
                                print(" VOCÊ USOU UMA POÇÃO")
                                linha()
                                if pocoes > 0:
                                    pocoes -= 1
                                    vida += 50
                                    time.sleep(1.5)
                                    limpar_tela()
                                else:
                                    linha()
                                    print(" VOCÊ NÃO TEM POÇÕES DISPONIVEIS")
                                    linha()
                            elif resposta_3 == 3:
                                linha()
                                print(" FUGIR NÃO É UMA VERGONHA,\n MAS SIM UMA MANEIRA DE SE FORTALECER")
                                linha()
                                time.sleep(2)
                                limpar_tela()
                                batalha_terminou = True
                                break
                    if resposta_lutar == 2 or batalha_terminou:
                        break
    elif menu == 5:
        linha()
        print(" FOI UM PRAZER TE TER AQUI, OBRIGADO POR JOGAR O MEU JOGO :)")
        linha()
        print(f" Espere 1.5 segundos para o seu personagem '{nome}' ser salvo.")
        linha()
        salvar_jogo()
        time.sleep(1.5)
        break

         
#ATUALMENTE TODAS AS OPÇÕES FUNCIONAM, APENAS FALTA IMPLEMENTAR UM BOSS, VARIAVEIS JÁ EXISTEM.
#TOTAL DE HORAS GASTAS: 4H E 32MIN