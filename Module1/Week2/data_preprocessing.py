#Open file
import re
from collections import Counter
# Using r"" to automatically handle blackflash
file_name = r"C:\Users\PC\Desktop\AIO-Exercises\Module1\Week2\P1_data.txt"
def read_data(file_name):
    with open(file_name, 'r') as file:
        data = file.read()
        file.close()
    return data.split(',')

data = read_data(file_name)
# Process each line in the list
for line in data:
    line = line.lower()
    line = re.sub(r'[^\w\s]', '', line)
    #Split into words
    words = line.split()
    
# Count the occurrences of each word
word_count = {word: count for word, count in Counter(words).items()}
"""for word in words:
    if word in word_count:
        word_count[word] += 1
    else:
        word_count[word] = 1"""
print(word_count)
