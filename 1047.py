# Passo 1: Ler os quatro números inteiros da entrada
hora_inicial, minuto_inicial, hora_final, minuto_final = map(int, input().split())

# Passo 2: Calcular a diferença entre a hora final e a hora inicial, convertendo horas em minutos
duracao = (hora_final * 60 + minuto_final) - (hora_inicial * 60 + minuto_inicial)

# Passo 3: Somar a diferença calculada no passo 2 com a diferença entre o minuto final e o minuto inicial
# Passo 4: Verificar se o resultado da soma do passo 3 é maior do que 1440 (24 horas em minutos)
if duracao <= 0:
    duracao += 1440

# Passo 5: Imprimir a mensagem com o resultado final
horas = duracao // 60
minutos = duracao % 60
print("O JOGO DUROU {} HORA(S) E {} MINUTO(S)".format(horas, minutos))
