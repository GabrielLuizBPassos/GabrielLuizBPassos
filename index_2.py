with open("index.py") as f:
    for line in f:
        if not line.isspace() or "# " in line:
            print(len(f.readline()))