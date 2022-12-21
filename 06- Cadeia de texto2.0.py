# Manipulando texto

frase = 'Curso em Video python'
print(frase[3])
Resultado: s


frase = 'Curso em Video python'
print(frase[3:13])
Resultado: so em Vide


frase = 'Curso em Video python'
print(frase[1:15])
Resultado: urso em Video 


frase = 'Curso em Video python'
print(frase[1:15:2])
Resultado:us mVdo


frase = 'Curso em Video python'
print(frase[:15:2])
Resultado: Croe ie 


frase = 'Curso em Video python'
print(frase[::2])
Resultado: Croe ie yhn

#COLOCANDO A VARIAVEL EM LETRA MAIUSCULA

frase = 'Curso em video python'
print(frase.upper().count('O'))
Resultado:3
  
# CONTAR TAMANHO DA VARIAVEL

frase = 'curso em video python'
print(len(frase))
Resultado:21

# trocando uma palavra por outra em apenas uma linha

frase = 'curso em video python'
print(frase.replace('python', 'android'))
Resultado: curso em video android

# trocando uma palavra por outra na variavel

frase = 'curso em video python'
frase = print(frase.replace('python', 'android'))
Resultado: curso em video android

-------------------------------------------
# saber se a palavra curso está dentro da variavel frase

frase = 'Curso em Video Python'
print('Curso' in frase)
Resultado: True

# saber a posição da palavra dentro da variavel
frase = 'Curso em Video Python'
print( frase.find('Curso'))
Resultado: 0

#colocando a frase em minusculo 
frase = 'Curso em Video Python'
print( frase.lower().find('python'))
Resultado: 15
----------------------------------------
# Dividindo frase com split

frase = 'Curso em video python'
print(frase.split())
Resultado: ['Curso', 'em', 'video', 'python']

# Mostrando o primeiro item da lista

frase = 'Curso em video python'
dividido = frase.split()
print(dividido[0])
Resultado: Curso


# Dividindo o primeiro item da lista e mostrando a respecitiva letra

frase = 'Curso em video python'
dividido = frase.split()
print(dividido[0] [3])
Resultado: s  
  
  
  
  
  
