from collections import Counter
import string
file = 'Desktop/finalhomework/7/Lab7/input_7_2.txt' 
with open(file, 'r') as file:
    text = file.read()
counter = Counter({char: 0 for char in string.ascii_uppercase})
for char in text.upper():
    if char in counter:
        counter[char] += 1
sorted = sorted(counter.items(), key=lambda x: x[1], reverse=True)
alphabets = [char for char, count in sorted if count > 0]
print(alphabets)

