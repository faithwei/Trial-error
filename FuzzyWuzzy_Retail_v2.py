from fuzzywuzzy import process
import csv

save_file = open('FuzzyResults3.csv', 'w')
writer = csv.writer(save_file, lineterminator = '\n')

def parse_csv(path):

    with open(path,'r') as f:
        reader = csv.reader(f, delimiter=',')
        for row in reader:
            yield row


if __name__ == "__main__":
    ## Create lookup dictionary by parsing the products csv
    data = {}
    for row in parse_csv('reported.csv'):
        data[row[0]] = row[0]

    ## For each row in the lookup compute the partial ratio
    for row in parse_csv("retail.csv"):
        #print(process.extract(row,data, limit = 100))
        for found, score, matchrow in process.extract(row, data, limit=100):
            if score >= 60:
                print('%d%% partial match: "%s" with "%s" ' % (score, row, found))
                Digi_Results = [score, row, found]
                writer.writerow(Digi_Results)


save_file.close()