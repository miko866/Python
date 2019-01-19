
# Python app to remove punctuation from a string

punctuation = '''!()-[]{};'":/\,<>.?@#$%^&*_~'''

my_str = input("Enter text: ")

# remove punctuation from the string
no_punct = ""
for char in my_str:
        if char not in punctuation:
        no_punct += char
print(no_punct)

