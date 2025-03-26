# Explicação do Projeto
- Na linha um, temos a assinatura da função, que recebe o array com os valores a serem analisados (array), o índice inicial (left) e o índice final (right) do array.
- Na primeira condicional (linha 2), se o array tiver apenas um elemento, ele é o máximo e o mínimo ao mesmo tempo.
- Na segunda condicional (linha 6 até a linha 10), uma única comparação é feita caso hajam apenas dois elementos no array para ver qual é o maior e qual é o menor.
- Nas linhas 12, 13 e 14 respectivamente, o array é dividido ao meio e o algoritmo é chamado para cada metade.
- o left e mid + 1 servem para indicar qual pedaço da lista estamos analisando em cada chamada recursiva. Como usamos a abordagem de divisão e conquista, essas variáveis vão mudando conforme dividimos a lista em partes menores.
- No contexto da divisão e conquista, o algoritmo segue os três pilares: divisão, recursão e combinação. Na primeira etapa o array é dividido ao meio, na segunda o algoritmo é chamado para cada metade e na terceira o maior global é o maior entre os dois máximos, enquanto o menor é o menor entre os dois mínimos.

# Como Executar o Código No Ambiente Local
- Ter o Python instalado na máquina
- Ter uma IDE instalada (VSCode, Pycharm)
- Clonar o repositório
- Abrir o repositório na IDE
- Pelo terminal da IDE, executar o comando "python maxmin.py"

# Relatório Técnico
- O array analisado tem n elementos, que é dividido ao meio resultando em dois subarrays de tamanho 𝑛/2. Cada subarray encontra seu próprio mínimo e máximo de forma recursiva.
- Quando as duas partes retornam, precisamos comparar:
    1. Os dois valores mínimos encontrados → 1 comparação
    2. Os dois valores máximos encontrados → 1 comparação
Ou seja, a cada nível da recursão, fazemos 2 comparações adicionais além do custo recursivo.
- O número total de comparações cresce de forma linear com o tamanho da entrada, pois a equação final C(n) = 3n/2 - 2 está na ordem de 
O(n).
- Recorrência: T(n)=2T(n/2)+O(1)

# Pergunta 1: 
Comparando o teorema mestre com a recorrência
a = 2
b = 2
f(n) = O(1)

# Pergunta 2: 
p = log b a = log 2 2=1

# Pergunta 3: 
A recorrência se encaixa no caso 1 do Teorema Mestre, pois se o f(n) = O(1), significa que o expoente do n é 0. 0 é menor do que 1, que é o valor do p. Se c < p, então se encaixa no primeiro caso.

# Pergunta 4: 
A complexidade assintótica é O(n) e isso se confirma pela recorrência se encaixar no caso 1 do Teorema Mestre.