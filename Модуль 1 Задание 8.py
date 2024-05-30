n = int(input())
max_values = []
for _ in range(n):
    sequence = input().split()
    max_value = max(map(int, sequence))
    max_values.append(max_value)

max_values.sort(reverse=True)
result = ";".join(map(str, max_values))
print(result)