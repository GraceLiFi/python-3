import re
def create_files(input):
    short = []
    long = []
    with open(input, "r") as file1:
        for line in file1:
            if not line:
                break

            #removePunct = re.sub(r'[.,!?]', '', line.lower())
            for word in line.split():
                if len(word) >= 3:
                    long.append(word)
                else:
                    short.append(word)
    short = set(short)
    long = set(long)
    count = len(short) + len(long)
    with open("small-words.txt", "w") as file2:
        for line in short:
            file2.writelines(line + "\n")

    with open("large-words.txt", "w") as file3:
        for line in long:
            file3.writelines(line + "\n")

    return count
def ex3():
    total_words = create_files("C:\\Users\\f9hud0c\\tedprojects\\python-3\\files\\words.txt")
    print(f"Total words: {total_words}.")

ex3()