import csv

global incomeList, equiwidthBins, equidepthBins, min_income, max_income


class Histogram:
    global incomeList, equiwidthBins, equidepthBins, min_income, max_income
    # List of Income attribute
    incomeList = list()
    # Bins as dictionary
    equiwidthBins = dict()
    equidepthBins = dict()

    def __init__(self, path, attribute):
        self.path = path
        self.attribute = attribute

    # Read csv file Income data, add them into a list
    def read_income_data(self):
        global incomeList, min_income, max_income
        with open(self.path, newline='') as csvfile:
            data = list(csv.reader(csvfile))
            self.attribute = data[0].index(self.attribute)
            for income in range(1, len(data)):
                # if the field is empty don't add it in list
                if data[income][self.attribute] == '':
                    continue
                else:
                    incomeList.append(float(data[income][self.attribute]))
        incomeList = sorted(incomeList)
        # Minimum income
        min_income = min(incomeList)
        # Maximum income
        max_income = max(incomeList)

    # Create an equi-width histogram
    def equiwidth(self):
        global incomeList, equiwidthBins, min_income, max_income
        pointer = 0
        min = min_income
        # The width for exact distribution of the values into the bins
        width = (max_income - min_income) / 100
        for i in range(100):
            # Range of every bin
            b = [round(min, 2), round(min + width, 2)]
            b = str(b).replace(']', ')')
            # Initialize the dictionary
            equiwidthBins[b] = []
            # Split income values into the right bins
            for income in range(pointer, len(incomeList)):
                if min <= incomeList[income] < min + width:
                    equiwidthBins[b].append(incomeList[income])
                else:
                    pointer = income
                    break
            # Update the value of min
            min = round(min + width, 2)

    def equidepth(self):
        global incomeList, equidepthBins
        start = 0
        pointer = int((len(incomeList) / 100))
        stop = pointer
        for i in range(100):
            b = [incomeList[start], incomeList[stop]]
            b = str(b).replace(']', ')')
            equidepthBins[b] = incomeList[start:stop]
            start = stop
            stop += pointer

    def print(self):
        global min_income, max_income, incomeList, equiwidthBins, equidepthBins
        print(len(incomeList), ' valid income values')
        print("minimum income = ", min_income)
        print("maximum income = ", max_income)
        print("equiwidth:")
        for key in equiwidthBins:
            print("range: ", key, ", numtuples: ", len(equiwidthBins[key]))
        print("equidepth: ")
        for key in equidepthBins:
            print("range: ", key, ", numtuples: ", len(equidepthBins[key]))


path = input("Please enter csv file path: ")
attribute = input("Please enter attribute: ")
histogram = Histogram(path, attribute)
histogram.read_income_data()
histogram.equiwidth()
histogram.equidepth()
histogram.print()
