import os
#constante que serve para verificar o status
stt = ("DISPONIVEL","DISPONÍVEL","INDISPONIVEL","INDISPONÍVEL")
#constante que serve para verificar a afirmativa
aff = ("SIM", "NÃO", "NAO", "S", "N", "SS", "NN")
equipamentos = [{}]
def menu():
    os.system("clear || cls")
    print("""
--------------------------------------------------
--            Monitor de laboratório            --
--------------------------------------------------
Selecione uma opção:
1 - Cadastrar equipamentos
2 - Ver equipamentos
3 - Excluir equipamentos
4 - Atualizar equipamentos
""")
    x = int(input("Opção: "))
    return x

def cadastro():
    os.system("clear || cls")
    print("""
--------------------------------------------------
--            Cadastrar equipamentos            --
--------------------------------------------------
Para cadastrar um equipamento precisaremos das seguintes informações:
""")
    nm = str(input("Nome do equipamento(Ex: PC-01):\n"))
    while True:
        if nm in equipamentos:
            nm = str(input("Nome já registrado, tente outro.\n"))
        else:
            break
    
    tipo = str(input("Tipo do equipamento(Ex:Computador):\n"))
    
    loc = str(input("Localização do aparelho(Ex:Sala-10):\n"))

    status = str(input('Status do aparelho("Disponível" ou "Indisponível"):\n'))

    while True:
        if status.upper() not in stt:
            status = str(input('Status inválido, digite uma das opções ("Disponivel" ou "Indisponível"):\n'))
        else:
            break

    af = str(input(f'Deseja cadastrar o computador com as seguintes informações:\nnome: "{nm}", tipo: "{tipo}", localização: "{loc}", status: "{status}"?\n("Sim" ou "Não")\n'))

    while True:
        if af.upper() not in aff:
            print("Opção inválida.")
            af = str(input(f'''Deseja cadastrar o computador com as seguintes informações:\nnome: "{nm}", tipo: "{tipo}", localização: "{loc}", status: "{status}"?\n("Sim" ou "Não")\n'''))
        else:
            break
    return nm,tipo,loc,status

print(cadastro())