def Pythagorean_pants(numbers = 0):
    """Функція Pythagorean_pants, приймає масив несортованих чисел і повертає boolean значення залежно від того, 
    чи можна із заданих значень скласти піфагорів трикутник з відповідними довжинами сторін."""
    try:
        numbers_ = sorted(numbers)
    except TypeError :
        if numbers == 0 :
            return "Ви забули ввести параметр"
        print("Перевірте, будь ласка, тип даних параметра!")
        return "Ви ввели", numbers, type(numbers)
   
    if numbers_[0] ** 2 + numbers_[1] ** 2 == numbers_[2] ** 2 :
        return True
    else:
        return False
print(Pythagorean_pants(["ііі", 3, 4]))
print(Pythagorean_pants([6, 8, 10]))   
print(Pythagorean_pants([100, 3, 65]))   
  
__version__ = '1.0'