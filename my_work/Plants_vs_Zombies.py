def plants_vs_zombies(list1 = 0, list2 = 0):
    # Створюю документацію
    """Функція plants_vs_zombies рийматє два масиви несортованих чисел (перший - масив рослин, що 
    захищається, другий - атакуючий масив зомбі) і поверне boolean значення в залежність від того
      чи перемогли захисники. """
    
    # Перевірка помилок
    if list1 == 0 or list2 == 0:
        return "Ви забули ввести параметр"
    
    if  not(isinstance(list1, list) and isinstance(list2, list)):
        return "Перевірте, будь ласка, тип даних параметрів!"
    
    for i in list1:
        if not isinstance(i, int):
            return "Перевірте тип даних в членах списків"
    for i in list2:
        if not isinstance(i, int):
            return "Перевірте тип даних в членах списків"
    
    

    # Створюю змінні для роботи функції
    plants = 0
    zombies = 0
    list1 = list1
    list2 = list2

    # Підготовлюю списки
    while len(list1) != len(list2):
        if len(list1) > len(list2):
            list2.append(0)
        else:
            list1.append(0) 

    # Проводжу бій
    for i in range(len(list1)):
        if list1[i] > list2[i]:
            zombies += 1
        elif list1[i] < list2[i]:
            plants += 1

    # Підведення пісумків
    if zombies < plants:
        return True
    elif zombies > plants:
        return False
    else:
        zombies_initial_strength = 0
        for i in list1:
            zombies_initial_strength += i
        plants_initial_strength = 0
        for i in list2:
            plants_initial_strength += i
        return plants_initial_strength >= zombies_initial_strength

# Перевірка

print(plants_vs_zombies([ 1, 3, 5, 7 ]))
print(plants_vs_zombies([ 1, 3, 5, 7 ], "qq"))
print(plants_vs_zombies([ 1, 3, 5, 7 ], [ 2, 4, "qq", 8 ]))
print(plants_vs_zombies([ 2, 1, 1, 1 ], [ 1, 2, 1, 1 ]))
print(plants_vs_zombies.__doc__)
#zombies=[ 1, 3, 5, 7 ] plants=[ 2, 4, 6, 8 ] -> True
#zombies=[ 1, 3, 5, 7 ] plants=[ 2, 4 ] -> False
#zombies=[ 1, 3, 5, 7 ] plants=[ 2, 4, 0, 8 ] -> True
#zombies=[ 2, 1, 1, 1 ] plants=[ 1, 2, 1, 1 ] -> True
__version__ = "1.0"   