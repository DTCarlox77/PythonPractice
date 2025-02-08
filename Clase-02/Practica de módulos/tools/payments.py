def modficar_saldo(usuario, monto):
    # Recibe un usuario (Diccionario) / Monto: Valor entero
    
    # Es una copia basada en el diccionario
    new_user = {
        "username" : usuario["username"],
        "saldo" : usuario["saldo"] + monto
    }
    
    return new_user