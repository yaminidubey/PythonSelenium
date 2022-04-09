with open('test.txt','r') as file:
    content = file.readlines()
    reversed(content)
    with open('test.txt', 'w') as file1:
        for line in reversed(content):
            file1.write(line)