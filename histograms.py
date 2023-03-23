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
            bin_range = (round(min, 2), round(min + width, 2))
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

    # Create an equi-depth histogram
    def equidepth(self):
        global incomeList, equidepthBins
        start = 0
        pointer = int((len(incomeList) / 100))
        stop = pointer
        for i in range(100):
            bin_range = (incomeList[start], incomeList[stop])
            equidepthBins[bin_range] = incomeList[start:stop]
            start = stop
            stop += pointer

    # Calculate the actula result of a query
    def actual_result(self, a, b):
        global incomeList
        result = 0
        for income in incomeList:
            if float(a) <= income < float(b):
                result += 1
        return result

    # Calculate the estimated result using equiwidth of a query
    def equiwidth_estimated_result(self, a, b):
        global equiwidthBins
        estimated_result = 0
        a = float(a)
        b = float(b)
        for bin in equiwidthBins:
            range_difference = bin[1] - bin[0]
            numtuples = len(equiwidthBins[bin])
            if bin[0] <= a < bin[1] and bin[0] < b <= bin[1]:
                ab_difference = b - a
                percentage = ab_difference/range_difference
                estimated_result += (percentage*numtuples)
            elif bin[0] <= a < bin[1]:
                a_bin_difference = bin[1] - a
                percentage = a_bin_difference/range_difference
                estimated_result += (percentage*numtuples)
            elif bin[0] <= b < bin[1]:
                b_bin_difference = b - bin[0]
                percentage = b_bin_difference/range_difference
                estimated_result += (percentage*numtuples)
            elif bin[0] > float(a) and bin[1] < float(b):
                estimated_result += numtuples
        return estimated_result

    # Calculate the estimated result using equidepth of a query
    def equidepth_estimated_result(self, a, b):
        global equidepthBins
        estimated_result = 0
        a = float(a)
        b = float(b)
        for bin in equidepthBins:
            range_difference = bin[1] - bin[0]
            numtuples = len(equidepthBins[bin])
            if bin[0] <= a < bin[1] and bin[0] < b <= bin[1]:
                ab_difference = b - a
                percentage = ab_difference/range_difference
                estimated_result += (percentage*numtuples)
            elif bin[0] <= a < bin[1]:
                a_bin_difference = bin[1] - a
                percentage = a_bin_difference/range_difference
                estimated_result += (percentage*numtuples)
            elif bin[0] <= b < bin[1]:
                b_bin_difference = b - bin[0]
                percentage = b_bin_difference/range_difference
                estimated_result += (percentage*numtuples)
            elif bin[0] > float(a) and bin[1] < float(b):
                estimated_result += numtuples
        return estimated_result

    # Print stats
    def print(self):
        global min_income, max_income, incomeList, equiwidthBins, equidepthBins
        print()
        print(len(incomeList), ' valid income values')
        print("minimum income = ", min_income)
        print("maximum income = ", max_income)

    def print_equiwidth(self):
        # Equi-width data
        print("\nequiwidth:")
        for key in equiwidthBins:
            range = str(key).replace('(', '[')
            print("range: ", range, ", numtuples: ", len(equiwidthBins[key]))

    def print_equidepth(self):
        # Equi-depth data
        print("\nequidepth: ")
        for key in equidepthBins:
            range = str(key).replace('(', '[')
            print("range: ", range, ", numtuples: ", len(equidepthBins[key]))
