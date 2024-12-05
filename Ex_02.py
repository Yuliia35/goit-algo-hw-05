import re
from typing import Callable
def generator_numbers(text: str):
    pattern = re.compile(r'\b\d+(\.\d+)?\b')  # знайти усі збіги за шаблоном регулярного виразу
    numbers = pattern.finditer(text)
    for number in numbers:
        yield float(number.group()) # виводимо відповідне число як число з плаваючою точкою

def sum_profit(text: str, func: Callable) -> float:
    return sum(func(text)) # підсумовуємо числа


if __name__ == "__main__":
    #text = "Загальний дохід працівника складається з декількох частин: 1000.01 як основний дохід, доповнений додатковими надходженнями 27.45 і 324.00 доларів."
    text = "20.12 or 12.28 . 333.1  and 2.9  or 0.2 and 2 or4.4 end 5.5."
    total_income = sum_profit(text, generator_numbers)
    print(f"Загальний дохід: {total_income}")
