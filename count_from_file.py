def count_words(file_name):
    num_words = 0
    num_chars = 0
    num_lines = 0

    with open(file_name, 'r') as file:
        for line in file:
            word_list = line.split()
            num_lines += 1
            num_words += len(word_list)
            num_chars += len(line)
    
    print("Words: ", num_words)
    print("Lines: ", num_lines)
    print("Characters: ", num_chars)

count_words('test.txt') # source file here!