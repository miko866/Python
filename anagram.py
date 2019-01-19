from collections import Counter

def is_anagram(str1, str2):
    return Counter(str1) == Counter(str2)

print(is_anagram('python', 'python'))
print(is_anagram('python', 'java'))
