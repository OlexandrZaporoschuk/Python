import datetime
import inspect
import logging

logger = logging.getLogger(f"{__name__}")
logger.setLevel(logging.INFO)


formatter = logging.Formatter('%(asctime)s - %(levelname)s - %(message)s')
stream_handler = logging.StreamHandler()
stream_handler.setFormatter(formatter)
logger.addHandler(stream_handler)


def employee_WSG(days: int, work_days: int, rest_days: int, start_date: datetime.datetime):
    """ Функція employee_WSG  - функція, яка генерує розклад робочих днів працівника, вона приймає 
    кількість днів, на які потрібно скласти розклад, кількість днів роботи, кількість днів відпочинку
      та дату початку розкладу. """
    logger.info(f"Start : {start_date}")
    # Робота над помилками
    if not(isinstance(days, int) and isinstance(work_days, int) and isinstance(rest_days, int) and inspect.isclass(datetime.datetime)):
        logger.error(f"Перевірьте, будь ласка типи параметрів, що ви ввели!:{days}- day, {work_days} - work days, {rest_days} - rest days, {start_date}")
        return

    schedule = []
    current_date = start_date
    total_days_added = 0

    while len(schedule) < days:
        # Додаємо робочі дні
        for _ in range(work_days):
            if len(schedule) >= days:
                break
            schedule.append(current_date)
            current_date += datetime.timedelta(days=1)
            total_days_added += 1
        
        # Пропускаємо дні відпочинку
        current_date += datetime.timedelta(days=rest_days)
        total_days_added += rest_days
    logger.info(f"The and: {schedule}")
    print(schedule)
# Перевіряємо

if __name__ == "__main__":
    print(employee_WSG.__doc__)
    employee_WSG(5, 2, 1, datetime.datetime(2020, 1, 30))
    employee_WSG("eee", 2, 1, datetime.datetime(2020, 1, 30))
    

__version__ = "1.0" 
#days: 5, work_days: 2, rest_days: 1, start_date: datetime(2020, 1, 30)