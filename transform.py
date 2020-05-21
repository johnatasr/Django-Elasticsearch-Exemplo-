import csv, json, os

import pandas as pd

csvFilePath = "datasets/udemy_courses.csv"
jsonFilePath = "data_transformed/udemy.json"

def trasn():

    arr = []
    # read the csv and add the arr to a arrayn

    with open(csvFilePath, encoding='utf-8') as csvFile:
        csvReader = csv.DictReader(csvFile)
        print(csvReader)
        for csvRow in csvReader:
            arr.append(csvRow)

    id_model = 1

    #Transform in Django Model to migrate
    final_arr = []
    for row in arr:
        dic = {}
        dic['model'] = 'courses.course'
        dic['pk'] = id_model
        dic['fields'] = row
        final_arr.append(dic)
        id_model = id_model + 1

    # write the data to a json file
    with open(jsonFilePath, "w") as jsonFile:
        jsonFile.write(json.dumps(final_arr, indent=4))

def transform():
    csvFilePath = "datasets/udemy_courses.csv"
    jsonFilePath = "data_transformed/udemy.json"
    df = pd.read_csv(csvFilePath)
    df.to_json(jsonFilePath)

if __name__ == "__main__":
    trasn()
