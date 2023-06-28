class Human:
    def __init__(self, fn, ln, age):
        self.fn = fn
        self.ln = ln
        self.age = age


class Student(Human):  # Student is Human
    def __init__(self, fn, ln, age, grade):
        self.grade = grade
        super().__init__(fn, ln, age)


class Teacher(Human):  # Teacher is Human
    def __init__(self, fn, ln, age, exp):
        self.exp = exp
        super().__init__(fn, ln, age)


student = Student('Taras', 'Sheketa', '22', 3)
teacher = Teacher('Alex', 'Sheketa', '22', 5)

print(f'{student.ln} {student.fn} {student.age} {student.grade}')
print(f'{teacher.ln} {teacher.fn} {teacher.age} {teacher.exp}')


#############################

class EngineGas:
    def __init__(self, volume, power):
        self.volume = volume
        self.power = power

    def info(self):
        return f'power: {self.power} volume: {self.volume}'


class EngineElectric:
    def __init__(self, power, capacity):
        self.capacity = capacity
        self.power = power

    def info(self):
        return f'power: {self.power} capacity: {self.capacity}'


class Car:  # Car has Engine
    def __init__(self, color, engine):
        self.color = color
        self.engine = engine


engine = EngineGas(volume='3', power='100')
engine2 = EngineElectric(capacity='5', power='200')


car = Car(color='red', engine=engine2)

print(f'color: {car.color} {car.engine.info()}')


class A:
    def __init__(self):
        self.foo = 1
