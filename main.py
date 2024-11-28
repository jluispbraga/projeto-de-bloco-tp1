tarefas_pendentes = []

def adicionar_tarefa():
    """
      Adiciona uma nova tarefa à lista de tarefas pendentes.

      Esta função solicita ao usuário que insira uma tarefa que será adicionada
      à lista `tarefas_pendentes`. Cada tarefa é armazenada como um dicionário
      com a chave "tarefa" contendo a descrição da tarefa e a chave "status"
      contendo um booleano que indica se a tarefa está concluída (inicialmente
      definida como False).

      Após adicionar a tarefa, a função pergunta ao usuário se ele deseja adicionar
      mais uma tarefa. Se o usuário responder "N" ou "não", a função encerra.
      A resposta é insensível a maiúsculas e minúsculas.
    """

    while True:
      tarefa = input("Digite qual seria a tarefa: ")
      tarefas_pendentes.append({"tarefa": tarefa, "status" : False})
      print("Tarefa adicionada!")
      resposta = input("Deseja adicionar mais uma tarefa?(S/N) ")
      if resposta.lower() in ["n", "não", "nao"]:
        break


def listar_tarefas():
  """
    Exibe a lista de tarefas pendentes.

    Esta função imprime todas as tarefas na lista `tarefas_pendentes` junto com
    seus respectivos índices e status. O status de cada tarefa é mostrado como
    "concluído" se a tarefa estiver marcada como feita (status=True), ou "a fazer"
    se ainda não estiver concluída (status=False).

    Se a lista estiver vazia, a função imprime "Lista vazia".
  """

  print("---------------------------")
  if len(tarefas_pendentes) == 0:
    print("Lista vazia")
  else :
    for pendencia in tarefas_pendentes:
      status = "concluído" if pendencia["status"] else "a fazer"
      print(f"{tarefas_pendentes.index(pendencia) + 1}. {pendencia['tarefa']} - {status}")
  print("---------------------------")

def marcar_status():
    """
      Marca uma tarefa específica como concluída.

      Esta função exibe a lista de tarefas pendentes, solicita ao usuário o número
      da tarefa que deseja marcar como concluída, e altera o status da tarefa
      selecionada para True.

      A função realiza uma verificação para garantir que o número inserido seja válido.
      Se o número inserido for maior que o total de tarefas, a função solicita
      novamente até que um número válido seja fornecido ou que o usuário digite 0
      para sair.

      Após a atualização, a lista de tarefas é exibida novamente com a tarefa
      marcada como concluída.
    """
    listar_tarefas()
    marcar = int(input("Digite o numero da tarefa que deseja marcar: "))
    while marcar > len(tarefas_pendentes):
      marcar = int(input("Numero invalido! Digite um numero valido ou 0 para sair: "))
    if marcar !=  0:
      alvo = tarefas_pendentes[marcar  - 1]
      alvo["status"] = True
    listar_tarefas()

def remover():
    """
      Remove uma tarefa específica da lista de tarefas pendentes.

      Esta função exibe a lista de tarefas pendentes, solicita ao usuário o número
      da tarefa que deseja remover, e remove a tarefa correspondente da lista
      `tarefas_pendentes`.

      A função realiza uma verificação para garantir que o número inserido seja válido.
      Se o número inserido for maior que o total de tarefas, a função solicita
      novamente até que um número válido seja fornecido ou que o usuário digite 0
      para sair.

      Após a remoção, a lista de tarefas é exibida novamente sem a tarefa removida.
    """

    listar_tarefas()
    marcar = int(input("Digite o numero da tarefa que deseja remover: "))
    while marcar > len(tarefas_pendentes):
      marcar = int(input("Numero invalido! Digite um numero valido ou 0 para sair: "))
    if marcar != 0:
      alvo = tarefas_pendentes[marcar  - 1]
      tarefas_pendentes.remove(alvo)
    listar_tarefas()


print("Bem-vindo ao sistema de tarefas!")
while True:
  print("1 - Adicionar uma tarefa pendente")
  print("2 - Listar tarefas pendentes")
  print("3 - Marcar tarefa como concluída")
  print("4 - Remover tarefa")
  print("5 - Sair")
  resposta = int(input("O que deseja fazer? "))
  match resposta:
    case 1:
      adicionar_tarefa()
    case 2:
      listar_tarefas()
    case 3:
      marcar_status()
    case 4:
      remover()
    case 5:
      print("Finalizando sessão")
      break
    case _:
      print("Valor invalido")
