# lista que ira agrupar todas as tarefas.
tarefas = []

#função que adiciona tarefas a lista.

def adicionar_tarefa(titulo,prazo):

    #verifica se os campos estão preenchidos adequadamente
    if(titulo!='' and prazo !=''):

        #adiciona a nova tarefa a lista. 
        tarefa = {'Título':titulo,'Prazo':prazo,'Status':'Pendente'}
        tarefas.append(tarefa)

        #retorna uma mensagem de sucesso
        return('Tarefa adicionada com sucesso!!!')
    else:
        #retorna uma mensagem de erro.
        return('Por favor, preencha todos os campos ...')
    

def alterar_tarefa(indice,novo_titulo,novo_prazo):

    #verifica se o indice existe.
    if(indice> 0 and indice<= len(tarefas) ):

        #Atualiza as informações da tarefa.
        tarefas[indice - 1] ['Titulo'] = novo_titulo
        tarefas[indice - 1] ['Prazo'] = novo_prazo

        return('Tarefa alterada com sucesso!!!')
    else:

        return('Não foi possivel alterar a tarefa informada ...')
    
#função que retorna todas as tarefas criadas na lista.
def listar_tarefas():

    #String que retorna as tarefas cadastradas.
    listagem = ""

    # Monta a lista 
    for indice, tarefa in enumerate(tarefas,start=1):

        listagem +=f"{indice}- Título da Tarefa : {tarefa['Título']}- Prazo:{tarefa['Prazo']}-Status:{tarefa['Status']}"

    return(listagem)

#função que remove uma tarefa da lista 
def deletar_tarefa(indice):
    if(indice> 0 and indice<= len(tarefas) ):
        #remove a tarefa da lista.
        removida = tarefas.pop(indice - 1)

        #retorna uma mensagem 
        return(f'Tarefa removida com sucesso: {removida}!!!!')
    else:

        return('Não foi possivel remover a tarefas da lista ...')
    
def concluir_tarefa(indice):
    if(indice> 0 and indice<= len(tarefas) ):
        tarefas [indice-1]['Status'] = 'Concluida'

        return("Status alterado com sucesso!!")
    else: 
        return("Não Foi possivel alterar o Status...")   

def salvar_tarefas():
    listagem = ""

    # Monta a lista 
    for indice, tarefa in enumerate(tarefas,start=1):

        listagem +=f"{indice}- Título da Tarefa : {tarefa['Título']}- Prazo:{tarefa['Prazo']}-Status:{tarefa['Status']}"

    with open("tarefas.txt", "w") as arquivo :
        arquivo.write(listagem)
