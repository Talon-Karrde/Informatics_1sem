class Vector():
    def __init__(self, x, y, z):
        self.x = x
        self.y = y
        self.z = z

    def __abs__(self):
        return (self.x**2 + self.y**2 + self.z**2)**0.5

    def __add__(self, other):
        if isinstance(other, Vector):
            return Vector(self.x + other.x, self.y + other.y, self.z + other.z)
        elif isinstance(other, int) or isinstance(other, float):
            return Vector(self.x + other, self.y + other, self.z + other)

    def __sub__(self, other):
        if isinstance(other, Vector):
            return Vector(self.x - other.x, self.y - other.y, self.z - other.z)
        elif isinstance(other, int) or isinstance(other, float):
            return Vector(self.x - other, self.y - other, self.z - other)

    def scal(self, other):
        return self.x * other.x + self.y * other.y + self.z * other.z

    def mult(self, num):
        return Vector(num * self.x, num * self.y, num * self.z)

    def __str__(self):
        return f'x = {self.x} y = {self.y} z = {self.z}'


vectors = []

while True:
    vector_str = input("Введите вектор в формате {x, y, z} (введите 'q' для завершения): ")
    if vector_str == 'q':
        break

    try:
        vector = vector_str.strip('{}').split(',')
        vectors.append(vector)
    except ValueError as e:
        print(f"Ошибка: {e}")



vectory = []

for i in range(len(vectors)):
    vec = Vector(int(vectors[i][0]), int(vectors[i][1]), int(vectors[i][2]))
    vectory.append(vec)
