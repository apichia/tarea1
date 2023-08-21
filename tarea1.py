# Vamos a definir un grafo con un diccionario de python cada clave va a ser un grafo.
grafo = {
    'A': ['B', 'C'],
    'B': ['D', 'E'],
    'C': ['F'],
    'D': [],
    'E': ['F'],
    'F': []
}

# aqui definimos la funcion para la busqueda dfs


def dfs(grafo, inicio, objetivo):
    visitados = set()
    pila = [(inicio, [inicio])]

    while pila:
        nodo, camino = pila.pop()

        if nodo == objetivo:
            return camino

        if nodo not in visitados:
            visitados.add(nodo)
            for vecino in grafo[nodo]:
                pila.append((vecino, camino + [vecino]))

    return None


# Busqueda en profundidad.
inicio = 'A'
objetivo = 'F'
resultado = dfs(grafo, inicio, objetivo)

# dondicicionales para mostrar el resultado.
if resultado:
    print(f"Se encontró un camino de {inicio} a {objetivo}: {resultado}")
else:
    print(f"No se encontró un camino de {inicio} a {objetivo}")
