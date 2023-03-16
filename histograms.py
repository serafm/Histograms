import csv

global incomeList, bins

# List of Income attribute
incomeList = list()
# Bins as dictionary
bins = dict()


# Read csv file Income data, add them into a list
def read_income_data():
    with open('acs2015_census_tract_data.csv', newline='') as csvfile:
        data = list(csv.reader(csvfile))
        for income in range(1, len(data)):
            # if the field is empty don't add it in list
            if data[income][13] == '':
                continue
            else:
                incomeList.append(float(data[income][13]))


# Create an equi-width histogram
def equiwidth():
    global incomeList, bins
    start = 0
    min = min_income
    # The width for exact distribution of the values into the bins
    width = (max_income - min_income) / 100
    for i in range(100):
        # Range of every bin
        temp = [round(min, 2), round(min + width, 2)]
        b = str(temp).replace(']', ')')
        # Initialize the dictionary
        bins[b] = []
        # Add income values into the bins
        for income in range(start, len(incomeList)):
            if min <= incomeList[income] < min + width:
                bins[b].append(incomeList[income])
            else:
                start = income
                break
        # Update the value of min
        min = round(min + width, 2)


# def equidepth():


read_income_data()
incomeList = sorted(incomeList)
# Minimum income
min_income = min(incomeList)
# Maximum income
max_income = max(incomeList)

equiwidth()

print(len(incomeList), ' valid income values')
print("minimum income = ", min_income)
print("maximum income = ", max_income)
print("equiwidth:")
for key in bins:
    print("range: ", key, ", numtuples: ", len(bins[key]))
