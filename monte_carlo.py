import random, time

def funFx(expressão, x):
    return eval(expressão)

def funGx(expressão, x):
    return eval(expressão)

class monteCarlo():
    def __init__(self):
        self.num_pontos_dentro = 0
        self.fx = input('Digite a função OBS: Utilize a sintaxe do python F(x) = ')
        self.gx = input('Digite a função OBS: Utilize a sintaxe do python G(x) = ')
        self.a = int(input('Digite o valor de a: '))
        self.b = int(input('Digite o valor de b: '))
        self.total_pontos = int(input('Digite o total de pontos: '))
        self.m = self.b + 10
        maior_y = 0
        for i in range(int(self.a), int(self.b)+1):
            y = funFx(self.fx, i)
            if y > maior_y:
                maior_y = y
        self.n = int(maior_y * 2)
    
    def sortearPontos(self):
        for i in range(self.total_pontos):
            x = random.randint(self.a-2, self.m)
            y = random.randint(0, self.n)
            if self.a <= x <= self.b:
                if funGx(self.gx, x) <= y <= funFx(self.fx, x):
                    self.num_pontos_dentro += 1 

    def calcularArea(self):
        self.total_pontos = self.total_pontos
        areaDoRetangulo = self.m * self.n
        self.sortearPontos()
        area = (self.num_pontos_dentro/self.total_pontos) * areaDoRetangulo
        return area


seed = input('Digite a semente randomica: ')
if not seed:
    random.seed(time.time())
else:
    random.seed(seed)

teste1 = monteCarlo()
print(teste1.calcularArea())
print(teste1.num_pontos_dentro)