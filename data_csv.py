import csv

def read(name_csv):
    data = []

    with open(f'csv/{name_csv}.csv', newline='', encoding='utf-8') as csvfile:
        reader = csv.reader(csvfile)

        # Suppresion de la premiere ligne du csv
        next(reader)

        for row in reader:
            if row and float(row[1]) > 0:
                data.append((row[0], float(row[1]), row[2].strip('%')))
    return data
