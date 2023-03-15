import csv

from rdflib import Graph, URIRef, BNode, Literal


def load_csv_file_as_object(file_path: str):
    result = []
    with open(file_path, "r") as stream:
        reader = csv.reader(stream)
        header = next(reader)  # Skip header
        for line in reader:
            result.append({key: value for key, value in zip(header, line)})
    return result


def main():
    file_path = "../../../example.csv"
    data = load_csv_file_as_object(file_path)
    print(data)


if __name__ == "__main__":
    main()
