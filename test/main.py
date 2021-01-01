import gensim.downloader as api
import math

NOW_PROCESSING = "Now processing ({0}, {1})"
FOUND_MATCH = "Found a match in MEN database for ({0}, {1})!"
MEN_DISTANCE = "Distance from word2vec and MEN: {0}"
DONE = "Final score: {0}"

FOUND_CORRELATION = "Target word ({0}) has a difficulty rating!"
CORRELATION = "Spearman correlation for this dataset is: {0}"

def main():
    # Load our models.
    wv = api.load("word2vec-google-news-300")
    men = tupleize("data/men.csv")

    # First, extract our target - response pairs
    input = tupleize("input.csv")

    # Of course we are also going to need some "difficulty" metric
    difficulty = dict(tupleize("data/difficulty.csv"))
    # This will contain tuples with the target word, its difficulty
    # and the final score (relative to the response word)
    correlation = []

    # Then, get similarity estimates from our models
    with open("output.csv", "w") as output:
        for target, response in input:
            print(NOW_PROCESSING.format(target, response));
            wvScore = wv.similarity(target, response)

            # If available, extract similarity estimate
            # from MAN as well...
            match = [score for score in men if (target in score
                                            and response in score)]

            if len(match) > 0:
                # If found normalize it...
                print(FOUND_MATCH.format(target, response))
                menScore = float(match[0][2]) / 100.0
                # ...find the vector distance from the two models...
                distance = abs(menScore - wvScore)
                print(MEN_DISTANCE.format(distance))
                # ...and get a final value as the mean of the two scores
                meanScore = mean([wvScore, menScore])
            else:
                # Too bad, can't do anything about it...
                meanScore = wvScore

            print(DONE.format(meanScore));
            # Write our results in output.csv
            output.write(", ".join([target, response, str(meanScore)]))
            output.write("\n")

            # Now working on our correlation coefficient
            #
            # First, we need to calculate rankings for the scores.
            # Of course this can only be done for words that have BOTH
            # a difficulty score AND a match score (which will naturally
            # depend on the word it's matched with, the response)
            #
            # Let us work on the target words and use the following strategy

            if target in difficulty:
                print(FOUND_CORRELATION.format(target), end="\n\n")
                tuple = (target, float(difficulty[target]), meanScore)
                correlation.append(tuple)

    covariance = cov([(i[1], i[2]) for i in correlation])
    xVariance = var([i[1] for i in correlation])
    yVariance = var([i[2] for i in correlation])

    spearman = covariance / math.sqrt(xVariance * yVariance)
    print(CORRELATION.format(spearman))

def var(values):
    return cov([(i, i) for i in values])

def cov(pairs):
    length = len(pairs)

    xMean = mean([i[0] for i in pairs])
    yMean = mean([i[1] for i in pairs])

    sum = 0
    for pair in pairs:
        sum += (pair[0] - xMean) * (pair[1] - yMean)

    sum /= (length - 1)
    return sum

def mean(values):
    sum = 0
    for value in values:
        sum += value

    return (sum / len(values))

def tupleize(file):
    output = []
    with open(file, "r") as input:
        line = input.readline()
        while line:
            nuple = tuple(line.rstrip().split(", "))
            output.append(nuple)
            line = input.readline();

    return output

if __name__ == "__main__":
    main()
else:
    print("Please run as main.")
