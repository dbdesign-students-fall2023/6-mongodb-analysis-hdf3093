import csv

input_csv_path = "data/listings.csv"

output_md_path = "README.md"

with open(input_csv_path, "rU") as csvfile:
    reader = csv.reader(csvfile)

    rows = [next(reader) for _ in range(3)]

with open(output_md_path, 'a') as mdfile:

    mdfile.write("| " + " | ".join(rows[0]) + " |\n")
    mdfile.write("|" + ":---:|" * len(rows[0]) + "\n")

    for row in rows[1:]:
        mdfile.write("| " + " | ".join(row) + " |\n")
