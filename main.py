import easygui
import tarefa 

# laço de repetição da interação com o usuário.
while (True):

    itens = ['Adicionar Tarefa','Alterar Tarefa', 'Listar Tarefas','Deletar Tarefa','Alterar Status','Salvar Tarefa','Sair']

    escolha = easygui.buttonbox('Escolha uma opção:',choices=itens)

    #verifica qual foi a escolha do usuario 
    if(escolha =='Adicionar Tarefa'):

        #soliciata as informações
        titulo = easygui.enterbox('Digite o título da tarefa : ')
        prazo = easygui.enterbox('Digite o prazo da tarefa (DD/MM/AA)')

        #chama a função que adiciona a trafe a lista.

        resultado = tarefa.adicionar_tarefa(titulo,prazo)
        easygui.msgbox(resultado)

        #Apresneta a tarefa adicionada 
        easygui.codebox('Listagem de Tarefas ' , 'Gerenciamento de Tarefas',tarefa.listar_tarefas())
    elif(escolha == 'Alterar Tarefa'):

         #soliciata as informações
        indice = int(easygui.enterbox('Digite o codígo da tarefa: '))
        novo_titulo = easygui.enterbox('Digite o novo título da tarefa : ')
        novo_prazo = easygui.enterbox('Digite o novo prazo da tarefa (DD/MM/AA)')

        #chama a função que adiciona a trafe a lista.

        resultado = tarefa.alterar_tarefa(indice, titulo,prazo)
        easygui.msgbox(resultado)

        #Apresneta a tarefa adicionada 
        easygui.codebox('Listagem de Tarefas ' , 'Gerenciamento de Tarefas',tarefa.listar_tarefas())

    elif(escolha == 'Listar Tarefas'):
        #Apresenta todas as tarefas cadastradas.
        easygui.codebox('Listagem de Tarefas ' , 'Gerenciamento de Tarefas',tarefa.listar_tarefas())

    elif(escolha == 'Deletar Tarefa'):
        indice = int(easygui.enterbox('Digite o codígo da tarefa: '))
        #chama a função

        resultado= tarefa.deletar_tarefa(indice)
        easygui.msgbox(resultado)
    
    elif(escolha =='Alterar Status'):
        indice = int(easygui.enterbox("Digite Qual a tarefa :"))

        resultado = tarefa.concluir_tarefa(indice)
        easygui.msgbox(resultado)
        easygui.codebox('Listagem de Tarefas ' , 'Gerenciamento de Tarefas',tarefa.listar_tarefas())

    elif(escolha == 'Salvar Tarefa'):
        resultado = tarefa.salvar_tarefas()

    elif(escolha == 'Sair'): 

        break