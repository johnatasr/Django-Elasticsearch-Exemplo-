import csv, json, os

import pandas as pd


def transform():
    csvFilePath = "datasets/udemy_courses.csv"
    jsonFilePath = "data_transformed/udemy.json"

    data = {}

    # list_csvs = [ csv_u for csv_u in csvFilePath ]

    # with open(csvFilePath) as csvFile:
    #     csvReader = csv.DictReader(csvFile)
    #     for rows in csvReader:
    #         id = rows['course_id']
    #         data['id'] = rows
    #
    # with open(jsonFilePath, 'w') as jsonFile:
    #     jsonFile.write(json.dumps(data, indent=4))

    df = pd.read_csv(csvFilePath)
    df.to_json(jsonFilePath)

if __name__ == "__main__":
    transform()
