def main():
    scores = []
    max = 0

    with open("english.csv", "r") as words:
        word = words.readline()
        while word:
            word = word.rstrip()
            difficulty = len(word)
            # Keep track of the maximum difficulty for this dataset
            if max < difficulty:
                max = difficulty

            scores.append((word, difficulty))
            word = words.readline();

    print("Max score is: " + str(max))

    with open("../data/difficulty.csv", "w") as diff:
        for tuple in scores:
            diff.write(", ".join([tuple[0], str(tuple[1] / max)]))
            diff.write("\n")

if __name__ == "__main__":
    main()
else:
    print("Not to be used as a module.")
