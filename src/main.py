import csv

from settings import Settings


def import_csv_as_tuples(csv_file):
    with open(csv_file, mode='r', newline='') as file:
        csv_reader = csv.reader(file)
        data = [tuple(row) for row in csv_reader]
    return data


def main():
    settings = Settings()
    samples = import_csv_as_tuples("../samples.csv")
    print(samples)


if __name__ == "__main__":
    main()
