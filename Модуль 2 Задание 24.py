def cache_deco(func):
    cache = {}

    def wrapper(*args):
        args_tuple = tuple(args)
        if args_tuple not in cache:
            cache[args_tuple] = func(*args)
        return cache[args_tuple]

    return wrapper

def solution(func_map, func_filter, data):
    filtered_data = filter(func_filter, data)
    mapped_data = map(func_map, filtered_data)
    for i, value in enumerate(mapped_data, start=1):
        if i % 2 == 1:
            yield value

code = []
while data := input():
    code.append(data)
code = "\n".join(code)
exec(code)