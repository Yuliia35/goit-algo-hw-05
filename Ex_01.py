def caching_fibonacci ():
    cache = {} # цей словник зберігатиме числа Фібоначчі
    def fibonacci (n):
        if n in cache: #визначаю чи є число Фібоначчі в кеші
            return cache[n]
        if n <= 0:
            return 0
        elif n == 1:
            return 1
        result = fibonacci(n - 1) + fibonacci(n - 2) #рекурсивно обчислюю число Фібоначчі
        cache[n] = result #і зберігаю у кеші
        return result
    return fibonacci

# Отримуємо функцію fibonacci
fib = caching_fibonacci()

# Використовуємо функцію fibonacci для обчислення чисел Фібоначчі
print(fib(10))  # Виведе 55
print(fib(15))  # Виведе 610
print(fib(20))
print(fib(30))


         

