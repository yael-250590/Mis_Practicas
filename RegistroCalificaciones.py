def mostrar_encabezado_escuela():
    print("Institucion: Universiad Tecnologica de Xicotepec de Juarez Puebla/n Titulo: Reporte De Calificaciones")
mostrar_encabezado_escuela()

def nota_minima_aprobatoria():
    return 6.0
nota_minima_aprobatoria()
def evaluar_rendimiento(nota_final):
    if nota_final < 6.9:
        return f"Estás Reprobado, suerte para la próxima. Tu nota final es de {nota_final}, ¡¡NECESITAS EXAMEN EXTRAORDINARIO!!"
    elif nota_final <= 9.4:
        return f"¡¡¡Felicidades!!! Estás Aprobado. Tu calificación final fue de: {nota_final}"
    elif nota_final <= 10.0:
        return f"¡Excelente! Has pasado con una excelente calificación: {nota_final}"
    else:
        return "Dato no válido"
evaluar_rendimiento(4)

def calcular_promedio_ponderado(nota_examenes, nota_tareas):
    return round((nota_examenes * 0.70) + (nota_tareas * 0.30), 1)
calcular_promedio_ponderado(8.3,10)

def generar_boleta(nombre_alumno, nota_examenes, nota_tareas):
    promedio = calcular_promedio_ponderado(nota_examenes, nota_tareas)
    minima = nota_minima_aprobatoria()
    rendimiento = evaluar_rendimiento(promedio)
    
    print(f"****************************************\n"
          f"BOLETA:\n"
          f" Nombre: {nombre_alumno} \n"
          f" Promedio Final: {promedio} \n"
          f" Nota Mínima: {minima} \n"
          f" {rendimiento}")

generar_boleta("Cesar", 7, 6)

