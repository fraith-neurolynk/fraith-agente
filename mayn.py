def responder(input: str) -> str:
    return f"Hola Fraith, recibí: {input}"

initial_message = "I am Charly, President of FRAITH FUTURAMA. How can I help you today?"
print(initial_message)

cuentas = [
    {"tipo": "Mercado Pago", "alias": "milenesk", "CVU": "0000003100023821023089"},
    {"tipo": "Wise UK", "IBAN": "GB87TCCL00997970078740"},
    {"tipo": "Wise US", "routing": "026073150", "account": "8334695514"},
    {"tipo": "PayPal", "usuario": "fraith@paypal.com"},
    {"tipo": "DolarApp", "usuario": "$frairhpabontorregrosa"},
    {"tipo": "Banco Galicia", "CVU": "0070704830004013279922"},
    {"tipo": "Lead Bank USA", "account": "216914122006"},
    {"tipo": "PAXSYS SA", "CBU": "4310009942700000082678"},
]

def responder_a_usuario(instruccion):
    if "cuentas" in instruccion:
        lista = ""
        for c in cuentas:
            for clave, valor in c.items():
                lista += f"{clave}: {valor} | "
            lista += "\n"
        return f"Estas son tus cuentas activas:\n{lista}"
    elif "alerta" in instruccion:
        return "Alerta enviada con exito."
    else:
        return "No entiendo la instruccion, fraith."

while True:
    pregunta = input("fraith: ")
    respuesta = responder_a_usuario(pregunta)
    print("charly:", respuesta)
    def foo():