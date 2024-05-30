def average_val(s):
    arr = list(map(int, s.split()))
    return sum(arr) / len(arr)
 
print(*map(average_val, iter(input, '')), sep='\n')