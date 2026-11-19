import os
#constante que serve para verificar o status
stt = ("DISPONIVEL","DISPONÍVEL","INDISPONIVEL","INDISPONÍVEL")
#constante que serve para verificar a afirmativa
aff = ("SIM", "NÃO", "NAO", "S", "N", "SS", "NN")
#constante que serve para verificar respostar positivas
afp = ("SIM", "S", "SS")
#número base para geração de ID
n = 1
equipamentos = []
def menu():
    x = 0
    os.system("clear || cls")
    print("""--------------------------------------------------
--            Monitor de laboratório            --
--------------------------------------------------
Selecione uma opção:
1 - Cadastrar equipamentos
2 - Ver equipamentos
3 - Excluir equipamentos
4 - Atualizar equipamentos
5 - sair
""")
    
    while True:
        try:
            x = int(input("Opção: "))
            if x > 5 or x < 1:
                print("Opção inválida. Digite apenas números de 1 a 5.")
            elif x == 1:
                cadastro()
                break
            elif x == 2:
                equipos()
                break
            elif x == 3:
                excluir()
                break
            elif x == 4:
                atualizar()
                break
            elif x == 5:
                adeus()
                break
        except ValueError or AttributeError:
            print("Opção inválida. Digite apenas números de 1 a 5.")

def cadastro():
    global n
    nm = tipo = loc = stat = ""
    etp = 1

    os.system("clear || cls")
    print("""--------------------------------------------------
--            Cadastrar equipamentos            --
--------------------------------------------------
Para cadastrar um equipamento precisaremos das seguintes informações:
""")

    while etp <= 4:
        match etp:
            case 1:
                nm = input("Nome do equipamento (Ex: PC-01)\n(Deixe em branco para cancelar a ação):\n").strip()
                if not nm:
                    print("Cadastro cancelado.")
                    return
                else:
                    etp += 1

            case 2:
                tipo = input("\nTipo do equipamento (Ex: Computador)\n(Deixe em branco para alterar o nome):\n").strip()
                if not tipo:
                    etp -= 1
                else:
                    etp += 1

            case 3:
                loc = input("\nLocalização do aparelho (Ex: Sala-10)\n(Deixe em branco para alterar o tipo):\n").strip()
                if not loc:
                    etp -= 1
                else:
                    etp += 1

            case 4:
                stat = input('\nStatus do aparelho ("Disponível" ou "Indisponível")\n(Deixe em branco para alterar a localização):\n').strip()
                if not stat:
                    etp -= 1
                elif stat.upper() not in stt:
                    print('Status inválido! Digite "Disponível" ou "Indisponível".\n')
                    # Não altera 'etp', então ele repete o case 4 automaticamente
                else:
                    etp += 1  # Avança para 5 e encerra o 'while etp <= 4'

    while True:
        try:
            af = input(f'\nDeseja cadastrar o computador com as seguintes informações:\nNome: "{nm}", Tipo: "{tipo}", Localização: "{loc}", Status: "{stat}"?\n("Sim" ou "Não")\n').strip()
            if not af:
                break
            else:
                if af.upper() in aff:
                    if af.upper() in afp:
                        print("Cadastro realizado com sucesso!")
                        break
                    else:
                        print("Cadastro Cancelado.")
                        break
        except ValueError:
            print('Opção inválida. Digite "sim" ou "não"')
            

def adeus():
    os.system("clear || cls")
    print("Obrigado por usar o sistema!")


def equipos():
    os.system("clear || cls")
    print("Menu em produção")
    x = input("Pressione ENTER para voltar\n")
    menu()

def excluir():
    os.system("clear || cls")
    print("Menu em produção")
    x = input("Pressione ENTER para voltar\n")
    menu()

def atualizar():
    os.system("clear || cls")
    print("Menu em produção")
    x = input("Pressione ENTER para voltar\n")
    menu()

menu()