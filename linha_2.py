
char = 0

with open("teste.py") as f:
    # print(len(f.readlines()))
    for line in f:
        if line.isspace() is False:
            if len(line.strip()) > 0:
                char += 1
    print(f"Total lines: {char}")
