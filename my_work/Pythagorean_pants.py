import logging

logger = logging.getLogger(f"{__name__}")
logger.setLevel(logging.INFO)
formatter = logging.Formatter('%(asctime)s - %(levelname)s - %(message)s')
stream_handler = logging.StreamHandler()
stream_handler.setFormatter(formatter)
logger.addHandler(stream_handler)

def Pythagorean_pants(numbers: list):
    """Функція Pythagorean_pants, приймає масив несортованих чисел і повертає boolean значення залежно від того, 
    чи можна із заданих значень скласти піфагорів трикутник з відповідними довжинами сторін."""
    logger.info(f"Start {numbers}")
    logger.debug(f"Функцыя отримала: {numbers}")
    try:
        numbers_ = sorted(numbers)
    except TypeError :
        logger.error(f"Перевірте, будь ласка, тип даних параметра!, {numbers}")
        return
   
    if numbers_[0] ** 2 + numbers_[1] ** 2 == numbers_[2] ** 2 :
        print(True)
    else:
        print(False)
    logger.info(f"The and {[(numbers_[0] ** 2 + numbers_[1] ** 2), (numbers_[2] ** 2)]}")

if __name__ == "__main__":
    print(Pythagorean_pants.__doc__)
    Pythagorean_pants(["ііі", 3, 4])
    Pythagorean_pants([6, 8, 10])  
    Pythagorean_pants([100, 3, 65])  
    

  
__version__ = '1.0'