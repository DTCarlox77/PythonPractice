from tools import auth, payments

usuario = {
    "username" : "Luisa",
    "saldo" : 5000
}

print(auth.login(usuario))

print(payments.modficar_saldo(usuario, -1000))
