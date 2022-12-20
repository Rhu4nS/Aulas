

#FASE 09

-------Manipular Cadeias de Texto:--------------

Exemplo: Uma variavel com 20 caracteres

FATIAMENTO de str:

Variavel[9]
identifica o caracter correspondente ao 9.

Variarvel[9:13]
seleciona do caracter 9 até o 12, pois o ultimo valor nao entra na contagem.

Variarvel[9:21]
começa no 9 e vai até o limite de caracteres, sendo ele, o 20.

Variavel[9:21:2]
começa no caracter 9 e vai até o ultimo pulando de duas em duas letras.
selecionando assim: 9-11-13-15-17-19.

Variavel [:5]
começa na str 0 e termina na str 5, incluindo apenas do 0 ao 4

Variavel [15:]

começa no 15 até o fim, sendo assim, do 15 ao 20

Variavel[9::3]
começa no 9 e vai até o final pulando de 3 em 3 str
selecionando assim: 9-12-15-18

-------------------------------------------
#ANÁLISE

Função len[variavel]
mostra o comprimento da variavel
------------------------
funçao count=
variavel.count('o')
conta todas as letras 'o' presentes na variavel

variavel.count('o',0,13)
conta a variavel 'o' do 0 ao 13
------------------------
função find = encontrar
variavel.find('deo')
encontrar a posição onde começou e terminou o 'deo' dentro da variavel

variavel.find('str que nao existe')
retorna o valor -1
------------------------
Operador in:
'qualquer informação' in variavel
encontra uma informação dentro da variavel e diz se é True or False
--------------------------------------------------------------------------
#TRANSFORMAÇÃO

função replace = substituir
variavel.replace('palavra1','palavra2')
substitui a palavra1 pela palavra2
------------------------------

função upper = maiusculo
variavel.upper()
tudo dentro da variavel vai ficar maiusculo
------------------------------

Função lower = minusculo
variavel.lower()
tudo dentro da variavel fica em minusculo
-------------------------------

Função capitalize = deixa a primeira letra em maiusculo e o resto em minusculo
variavel.capitalize()
-------------------------------

Função title = quantas palavras tem na variavel, onde tem espaço ele faz a quebra
variavel.title()
onde estiver quebra, a primeira letra fica maiuscula
-------------------------------

#Função strip

frase.strip()
remove os espaços desnecessarios
--------------------------------
função rstrip

frase.rstrip()
remove os ultimos espaços vazios da str
--------------------------------
função lstrip

frase.lstrip()
remove os primeiros espaços vazios da str
---------------------------------------------------------
#DIVISÃO

split

variavel.split()
faz a divisão da str e separa os pedaços e refaz a numeração de cada elemento
--------------------------
#JUNÇÃO

'-'.join(variavel)
faz a junçao da string e coloca - no lugar dos epaços, separando








