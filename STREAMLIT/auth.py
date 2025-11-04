# Simulación de una "base de datos" en memoria
usuarios = {"admin": "1234"}

def registrar(user, password):
    if not user or not password:
        return False
    if user in usuarios:
        return False
    usuarios[user] = password
    return True

def verificar(user, password):
    return user in usuarios and usuarios[user] == password