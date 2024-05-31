class Passaro:
    def voar(self):
        print("Voando ...")


class Pardal(Passaro):
    def voar(self):
        print("Pardar pode voar.")

class Avestruz(Passaro):
    def voar(self):
        print("Avestruz não pode voar")

# FIXME: exemplo ruim de uso de henrança para "ganhar" o método voar
class Aviao(Passaro):
    def voar(self):
        print("Avião está decolando ...")


def plano_voo(obj):
    obj.voar()


plano_voo(Pardal())
plano_voo(Avestruz())
plano_voo(Aviao())