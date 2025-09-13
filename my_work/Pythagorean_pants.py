def Pythagorean_pants(numbers):
    numbers_ = sorted(numbers)
    if numbers_[0] ** 2 + numbers_[1] ** 2 == numbers_[2] ** 2 :
        return True
    else:
        return False
print(Pythagorean_pants([5, 3, 4]))
print(Pythagorean_pants([6, 8, 10]))   
print(Pythagorean_pants([100, 3, 65]))   

__version__ = '1.0'
