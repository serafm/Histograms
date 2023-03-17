import csv

global incomeList, equiwidthBins, equidepthBins, min_income, max_income


class Histogram:
    global incomeList, equiwidthBins, equidepthBins, min_income, max_income
    # List of Income attribute
    incomeList = list()
    # Bins as dictionaries
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
        # Sort income list
        incomeList = sorted(incomeList)
        # Minimum income
        min_income = min(incomeList)
        # Maximum income
        max_income = max(incomeList)

    # Create an equi-width histogram
    def equiwidth(self):
        global incomeList, equiwidthBins, min_income, max_income
        # Keep a pointer to continue from where the list stops to add in a bin the values
        # (so there no need to start over from the beginning of the list)
        pointer = 0
        min = min_income
        # The width for exact distribution of the values into the bins
        width = (max_income - min_income) / 100
        for i in range(100):
            # Range of every bin
            bin_range = [round(min, 2), round(min + width, 2)]
            bin_range = str(bin_range).replace(']', ')')
            # Initialize the dictionary
            equiwidthBins[bin_range] = []
            # Add income values into the right bins
            for income in range(pointer, len(incomeList)):
                if min <= incomeList[income] < min + width:
                    equiwidthBins[bin_range].append(incomeList[income])
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
            bin_range = [incomeList[start], incomeList[stop]]
            bin_range = str(bin_range).replace(']', ')')
            equidepthBins[bin_range] = incomeList[start:stop]
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


csv_path = input("Please enter csv file path: ")
csv_attribute = input("Please enter attribute: ")
histogram = Histogram(csv_path, csv_attribute)
histogram.read_income_data()
histogram.equiwidth()
histogram.equidepth()
histogram.print()