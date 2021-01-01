def main():
    scores = {}
    max = 0

    with open("../data/men.csv", "r") as men:
        line = men.readline()
        while line:
            tokens = line.split(", ")[:-1]
            for token in tokens:
                difficulty = len(token)
                # Keep track of the maximum difficulty for this dataset
                if max < difficulty:
                    max = difficulty

                scores[token] = difficulty / max


            line = men.readline();

    with open("../data/difficulty.csv", "w") as diff:
        for tuple in list(scores.items()):
            line = [str(i) for i in tuple]

            diff.write(", ".join(line))
            diff.write("\n")

if __name__ == "__main__":
    main()
else:
    print("Not to be used as a module.")
