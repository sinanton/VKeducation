input_str = input()
words = input_str.split()
average_length = sum(len(word) for word in words) / len(words)
print("{:.2f}".format(average_length))