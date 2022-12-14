'''
Um carrinho elétrico, que usa apenas uma bateria com carga inicial de C coulombs, tem uma
característica incrível: ele só pode ir à velocidade constante mas pode escolher qualquer velocidade
constante, maior do que zero, de V metros por segundo. Só que quanto maior a velocidade, menor a
autonomia. Quer dizer, de maneira mais rigorosa, a distância máxima dmax metros que ele pode
percorrer é diretamente proporcional à carga inicial da bateria e inversamente proporcional à
velocidade: dmax = C/V. É incrível mas veja que, mesmo que a carga seja muito pequena, o carrinho
sempre pode percorrer qualquer distância, desde que vá a uma velocidade suficientemente
pequena!
O carrinho está na posição zero de uma pista reta com comprimento D metros. Há N baterias, com
diferentes cargas, colocadas em posições distintas ao longo da pista, uma delas na posição zero.
Considere que nosso carrinho ideal consegue fazer um pit-stop instantâneo, trocando de bateria sem
perder tempo algum. Ao passar por uma nova bateria ele pode decidir ou não fazer a troca; e ele
pode alterar sua velocidade apenas num instante em que troca de bateria. Qual é o tempo mínimo
possível para o carrinho chegar ao final da pista?

Entrada
A primeira linha da entrada contém um inteiro N e um real D, respectivamente, o número de baterias
e o comprimento da pista. As N linhas seguintes contêm, cada uma, dois reais P e C definindo,
respectivamente, a posição e a carga das baterias. Sempre existe uma bateria na posição 0.0 e as
baterias são dadas em ordem estritamente crescente de posição.

Saída
Imprima uma linha contendo um real, com exatamente três casas decimais, o tempo mínimo possível
em segundos para o carrinho chegar ao final da pista
'''
'''
Restrições:
1 ≤ nBaterias ≤ 1000 e 1.0 ≤ dPista ≤ 10000.0

0.0 ≤ Pos < dPista e 0.0 < Carga < 100.0
'''

while True:
    entrada = input().split(" ") # 4 10.000 (mesma linha)
    n_baterias = int(entrada[0])
    dist = float(entrada[1])
    if (n_baterias >= 1 and n_baterias <= 1000) and (dist >= 1 and dist <= 10000): #Restrição
        break

bat_pos = []
bat_car = []

print('\n')
for i in range(n_baterias):
    while True:
        entrada = input().split(" ")    
        pos = float(entrada[0])
        carga = float(entrada[1])
        # 0.000  1.000  
        # 1.200  0.100
        # 3.000  10.000
        # 7.700  1.000
        if (0 <= pos and pos < dist) and (0 < carga and carga < 100):  # Restrição
            break
    bat_pos.append(pos)     #Armazenar a posição
    bat_car.append(carga)   #Armazenar a carga

bat_pos.append(dist)    # Armazenar a distância final

#Declaração das variáveis
tempo = 0
aux_tempo = 0

pivo_pos = 0
pivo_tempo = 0
tot_tempo = 0

def calcTime(pos_init, pos_end, carga): # Função para calcular o tempo
    diff_pos = pos_end - pos_init
    velocity = carga / diff_pos
    return diff_pos / velocity

for i in range(n_baterias):       # Comparação de tempo
    tempo = calcTime(bat_pos[i], bat_pos[i+1], bat_car[i])
    aux_tempo = calcTime(bat_pos[pivo_pos], bat_pos[i+1], bat_car[pivo_pos])

    if tempo <= aux_tempo:  # Guardar posição
        pivo_pos = i
    else:                   # Guardar tempo
        pivo_tempo = aux_tempo

    if tempo <= aux_tempo or i == n_baterias-1:
        tot_tempo += pivo_tempo
        pivo_tempo = tempo

print(f"{tot_tempo:.3f}")
