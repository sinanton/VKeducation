# Словарь для кэширования вычислений
fib_cache = {}

def fibonacci(n):
    """
    Рекурсивная функция для вычисления n-го числа Фибоначчи.
    """
    # Проверяем, есть ли значение в кэше
    if n in fib_cache:
        return fib_cache[n]
    
    # Базовые случаи
    if n == 1 or n == 2:
        return 1
    
    # Рекурсивное вычисление
    result = fibonacci(n-1) + fibonacci(n-2)
    
    # Кэшируем результат
    fib_cache[n] = result
    
    return result

# Чтение ввода и вывод результата
n = int(input())
print(fibonacci(n))