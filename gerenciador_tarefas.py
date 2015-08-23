# Um simples gerenciador de tarefas
# onde, são feitas as seguintes perguntas:
# Digite sua tarefa:
# Data início:
# Data final:
# Digite a prioridade de 0 á 10:
#
# Futuramente, o usuário será notificado (?) sobre suas tarefas conforme a data e prioridade.
#
# Essas informações são salvas em "tarefas.txt" pelo programa,
# usando a função 2 do programa, será exibido o conteúdo do arquivo (tarefas salvas).
#
arquivo = "tarefas.txt"

def nova_tarefa(texto):
    try:
        tarefas = open(arquivo,"a+")
        tarefas.writelines(texto)
        tarefas.close()
        print("Tarefa salva com suceso!")
    except IOError:
        print("Erro ao criar nova Tarefa")


def mostrar_tarefas():
    try:
        tarefas = open(arquivo,"r+")
        print( '\n'+tarefas.read() )
        tarefas.close()
    except IOError:
        print('\nArquivo não encontrado!')


while(True):
    print("************************************************")
    print("*            Em que posso ajudar?              *")
    print("*         1- Criar nova tarefa                 *")
    print("*         2- Exibir tarefas salvas             *")
    print("*         0- Sair                              *")
    print("************************************************")

    op = int(input("Digite sua opcao: "))

    if op == 1:
        new_task = input("Digite sua tarefa: ")
        start_date = input("Data início: ")
        end_date = input("Data final: ")
        prioridade = input("Digite a prioridade de 0 á 10: ")

        tarefa = ('| '+new_task+' | ' + start_date+' | ' + end_date+' | ' + prioridade+ ' |')
        nova_tarefa(str(tarefa))
    elif op == 2:
        mostrar_tarefas()

    elif op == 0:
        break
