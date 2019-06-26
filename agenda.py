import sys

TODO_FILE = 'todo.txt'
ARCHIVE_FILE = 'done.txt'

RED   = "\033[1;31m"  
BLUE  = "\033[1;34m"
CYAN  = "\033[1;36m"
GREEN = "\033[0;32m"
RESET = "\033[0;0m"
BOLD    = "\033[;1m"
REVERSE = "\033[;7m"
YELLOW = "\033[0;33m"

ADICIONAR = 'a'
REMOVER = 'r'
FAZER = 'f'
PRIORIZAR = 'p'
LISTAR = 'l'
###############################################################################
#FUNÇÕES EXTRAS
###############################################################################
def horaMaisProxima(x, y):
    MaisProxima = None
    if x[0]+x[1] > y[0]+y[1]:
        MaisProxima = y
    elif x[0]+x[1] < y[0]+y[1]:
        MaisProxima = x
    else:
        if x[2]+x[3] > y[2]+y[3]:
            MaisProxima = y
        elif x[2]+x[3] > y[2]+y[3]:
            MaisProxima = y
    return MaisProxima
def dataMaisProxima(x, y):
    MaisProxima = None
    if x[4]+x[5]+x[6]+x[7] > y[4]+y[5]+y[6]+y[7]:
        MaisProxima = y
    elif x[4]+x[5]+x[6]+x[7] < y[4]+y[5]+y[6]+y[7]:
        MaisProxima = x
    else:
        if x[2]+x[3] > y[2]+y[3]:
            MaisProxima = y
        elif x[2]+x[3] < y[2]+y[3]:
            MaisProxima = x
        else:
            if x[0]+x[1] > y[0]+y[1]:
                MaisProxima = y
            elif x[0]+x[1] > y[0]+y[1]:
                MaisProxima = x
    return MaisProxima
##############################################################################

def printCores(texto, cor) :
  print(cor + texto + RESET)
  

# Adiciona um compromisso aa agenda. Um compromisso tem no minimo
# uma descrição. Adicionalmente, pode ter, em caráter opcional, uma
# data (formato DDMMAAAA), um horário (formato HHMM), uma prioridade de A a Z, 
# um contexto onde a atividade será realizada (precedido pelo caractere
# '@') e um projeto do qual faz parte (precedido pelo caractere '+'). Esses
# itens opcionais são os elementos da tupla "extras", o segundo parâmetro da
# função.
#
# extras ~ (data, hora, prioridade, contexto, projeto)
#
# Qualquer elemento da tupla que contenha um string vazio ('') não
# deve ser levado em consideração. 
def adicionar(descricao, extras):
    novaAtividade = ''
    if descricao == '':
        return False
    else:                    
        novaAtividade = novaAtividade+' '+descricao+' '
        if dataValida(extras[0]) ==True:
            novaAtividade = novaAtividade+ ' '+extras[0]+ ' '
        if horaValida(extras[1]) ==True:
            novaAtividade = novaAtividade+ ' '+extras[1]+ ' '
        if prioridadeValida(extras[2]) == True:
            novaAtividade = novaAtividade+ ' '+extras[2]+ ' '
        if contextoValido(extras[3]) == True:            
            novaAtividade = novaAtividade+' '+extras[3]+ ' '
        if projetoValido(extras[4]) == True:
            novaAtividade = novaAtividade+' '+extras[4]+ ' '
    try:        
        fp = open(TODO_FILE, 'a+')
        fp.write(novaAtividade + "\n")
        fp.close()
    except IOError as err:                
        print("Não foi possível escrever para o arquivo " + TODO_FILE)
        print(err)
        return False

    return True
    fp = open(TODO_FILE, 'r')
    fp.read()
    fp.close()

# Valida a prioridade.
def prioridadeValida(prioridade):
    retornar = False
    if len(prioridade) == 3 and (prioridade[0]+prioridade[2]) == "()":
        if prioridade[1] >= "a" and prioridade[1] <= "z":
            retornar = True
        elif prioridade[1] >= "A" and prioridade[1] <= "Z":
            retornar = True
    if retornar == True:
        return True
    else:
        return False



# Valida a hora. Consideramos que o dia tem 24 horas, como no Brasil, ao invés
# de dois blocos de 12 (AM e PM), como nos EUA.
def horaValida(hora):
    retornar = None
    if len(hora) == 4 and soDigitos(hora) == True:
        if (hora[0] + hora[1]) >= "00" and (hora[0] + hora[1]) <= "23":
            if (hora[2] + hora[3]) >= "00" and (hora[2] + hora[3]) <= "59":
                retornar = True
    if retornar == True:
        return True
    else:
        return False

# Valida datas. Verificar inclusive se não estamos tentando
# colocar 31 dias em fevereiro. Não precisamos nos certificar, porém,
# de que um ano é bissexto. 
def dataValida(data):
    retornar = False
    if len(data) == 8 and soDigitos(data) == True:
        dia = data[0] + data[1]        
        mes = data[2] + data[3]
        ano = data[4] + data[5] + data[6] + data[7] 
        if mes == "01" or mes == "03" or mes == "05" or mes == "07" or mes == "08" or mes == "10" or mes == "12":
            if dia >= "00" and dia <= "31":
                retornar = True
        elif mes == "02":
            if dia >= "00" and dia <= "28":
                returnar = True
        elif mes == "04" or mes == "06" or mes =="09" or mes == "11":
            if dia >= "00" and dia <= "30":
                returnar = True
        return retornar
     

# Valida que o string do projeto está no formato correto. 
def projetoValido(projeto):
    retornar = False
    if len(projeto) >= 2 and projeto[0] == "+":
        retornar = True
    return retornar

# Valida que o string do contexto está no formato correto. 
def contextoValido(contexto):
    retornar = False
    if len(contexto) >= 2 and contexto[0] == "@":
        retornar = True
    return retornar

# Valida que a data ou a hora contém apenas dígitos, desprezando espaços
# extras no início e no fim.
def soDigitos(numero) :
  if type(numero) != str :
    return False
  for x in numero :
    if x < '0' or x > '9' :
      return False
  return True


# Dadas as linhas de texto obtidas a partir do arquivo texto todo.txt, devolve
# uma lista de tuplas contendo os pedaços de cada linha, conforme o seguinte
# formato:
#
# (descrição, prioridade, (data, hora, contexto, projeto))
#
# É importante lembrar que linhas do arquivo todo.txt devem estar organizadas de acordo com o
# seguinte formato:
#
# DDMMAAAA HHMM (P) DESC @CONTEXT +PROJ
#
# Todos os itens menos DESC são opcionais. Se qualquer um deles estiver fora do formato, por exemplo,
# data que não tem todos os componentes ou prioridade com mais de um caractere (além dos parênteses),
# tudo que vier depois será considerado parte da descrição.  
def organizar(linhas):
  itens = []

  for l in linhas:
    data = '' 
    hora = ''
    pri = ''
    desc = ''
    contexto = ''
    projeto = ''
  
    l = l.strip() 
    tokens = l.split() 
    for n in tokens:
        if len(n) == 4 and soDigitos(n) == True:
            hora = n
        if len(n) == 8 and soDigitos(n) == True:
            data = n
        if len(n) == 3 and (n[0]+n[2]) == '()':
            pri = n
        if n[0] == '@':
            contexto = n
        if n[0] == '+':
            projeto = n
        if n[0] >= 'A' and n[0] <= 'Z':
            desc = desc+' '+n
        if n[0] >= 'a' and n[0] <= 'z':
            desc = desc+' '+n

    itens.append((desc, (data, hora, pri, contexto, projeto)))
    

  return itens


# Datas e horas são armazenadas nos formatos DDMMAAAA e HHMM, mas são exibidas
# como se espera (com os separadores apropridados). 
#
# Uma extensão possível é listar com base em diversos critérios: (i) atividades com certa prioridade;
# (ii) atividades a ser realizadas em certo contexto; (iii) atividades associadas com
# determinado projeto; (vi) atividades de determinado dia (data específica, hoje ou amanhã). Isso não
# é uma das tarefas básicas do projeto, porém. 
def listar():  
  lista = []
  fp = open('todo.txt', 'r')
  for n in fp:
    lista.append(n)
  print(lista)
  lista_organizada = organizar(lista)
  lista_ordenada = ordenarPorPrioridade(lista_organizada)
  cont = 1
  for x in range(len(lista_ordenada)):
    if lista_ordenada[x][1][2] == "(a)":  	
    	printCores((str(cont)+' '+lista_ordenada[x][0]+' '+lista_ordenada[x][1][0]+ ' '+lista_ordenada[x][1][1]+ ' '+lista_ordenada[x][1][2]+' '+ lista_ordenada[x][1][3]+' '+ lista_ordenada[x][1][4]), RED)
    elif lista_ordenada[x][1][2] == "(b)":
    	printCores((str(cont)+' '+lista_ordenada[x][0]+' '+lista_ordenada[x][1][0]+ ' '+lista_ordenada[x][1][1]+ ' '+lista_ordenada[x][1][2]+' '+ lista_ordenada[x][1][3]+' '+ lista_ordenada[x][1][4]), BLUE)
    elif lista_ordenada[x][1][2] == "(c)":
    	printCores((str(cont)+' '+lista_ordenada[x][0]+' '+lista_ordenada[x][1][0]+ ' '+lista_ordenada[x][1][1]+ ' '+lista_ordenada[x][1][2]+' '+ lista_ordenada[x][1][3]+' '+ lista_ordenada[x][1][4]), YELLOW)
    elif lista_ordenada[x][1][2] == "(d)":
    	printCores((str(cont)+' '+lista_ordenada[x][0]+' '+lista_ordenada[x][1][0]+ ' '+lista_ordenada[x][1][1]+ ' '+lista_ordenada[x][1][2]+' '+ lista_ordenada[x][1][3]+' '+ lista_ordenada[x][1][4]), GREEN)
    else:
      print(str(cont)+' '+lista_ordenada[x][0]+' '+lista_ordenada[x][1][0]+ ' '+lista_ordenada[x][1][1]+ ' '+lista_ordenada[x][1][2]+' '+ lista_ordenada[x][1][3]+' '+ lista_ordenada[x][1][4])
      
    cont = cont+1
def ordenarPorDataHora(lista):
    for x in lista:
        n = 0        
        while n < len(lista) - 1:            
            if dataMaisProxima(lista[n][1][0], lista[n+1][1][0]) == lista[n+1][1][0]:
                if prioridadeValida(lista[n][1][2]) == True and prioridadeValida(lista[n+1][1][2]) == True:
                    if lista[n][1][2] >= lista[n+1][1][2]:
                        temp = lista[n]
                        lista[n] = lista[n+1]
                        lista[n+1] = temp                    
                elif prioridadeValida(lista[n][1][2]) == False and prioridadeValida(lista[n+1][1][2]) == True:
                    temp = lista[n]
                    lista[n] = lista[n+1]
                    lista[n+1] = temp
                    print(lista)
            elif horaMaisProxima(lista[n][1][1], lista[n+1][1][1]) == lista[n+1][1][1]:
                if horaValida(lista[n][1][1]) == True and horaValida(lista[n+1][1][1]) == True:
                    if lista[n][1][2] >= lista[n+1][1][2]:
                        temp = lista[n]
                        lista[n] = lista[n+1]
                        lista[n+1] = temp
                    elif prioridadeValida(lista[n][1][2]) == False and prioridadeValida(lista[n+1][1][2]) == True:
                        temp = lista[n]
                        lista[n] = lista[n+1]
                        lista[n+1] = temp
                        print(lista)                   
            n = n+1
    return lista

   
def ordenarPorPrioridade(lista):
    for x in lista:
        n = 0
        while n < len(lista) -1:
            if prioridadeValida(lista[n][1][2]) == True and prioridadeValida(lista[n+1][1][2]):
                if lista[n][1][2] > lista[n+1][1][2]:
                    temp = lista[n]
                    lista[n] = lista[n+1]
                    lista[n+1] = temp
            elif prioridadeValida(lista[n][1][2]) == False and prioridadeValida(lista[n+1][1][2]) == True:                
                temp = lista[n]
                lista[n] = lista[n+1]
                lista[n+1] = temp                
            n = n+1
    return lista
# Esta função processa os comandos e informações passados através da linha de comando e identifica
# que função do programa deve ser invocada. Por exemplo, se o comando 'adicionar' foi usado,
# isso significa que a função adicionar() deve ser invocada para registrar a nova atividade.
# O bloco principal fica responsável também por tirar espaços em branco no início e fim dos strings
# usando o método strip(). Além disso, realiza a validação de horas, datas, prioridades, contextos e
# projetos. 
def processarComandos(comandos):
  print(comandos)
  if comandos[1] == ADICIONAR:
    comandos.pop(0) # remove 'agenda.py'
    comandos.pop(0) # remove 'adicionar'
    itemParaAdicionar = organizar([' '.join(comandos)])[0]
    # itemParaAdicionar = (descricao, (prioridade, data, hora, contexto, projeto))
    adicionar(itemParaAdicionar[0], itemParaAdicionar[1]) # novos itens não têm prioridade
  elif comandos[1] == LISTAR:
    listar()    
  else :
    print("Comando inválido.")
  
    
  #('sadasd',('','','',''))
# sys.argv é uma lista de strings onde o primeiro elemento é o nome do programa
# invocado a partir da linha de comando e os elementos restantes são tudo que
# foi fornecido em sequência. Por exemplo, se o programa foi invocado como
#
# python3 agenda.py a Mudar de nome.
#
# sys.argv terá como conteúdo
#
# ['agenda.py', 'a', 'Mudar', 'de', 'nome']
processarComandos(sys.argv)





