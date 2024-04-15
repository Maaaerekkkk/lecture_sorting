import os
import csv

def read_data(file_name):
    """
    Reads csv file and returns numeric data.

    :param file_name: (str), name of CSV file
    :return: (dict), dictionary with numeric data, keys - csv column names, values - numbers in each column
    """
    cwd_path = os.getcwd()
    file_path = os.path.join(cwd_path, file_name)
    with open(file_path, mode="r") as file:
        reader = csv.DictReader(file)
        data = {}
        iter = 0
        for row in reader:
            for key, value in row.items():
                if iter == 0:
                    data[key] = [int(value)]
                else:
                    data[key].append(int(value))
            iter = iter + 1
    return data

def selection_sort(zoznam, order):
    for i in range(len(zoznam)):
        idx = i
        for j in range(i + 1, (len(zoznam))):
            if 'ascending' in order:
                if zoznam[j] < zoznam[idx]:
                    idx = j
            elif 'descending' in order:
                if zoznam[j] > zoznam[idx]:
                    idx = j

        zoznam[i], zoznam[idx] = zoznam[idx], zoznam[i]
    return zoznam

def bubble_sort(zoznam):
    for i in range(len(zoznam) - 1):
        for j in range(len(zoznam) - i - 1):
            if zoznam[j] > zoznam[j + 1]:
                zoznam[j], zoznam[j + 1] = zoznam[j + 1], zoznam[j]
    return zoznam

def insertion_sort(zoznam):
    for i in range(1, len(zoznam)):
        number = zoznam[i]
        j = i - 1
        while j >= 0 and zoznam[j] > number:
            zoznam[j + 1] = zoznam[j]
            j = j - 1
        zoznam[j + 1] = number
    return zoznam

def main():
    pass


if __name__ == '__main__':
    data = read_data('numbers.csv')
    upratane = insertion_sort(data['series_1'])
    print(data)
    print(upratane)
    main()
