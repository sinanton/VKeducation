def process_string(input_str):
    """
    Функция, которая принимает строку, обрабатывает ее в соответствии с условиями
    и возвращает обработанную строку.
    """
    processed_chars = []
    for char in input_str:
        if char not in "!@#%":
            if input_str[0] == "!":
                processed_chars.append(char.upper())
            else:
                processed_chars.append(char.lower())
    return "".join(processed_chars)

# Чтение и обработка входных данных
while True:
    input_str = input()
    if not input_str:
        break
    print(process_string(input_str))