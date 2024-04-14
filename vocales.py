def contar_vocales(palabra):
    resultado = {}
    for letra in palabra:
        letra_min = letra.lower()  # Convertimos la letra a minúscula para considerar mayúsculas y minúsculas
        if letra_min in "aeiou":
            if letra_min in resultado:
                resultado[letra_min] += 1
            else:
                resultado[letra_min] = 1

    return resultado
