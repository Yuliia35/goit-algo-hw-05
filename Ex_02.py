import re
from typing import Callable
def generator_numbers(text: str):
    numbers = map(float, filter(lambda x: re.match(r"\d+[\.,]{0,1}\d+.", x), text.split(" ")))  # знайти усі збіги за шаблоном регулярного виразу
    
    for number in numbers:
        yield number # виводимо відповідне число як число з плаваючою точкою

def sum_profit(text: str, func: Callable) -> float:
    return sum(func(text))


if __name__ == "__main__":
    text = "Загальний дохід працівника складається з декількох частин: 1000.01 як основний дохід, доповнений додатковими надходженнями 27.45 і 324.00 доларів."
    total_income = sum_profit(text, generator_numbers)
    print(f"Загальний дохід: {total_income}")