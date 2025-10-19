"""Crea un sistema de notificaciones.
 Requisitos:
 1. El sistema puede enviar Email, PUSH y SMS (implementaciones específicas).
 2. El sistema de notificaciones no puede depender de las implementaciones específicas.
 Instrucciones:
 1. Crea la interfaz o clase abstracta.
 2. Desarrolla las implementaciones específicas.
 3. Crea el sistema de notificaciones usando el DIP.
 4. Desarrolla un código que compruebe que se cumple el principio"""

from abc import ABC, abstractmethod

class AbstractNotifier(ABC):
    @abstractmethod
    def notifcador():
        pass

class EnviarEmail(AbstractNotifier):
    
    def notificador():
        print("Enviado por Email:")

class EnviarPush(AbstractNotifier):
    
    def notificador():
        print("Enviado por Push:")

class EnviarSMS(AbstractNotifier):
    
    def notificador():
        print("Enviado por SMS:")

class Message:
    def __init__(self, notificar:AbstractNotifier):

        self.notificar = notificar

    def enviar(self, tipoMensage: int):
        servicio = AbstractNotifier(EnviarSMS)
        servicio.enviar("Hola, notificador por sms")
        

class Message:
    def __init__(self, notificar:AbstractNotifier):

        self.notificar = notificar

