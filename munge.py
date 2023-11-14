import csv
with open('data/listings.csv', 'r', encoding='utf-8') as csvfile:
    reader = csv.DictReader(csvfile)
    rows = list(reader)

#removing unnecessary / blank columns
drop_columns = [ 'neighborhood_overview', 'host_about', 'host_response_time', 'host_response_rate', 'host_acceptance_rate',  'neighbourhood_group_cleansed','license', 'calendar_updated']

cleaned_rows = []
for row in rows:
    cleaned_row = {}
    for key, value in row.items():
        if key not in drop_columns and value is not None:
            cleaned_row[key] = value
    if len(cleaned_row) == len(row) - len(drop_columns):
        cleaned_rows.append(cleaned_row)

with open('data/listings_clean.csv', 'w', newline='', encoding='utf-8') as csvfile:
    fieldnames = cleaned_rows[0].keys()
    writer = csv.DictWriter(csvfile, fieldnames=fieldnames)

    writer.writeheader()
    writer.writerows(cleaned_rows)


