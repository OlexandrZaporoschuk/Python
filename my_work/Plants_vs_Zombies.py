import logging

logger = logging.getLogger(f"{__name__}")
logger.setLevel(logging.INFO)


formatter = logging.Formatter('%(asctime)s - %(levelname)s - %(message)s')
stream_handler = logging.StreamHandler()
stream_handler.setFormatter(formatter)
logger.addHandler(stream_handler)

def plants_vs_zombies(list1 = 0, list2 = 0):
    # Створюю документацію
    """Функція plants_vs_zombies рийматє два масиви несортованих чисел (перший - масив рослин, що 
    захищається, другий - атакуючий масив зомбі) і поверне boolean значення в залежність від того
      чи перемогли захисники. """
    logger.info(f"Start {list1}, {list2}")
    # Перевірка помилок
    if list1 == 0 or list2 == 0:
        logger.error("Ви забули ввести параметр")
        return
    
    if  not(isinstance(list1, list) and isinstance(list2, list)):
        logger.error("Перевірте, будь ласка, тип даних параметрів!")
        return 
    
    for i in list1:
        if not isinstance(i, int):
            logger.error("Перевірте тип даних в членах списків")
            return
    for i in list2:
        if not isinstance(i, int):
            logger.error("Перевірте тип даних в членах списків")
            return
    
    

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
    logger.info(f"Підготовлені списки: {list1}, {list2}")
    # Проводжу бій
    for i in range(len(list1)):
        if list1[i] > list2[i]:
            zombies += 1
        elif list1[i] < list2[i]:
            plants += 1

    # Підведення пісумків
    if zombies < plants:
        print(True)
    elif zombies > plants:
        print(False)
    else:
        zombies_initial_strength = 0
        for i in list1:
            zombies_initial_strength += i
        plants_initial_strength = 0
        for i in list2:
            plants_initial_strength += i
        print(plants_initial_strength >= zombies_initial_strength)
    logger.info(f"The end {zombies}, {plants}")

# Перевірка
if __name__ == "__main__":
    print(plants_vs_zombies.__doc__)
    plants_vs_zombies([ 1, 3, 5, 7 ])
    plants_vs_zombies([ 1, 3, 5, 7 ], "qq")
    plants_vs_zombies([ 1, 3, 5, 7 ], [ 2, 4, "qq", 8 ])
    plants_vs_zombies([ 2, 1, 1, 1 ], [ 1, 2, 1, 1 ])

#zombies=[ 1, 3, 5, 7 ] plants=[ 2, 4, 6, 8 ] -> True
#zombies=[ 1, 3, 5, 7 ] plants=[ 2, 4 ] -> False
#zombies=[ 1, 3, 5, 7 ] plants=[ 2, 4, 0, 8 ] -> True
#zombies=[ 2, 1, 1, 1 ] plants=[ 1, 2, 1, 1 ] -> True
__version__ = "1.0"   