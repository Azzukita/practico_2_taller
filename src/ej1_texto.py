def analizar_texto(texto):
    # Separar en lineas
    lineas = texto.split("\n")

    # Cantidad total de lineas
    total_lineas = len(lineas)

    # Palabras por linea
    palabras_por_linea = [len(linea.split()) for linea in lineas]

    # Total de palabras
    total_palabras = sum(palabras_por_linea)

    # Promedio de palabras por linea
    promedio = total_palabras / total_lineas

    # Lineas sobre el promedio
    lineas_sobre_promedio = [linea for linea, cant in zip(lineas, palabras_por_linea)
                             if cant > promedio]

    # Mostrar resultados
    print(f"Total de lineas:           {total_lineas}")
    print(f"Total de palabras:         {total_palabras}")
    print(f"Promedio palabras/linea:   {promedio:.2f}")
    print(f"\nLineas sobre el promedio ({promedio:.2f} palabras):")
    for linea in lineas_sobre_promedio:
        print(f"  - {linea}")
        
        
        
        
texto = """Beautiful is better than ugly.
Explicit is better than implicit.
Simple is better than complex.
Complex is better than complicated.
Flat is better than nested.
Sparse is better than dense.
Readability counts.
Special cases aren't special enough to break the rules.
Although practicality beats purity.
Errors should never pass silently.
Unless explicitly silenced.
In the face of ambiguity, refuse the temptation to guess.
There should be one-- and preferably only one --obvious way to do it.
Although that way may not be obvious at first unless you're Dutch.
Now is better than never.
Although never is often better than *right* now.
If the implementation is hard to explain, it's a bad idea.
If the implementation is easy to explain, it may be a good idea.
Namespaces are one honking great idea -- let's do more of those!"""