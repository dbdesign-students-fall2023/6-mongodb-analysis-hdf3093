import csv
reader = csv.reader(open("data/listings.csv", "r"), delimiter=',')
writer = csv.writer(open("data/markdown.csv", 'w'), delimiter='|')
writer.writerows(reader)