class Tobacco:
    def __init__(self, tobacco_brand, tobacco_flavor, tobbacco_strength, tobacco_pot):
        self.brand = tobacco_brand
        self.flavor = tobacco_flavor
        self.strength = tobbacco_strength
        self.pot = tobacco_pot

    def smoke(self):
        return f"I smoked tobacco {self.brand}"

# Задание:
# Используя tobacco_mixes.py реализовать:
# Класс табака
#   Метод смешивания табака.
#   * Реализовать смешивание табака с помощью оператора +
# Класс табачного микса
#   Ингридиенты
#   Рейтинг
#   Вывод рецепта
