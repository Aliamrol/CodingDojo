def readFile(file_name, char_to_count):
    with open(file_name, 'r') as file:
        content = file.read()
        char_count = 0
        for i in content:
            if i == char_to_count:
                char_count += 1
        print(char_count)


readFile("Text.txt", "a")
