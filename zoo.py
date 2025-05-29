class Animal:
    def __init__(self, name, species, age):
        self.name = name
        self.species = species
        self.age = age
    
    def make_sound(self):
        if self.species.lower() == "лев":
            print(f"{self.name} говорит: Ррр!")
        elif self.species.lower() == "слон":
            print(f"{self.name} говорит: Тууу!")
        elif self.species.lower() == "змея":
            print(f"{self.name} говорит: Шшш!")
        else:
            print(f"{self.name} издает звук!")
    
    def info(self):
        age_str = f"{self.age} {'год' if self.age == 1 else 'года' if 2 <= self.age <= 4 else 'лет'}"
        print(f"Кличка: {self.name}\nВид: {self.species}\nВозраст: {age_str}")


class Zoo:
    def __init__(self):
        self.animals = []
    
    def add_animal(self, animal):
        self.animals.append(animal)
        print(f"Животное {animal.name} добавлено в зоопарк!")
    
    def show_animals(self):
        if not self.animals:
            print("В зоопарке пока нет животных.")
            return
        
        print("Животные в зоопарке:")
        for i, animal in enumerate(self.animals, 1):
            print(f"\n{i}.")
            animal.info()
    
    def make_all_sounds(self):
        if not self.animals:
            print("В зоопарке пока нет животных.")
            return
        
        print("Звуки животных в зоопарке:")
        for animal in self.animals:
            animal.make_sound()


# Пример использования
if __name__ == "__main__":
    my_zoo = Zoo()  # Создаём зоопарк
    
    # Добавляем животных
    lion = Animal("Барсик", "Лев", 5)
    elephant = Animal("Дамбо", "Слон", 10)
    snake = Animal("Каа", "Змея", 3)
    
    my_zoo.add_animal(lion)
    my_zoo.add_animal(elephant)
    my_zoo.add_animal(snake)
    
    # Показываем всех животных
    print("\n--- Информация о животных ---")
    my_zoo.show_animals()
    
    # Все животные издают звуки
    print("\n--- Звуки животных ---")
    my_zoo.make_all_sounds()
