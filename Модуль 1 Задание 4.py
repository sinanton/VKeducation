input_str = input()
if 'a' in input_str or 'o' in input_str:
    if 'i' not in input_str and 'e' not in input_str:
        print(True)
    else:
        print(False)
else:
    print(False)