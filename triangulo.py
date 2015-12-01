class Segmento:
    def __init__(self, p1, p2):
        self.p1 = p1
        self.p2 = p2

    def comprimento(self):
        return ((self.p1[0] - self.p2[0]) ** 2 + (self.p1[1] - self.p2[1]) ** 2) ** (0.5)

    def sinal(self, pt):
        return (pt[0] - self.p2[0]) * (self.p1[1] - self.p2[1]) - (self.p1[0] - self.p2[0]) * (pt[1] - self.p2[1])

    def __repr__(self):
        return "Segmento(%s, %s, %f)" % (str(self.p1), str(self.p2), self.comprimento())

    def __lt__(self, o):
        return self.comprimento() < o.comprimento()

class Triangulo:
    def __init__(self, ps):
        self.pontos = ps

    def lados(self):
        return [Segmento(self.pontos[0], self.pontos[1]),
                Segmento(self.pontos[1], self.pontos[2]),
                Segmento(self.pontos[2], self.pontos[0])]

    def inside(self, pt):
        [b1, b2, b3] = [p.sinal(pt) < 0.0 for p in self.lados()]
        return (b1 == b2) and (b2 == b3)


t = Triangulo([(1, 1), (2, 2), (2, 1)])
print(t.lados())
print(sorted(t.lados()))

vs = [x / 10 for x in  range(30)]


dentro = []
fora = []
for x in vs:
    for y in vs:
        if t.inside((x,y)):
            dentro.append((x,y))
        else:
            fora.append((x,y))

print(dentro)
print(fora)
