
respuestas = {
    "hola como estas": "muy bien en que puedo ayudarte",
    "donde se encuentran ubicados": "en la cra 29#50-20",
    "que curso tienen disponibles": "tenemos bootcamps de prograacion y analisis de datos",
    "cuando inician los cursos": "cada primera semana del mes",
    "cuanto dura el curso": "un mes y medio",
    "cuanto sura el certificado en llegar": "dura aproximadamente 2 meses"
}

def generar_respuesta(pregunta):
    if pregunta in respuestas:
        return respuestas[pregunta]
    else:
        return "no entiendo tu pregunta"
    
print("hola soy un chatbot en que puedo ayudarte\n")
while True:
    prompt = input("ingresa tu pregunta\n")
    if prompt == "salir":
        break
    respuesta = generar_respuesta(prompt)
    print(respuesta)