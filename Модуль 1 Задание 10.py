text = input().lower()
words = text.split()
counts = {}
for word in words:
    if word not in counts:
        counts[word] = 0
    counts[word] += 1

most_common_word = max(counts, key=counts.get)
most_common_count = counts[most_common_word]

print(f"{most_common_word} {most_common_count}")