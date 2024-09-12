# README

Este documento descreve a solução para uma série de problemas de programação e raciocínio lógico. Cada seção inclui um problema, a solução proposta em Python e uma breve explicação.

## Problemas e Soluções

### 1. Sequência de Fibonacci

**Problema:** Dado um número, determine se ele pertence à sequência de Fibonacci.

**Código:**

```python
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
```

**Explicação:**  A função `fibonacci_sequence` verifica se um número 'n' pertence à sequência de Fibonacci, retornando uma mensagem correspondente. O código utiliza uma abordagem iterativa para gerar os números de Fibonacci até o valor de 'n'.


### 2. Verificação da Letra 'a' em uma String

**Problema:** Verifique a existência da letra 'a' (maiúscula ou minúscula) em uma string e conte quantas vezes ela aparece.

**Código:**

```python
def check_string(text):
    count = text.lower().count('a')
    if count > 0:
        print(f"'a' está presente em '{text}' e aparece {count} vezes")
    else:
        print(f"'a' não aparece em '{text}'")

text = input("Digite a string: ")
check_string(text)
```

**Explicação:**  A função `check_string` utiliza o método `count` para contar a ocorrência da letra 'a' em uma string, considerando ambos os casos (maiúsculo e minúsculo). O resultado é exibido para o usuário.


### 3. Cálculo da Soma

**Problema:** Determine o valor da variável `SOMA` ao final do processamento do código fornecido.

**Código:**

```python
INDICE = 12
SOMA = 0
K = 1

while K < INDICE:
    K = K + 1
    SOMA = SOMA + K
print(SOMA)
```
**Explicação:** O código realiza a soma dos números inteiros de 2 a 11. O resultado da soma é `77`.


### 4. Sequências Numéricas

**Problema:** Complete a próxima sequência para os seguintes padrões:

a) 1, 3, 5, 7, __9__

b) 2, 4, 8, 16, 32, 64, __128__

c) 0, 1, 4, 9, 16, 25, 36, __49__

d) 4, 16, 36, 64, __100__

e) 1, 1, 2, 3, 5, 8, __13__

f) 2, 10, 12, 16, 17, 18, 19, __200__

**Explicação:**

- a) Sequência de números ímpares.
- b) Sequência de potências de 2.
- c) Quadrados perfeitos.
- d) Quadrados perfeitos pares.
- e) Sequência de Fibonacci.
- f) Sequência de números iniciando com a letra 'D'.

### 5. Identificação de Interruptores e Lâmpadas

**Problema:** Determine qual interruptor controla qual lâmpada usando apenas duas idas à sala das lâmpadas.

**Solução:**

**Passos:**

1. Ligue o interruptor A e deixe-o ligado por alguns minutos para aquecer a lâmpada correspondente. Desligue o interruptor A e ligue o interruptor B.
2. Vá para a sala das lâmpadas.

**Na sala das lâmpadas (primeira ida):**

- A lâmpada acesa corresponde ao interruptor B (foi ligado por último).
- A lâmpada apagada, mas quente corresponde ao interruptor A (foi ligado por algum tempo e depois desligado).
- A lâmpada apagada e fria corresponde ao interruptor C (nunca foi ligado).

**Explicação:** Esta abordagem utiliza a combinação de estado (aceso/apagado) e temperatura para identificar corretamente a relação entre interruptores e lâmpadas.
