import csv

global incomeList, equiwidthBins, equidepthBins

# List of Income attribute
incomeList = list()
incomeListSize = len(incomeList)
# Bins as dictionary
equiwidthBins = dict()
equidepthBins = dict()


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
    global incomeList, equiwidthBins
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


def equidepth():
    start = 0
    pointer = int((len(incomeList)/100))
    stop = pointer
    for i in range(100):
        b = [incomeList[start], incomeList[stop]]
        b = str(b).replace(']', ')')
        equidepthBins[b] = incomeList[start:stop]
        start = stop
        stop += pointer

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
for key in equiwidthBins:
    print("range: ", key, ", numtuples: ", len(equiwidthBins[key]))

equidepth()
print("equidepth: ")
for key in equidepthBins:
    print("range: ", key, ", numtuples: ", len(equidepthBins[key]))
