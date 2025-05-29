class Pet:
    def __init__(self, name: str, animal_type: str):
        self.name = name
        self.animal_type = animal_type
        self.hunger = 0  # 0 = сытый, 10 = очень голодный
        self.energy = 10  # 10 = максимум энергии

    def feed(self):
        """Кормит питомца, уменьшая голод на 2 (но не меньше 0)."""
        self.hunger = max(0, self.hunger - 2)
        return self.hunger

    def play(self):
        """Играет с питомцем, увеличивая голод на 1 (но не больше 10)."""
        self.hunger = min(10, self.hunger + 1)
        return self.hunger

    def sleep(self):
        """Восстанавливает энергию до максимума."""
        self.energy = 10
        return self.energy

    def run(self):
        """Тратит 2 единицы энергии (но не меньше 0)."""
        self.energy = max(0, self.energy - 2)
        return self.energy

    def get_status(self):
        """Возвращает строку с текущим состоянием питомца."""
        return f"{self.animal_type.capitalize()} {self.name} (голод: {self.hunger}/10, энергия: {self.energy}/10)"


# Пример использования
pet = Pet("Барсик", "кот")
print(pet.get_status())  # Кот Барсик (голод: 0/10, энергия: 10/10)

pet.play()
pet.run()
print(pet.get_status())  # Кот Барсик (голод: 1/10, энергия: 8/10)

pet.feed()
pet.sleep()
print(pet.get_status())  # Кот Барсик (голод: 0/10, энергия: 10/10)
