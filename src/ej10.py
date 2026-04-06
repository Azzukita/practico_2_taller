rounds = [
    {
        'theme': 'Entrada',
        'scores': {
            'Valentina': {'judge_1': 8, 'judge_2': 7, 'judge_3': 9},
            'Mateo':     {'judge_1': 7, 'judge_2': 8, 'judge_3': 7},
            'Camila':    {'judge_1': 9, 'judge_2': 9, 'judge_3': 8},
            'Santiago':  {'judge_1': 6, 'judge_2': 7, 'judge_3': 6},
            'Lucia':     {'judge_1': 8, 'judge_2': 8, 'judge_3': 8},
        }
    },
    {
        'theme': 'Plato principal',
        'scores': {
            'Valentina': {'judge_1': 9, 'judge_2': 9, 'judge_3': 8},
            'Mateo':     {'judge_1': 8, 'judge_2': 7, 'judge_3': 9},
            'Camila':    {'judge_1': 7, 'judge_2': 6, 'judge_3': 7},
            'Santiago':  {'judge_1': 9, 'judge_2': 8, 'judge_3': 8},
            'Lucia':     {'judge_1': 7, 'judge_2': 8, 'judge_3': 7},
        }
    },
    {
        'theme': 'Postre',
        'scores': {
            'Valentina': {'judge_1': 7, 'judge_2': 8, 'judge_3': 7},
            'Mateo':     {'judge_1': 9, 'judge_2': 9, 'judge_3': 8},
            'Camila':    {'judge_1': 8, 'judge_2': 7, 'judge_3': 9},
            'Santiago':  {'judge_1': 7, 'judge_2': 7, 'judge_3': 6},
            'Lucia':     {'judge_1': 9, 'judge_2': 9, 'judge_3': 9},
        }
    },
    {
        'theme': 'Cocina internacional',
        'scores': {
            'Valentina': {'judge_1': 8, 'judge_2': 9, 'judge_3': 9},
            'Mateo':     {'judge_1': 7, 'judge_2': 8, 'judge_3': 7},
            'Camila':    {'judge_1': 9, 'judge_2': 8, 'judge_3': 8},
            'Santiago':  {'judge_1': 8, 'judge_2': 9, 'judge_3': 7},
            'Lucia':     {'judge_1': 8, 'judge_2': 7, 'judge_3': 8},
        }
    },
    {
        'theme': 'Final libre',
        'scores': {
            'Valentina': {'judge_1': 9, 'judge_2': 8, 'judge_3': 9},
            'Mateo':     {'judge_1': 8, 'judge_2': 9, 'judge_3': 8},
            'Camila':    {'judge_1': 7, 'judge_2': 8, 'judge_3': 7},
            'Santiago':  {'judge_1': 9, 'judge_2': 9, 'judge_3': 9},
            'Lucia':     {'judge_1': 7, 'judge_2': 8, 'judge_3': 7},
        }
    }
]


# ------------------------------------------------------------
# FUNCION 1: calcular el puntaje de un participante en una ronda
# Recibe un diccionario con los puntajes de los 3 jueces
# Retorna la suma de los 3 puntajes
def calcular_puntaje_ronda(puntajes_jueces):
    return sum(puntajes_jueces.values())

# ------------------------------------------------------------
# FUNCION 2: encuentra a el ganador de una ronda
# Recibe un diccionario {participante: puntaje_ronda}
# Retorna el nombre del participante con mayor puntaje

def obtener_ganador_ronda(puntajes_ronda):
    return max(puntajes_ronda, key=puntajes_ronda.get)

# ------------------------------------------------------------
# FUNCION 3: imprime la tabla de posiciones de una ronda
# Recibe el nombre de la ronda, el ganador, los puntajes
# de la ronda y los puntajes acumulados hasta el momento

def imprimir_tabla_ronda(theme, ganador, puntajes_ronda, acumulado):
    print(f"\n{'='*55}")
    print(f"  RONDA: {theme}")
    print(f"  Ganador de la ronda: {ganador} ({puntajes_ronda[ganador]} pts)")
    print(f"{'='*55}")
    print(f"{'Pos':<5} {'Participante':<15} {'Ronda':>6} {'Acumulado':>10}")
    print(f"{'-'*55}")

    # Ordenar por puntaje acumulado de mayor a menor
    ranking = sorted(acumulado, key=acumulado.get, reverse=True)

    for posicion, participante in enumerate(ranking, start=1):
        print(f"{posicion:<5} {participante:<15} "
              f"{puntajes_ronda[participante]:>6} "
              f"{acumulado[participante]:>10}")


# ------------------------------------------------------------
# FUNCION 4: imprime la tabla final de la competencia
# Recibe el acumulado, rondas ganadas, mejor puntaje
# y cantidad de rondas jugadas
def imprimir_tabla_final(acumulado, rondas_ganadas, mejor_puntaje, total_rondas):
    print(f"\n{'='*65}")
    print(f"  TABLA FINAL DE LA COMPETENCIA")
    print(f"{'='*65}")
    print(f"{'Pos':<5} {'Participante':<15} {'Total':>7} "
          f"{'Rondas gan.':>12} {'Mejor':>7} {'Promedio':>9}")
    print(f"{'-'*65}")

    # Ordenar por puntaje total de mayor a menor
    ranking_final = sorted(acumulado, key=acumulado.get, reverse=True)

    for posicion, participante in enumerate(ranking_final, start=1):
        promedio = acumulado[participante] / total_rondas
        print(f"{posicion:<5} {participante:<15} "
              f"{acumulado[participante]:>7} "
              f"{rondas_ganadas[participante]:>12} "
              f"{mejor_puntaje[participante]:>7} "
              f"{promedio:>9.2f}")



# FUNCION PRINCIPAL: simula la competencia completa. Recibe la lista de rondas y coordina todas las funciones

def simular_competencia(rounds):

    # Obtener la lista de participantes de la primera ronda
    participantes = list(rounds[0]['scores'].keys())

    # Inicializar los acumuladores de cada participante en 0
    acumulado      = {p: 0 for p in participantes}
    rondas_ganadas = {p: 0 for p in participantes}
    mejor_puntaje  = {p: 0 for p in participantes}

    # Procesar cada ronda
    for ronda in rounds:
        theme  = ronda['theme']
        scores = ronda['scores']

        # Calcular el puntaje de cada participante en esta ronda
        puntajes_ronda = {
            participante: calcular_puntaje_ronda(scores[participante])
            for participante in participantes
        }

        # Determinar el ganador de esta ronda
        ganador = obtener_ganador_ronda(puntajes_ronda)
        rondas_ganadas[ganador] += 1

        # Actualizar el acumulado y el mejor puntaje de cada participante
        for participante in participantes:
            acumulado[participante]     += puntajes_ronda[participante]
            mejor_puntaje[participante]  = max(
                mejor_puntaje[participante],
                puntajes_ronda[participante]
            )

        # Mostrar la tabla de posiciones de esta ronda
        imprimir_tabla_ronda(theme, ganador, puntajes_ronda, acumulado)

    # Mostrar la tabla final al terminar todas las rondas
    imprimir_tabla_final(acumulado, rondas_ganadas, mejor_puntaje, len(rounds))


# Llamar a la funcion principal
simular_competencia(rounds)