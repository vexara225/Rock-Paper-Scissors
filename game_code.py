import random

stone = "камень"
paper = "бумага"
scissors = "ножницы"


user = input("Выбери: камень, ножницы, бумага (с маленькой буквы) - ")
if stone == user or paper == user or scissors == user:
    print("Ваш выбор принят!")
else:
    print("вы ввели не то, что нужно!!!")

choice = [stone, scissors, paper]
computer = random.choice(choice)

# первое условие
if user == computer:
    print("⚠️ Нечья. ответы совпали")

# второе условие
elif computer == stone and user == paper:
    print(f"✅ Поздравляем, {paper} побеждает {stone}. Вы выиграли!") # бумага побеждает камень
elif computer == paper and user == stone:
    print(f"❌ Вы проиграли {paper} побеждает {stone}. Не растраивайтесь.")

# третье условие
elif computer == paper and user == scissors:
    print(f"✅ Поздравляем, {scissors} побеждает {paper}. Вы выиграли!") # ножницы побеждают бумагу
elif computer == scissors and user == paper:
    print(f"❌ Вы проиграли {scissors} побеждает {paper}. Не растраивайтесь.")

#четвёртое условие
elif computer == scissors and user == stone:
    print(f"✅ Поздравляем, {stone} побеждает {scissors}. Вы выиграли!") # камень побеждает ножницы
elif computer == stone and user == scissors:
    print(f"❌ Вы проиграли. {stone} побеждает {scissors}. Не растраивайтесь.")


print("Спасибо за игру!!!❤️")