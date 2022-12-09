def linha():
    with open("index.py") as f:
        # print(len(f.readlines()))
        for line in f:
            if line.isspace() == False:
                line.strip()
                print(line)


linha()
