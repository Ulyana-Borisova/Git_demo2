class Rosa:     #создаём класс
    biology_class = 'flowers'   #статичный методб относится ко всем объектам класса
    def __init__(self, title, __height, color):  #задаём свойства класса при помоши конструктора, используем инит, передаём атрибуты (свойства)
        self.title = title         #задаём аргументы
        self.height = __height       #задаём аргументы
        self.color = color         #задаём аргументы
    def beautiful(self):
        return 'I am very beautiful'  #задаём метод (поведение)
    def get_title(self):
        return f'Hello! I am {self.title}'
    def set_title(self, new_title):
        self.title = new_title

Rosa1 = Rosa ('Aida', 25, 'red')  #создаём объект класса
print(Rosa1.title)                  #смотрим атрибуты
print(Rosa1.color)                  #смотрим атрибуты
print(Rosa1.beautiful())            #смотрим методы
print(Rosa1.get_title())            #смотрим методы
print(Rosa1.biology_class)

#
Rosa2 = Rosa ('Tiffany', 40, 'Yellow')
print(Rosa2.color)
print(Rosa2.biology_class)
print(Rosa2.get_title())
Rosa2.title = 'Mr. Lincoln'
print(Rosa2.get_title())
print(Rosa2.height)


class Tulpan(Rosa):                #создаём подкласс
    def __init__(self, title, height, color, smell):
        super().__init__(title, height, color)
        self.smell = smell

    def old(self):
        return 'I am perennial plant'

Tulpan1 = Tulpan('White Prince', 20, 'white', 'ght fragrance')
print(Tulpan1.get_title())
print(Tulpan1.height)
print(Tulpan1.biology_class)