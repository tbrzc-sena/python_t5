#5. Escriba un clase padre llamada Ave que herede a clases hijas con tipos de aves

class Ave:
    def __init__(self, tipo):
        self.tipo = tipo
    def volar(self):
        # Método vacío
        pass


class Paloma(Ave):
    pass


padre = Ave('rapaz')
paloma = Paloma('')
paloma.volar()