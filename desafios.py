'''1) Dado a sequência de Fibonacci, onde se inicia por 0 e 1 e o próximo valor sempre será a soma dos 2 valores anteriores 
(exemplo: 0, 1, 1, 2, 3, 5, 8, 13, 21, 34...), escreva um programa na linguagem que desejar onde, informado um número, 
ele calcule a sequência de Fibonacci e retorne uma mensagem avisando se o número informado pertence ou não a sequência.'''

def fibonacci_sequence(n):
  if n < 0:
    return "Número Inválido"

  elif n == 0:
    return "0 pertence a sequência Fibonacci"

  else:
    a = 0
    b = 1
    while b <= n:
      if b == n:
        return f"{n} pertence a sequência Fibonacci"
      a, b = b, a + b
    return f"{n} não pertence a sequência Fibonacci"

num = int(input("Digite um número: "))

print(fibonacci_sequence(num))


'''2) Escreva um programa que verifique, em uma string, a existência da letra 'a', seja maiúscula ou minúscula, 
além de informar a quantidade de vezes em que ela ocorre.
'''

def check_string(text):
  count = text.lower().count('a')
  if count > 0:
    print(f"'a' está presente em '{text}' e aparece {count} vezes")
  else:
    print(f"'a' não aparece em '{text}'")

text = input("Digite a string: ")

check_string(text)


'''3) Observe o trecho de código abaixo: 
int INDICE = 12, SOMA = 0, K = 1; enquanto K < INDICE faça { K = K + 1; SOMA = SOMA + K; } imprimir(SOMA);
Ao final do processamento, qual será o valor da variável SOMA?'''

INDICE = 12
SOMA = 0
K = 1

while K < INDICE:
  K = K + 1
  SOMA = SOMA + K
print(SOMA) 

#RESULTADO = 77


'''4) Descubra a lógica e complete o próximo elemento:
a) 1, 3, 5, 7, _9_
b) 2, 4, 8, 16, 32, 64, __128__
c) 0, 1, 4, 9, 16, 25, 36, __49__
d) 4, 16, 36, 64, __100__
e) 1, 1, 2, 3, 5, 8, __13__
f) 2, 10, 12, 16, 17, 18, 19, __200__'''


'''5) Você está em uma sala com três interruptores, cada um conectado a uma lâmpada em salas diferentes. 
Você não pode ver as lâmpadas da sala em que está, mas pode ligar e desligar os interruptores quantas vezes quiser. 
Seu objetivo é descobrir qual interruptor controla qual lâmpada. 
Como você faria para descobrir, usando apenas duas idas até uma das salas das lâmpadas, qual interruptor controla cada lâmpada?'''

'''Passos:
Vamos chamar os três interruptores de A, B e C, e as três lâmpadas de L1, L2 e L3. 

Primeira ida:

Ligue o interruptor A e deixe-o ligado por alguns minutos. Isso fará com que a lâmpada correspondente a A aqueça.
Depois de alguns minutos, desligue o interruptor A e ligue o interruptor B.
Vá para a sala das lâmpadas.

Na sala das lâmpadas (primeira ida):

A lâmpada que está acesa corresponde ao interruptor B (pois o interruptor B foi ligado por último).
A lâmpada que está apagada, mas quente corresponde ao interruptor A (porque você deixou o interruptor A ligado por alguns minutos antes de desligá-lo).
A lâmpada que está apagada e fria corresponde ao interruptor C (porque o interruptor C nunca foi ligado).'''