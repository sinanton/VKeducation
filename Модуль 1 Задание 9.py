string = input().lower()
unique_chars = sorted(set(string.replace(" ", "")))
print(" ".join(unique_chars))