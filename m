
def responder(input: str) -> str:
    return f"Hola Fraith, recibí: {input}"
    def responder(input: str) -> str:
    return f"Hola Fraith, recibí: {input}"

if _name_ == "_main_":
    while True:
        mensaje = input("Tú: ")
        if mensaje.lower() in ["salir", "exit"]:
            break
        respuesta = responder(mensaje)
        print("Agente:", respuesta)