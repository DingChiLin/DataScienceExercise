import sys
import json

def hw(sent_file,tweet_file):

    scores = {} # initialize an empty dictionary
    for line in sent_file:
        term, score  = line.split("\t")  # The file is tab-delimited. "\t" means "tab character"
        scores[term] = int(score)  # Convert the score to an integer.

    tweet_scores = []
    for line in tweet_file:
        tweet = json.loads(line)
        line_content = tweet.get("text")

        score = 0
        if line_content != None:
           words = line_content.split(" ")
           for word in words:
               value = scores.get(word)
               if value != None:
                  score += value

        tweet_scores.append(score)
        if score > 10:
            print line_content.encode('utf-8')
        elif score < -10:
            print line_content.encode('utf-8')

    print('\t'.join(map(str, tweet_scores)))

def lines(fp):
    print "line: " + str(len(fp.readlines()))

def main():
    sent_file = open(sys.argv[1])
    tweet_file = open(sys.argv[2])
    hw(sent_file,tweet_file)
    lines(sent_file)
    lines(tweet_file)

if __name__ == '__main__':
    main()
