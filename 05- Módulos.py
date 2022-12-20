# Módulo Math: Funções básicas

Ceil = arredondamento para cima
floor = arredondamento para baixo
trunc = elimina o numero da virgula pra frente, deixando o  numero inteiro 
pow = potência 
sqrt = raiz quadrada
factorial = fatorial

import math = importa o modulo inteiro

from math import ceil = importa somente essa função

-   -   -   -   -   -   -   -   -   -   -   -   -   -   -   -   -
# EXEMPLO DE IMPORTAÇÃO

import math
num = int(input(' Digite um numero: '))
raiz = math.sqrt(num)
print ('A raiz de {} é igual a {}'.format(num, raiz)
---------------
#resultado

Digite um numero: 81
A raiz de 81 é igual a 9.0 
-------------------------------------------------------------

from math import sqrt, floor

num = int(input(' Digite um numero: '))
raiz = math.sqrt(num)
print ('A raiz de {} é igual a {:.2f}'.format(num, floor(raiz))) 

-------------------------------------------------------------
