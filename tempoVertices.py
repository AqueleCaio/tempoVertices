def temposVertices(listaAdj, v):
    # Inicialize o dicionário de tempos
    tempos = {}

    # Inicialize o tempo global
    tempo = [0]

    # Função auxiliar para DFS
    def DFS(v, tempo):
        # Marque o tempo de descoberta
        tempo[0] += 1
        tempos[v] = [tempo[0]]

        # Visite todos os vértices adjacentes
        for adj in sorted(listaAdj[v]):
            if adj not in tempos:
                DFS(adj, tempo)

        # Marque o tempo de término
        tempo[0] += 1
        tempos[v] = f"{tempos[v][0]}/{tempo[0]}"

    # Realize DFS no vértice inicial
    DFS(v, tempo)

    # Realize DFS em todos os outros vértices em ordem crescente
    for v in sorted(set(listaAdj.keys()) - {v}):
        if v not in tempos:
            DFS(v, tempo)

    # Construa uma string com todos os tempos dos vértices
    resp = ', '.join(f"{v}: '{tempos[v]}'" for v in sorted(tempos.keys()))

    # Imprima a string
    print('{' + resp + '}')
