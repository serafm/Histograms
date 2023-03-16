import csv

global data, incomeList, bins

# List of Income field
incomeList = list()

bins = dict()


# Read csv file data and add them into a list
def read_data():
    global data
    with open('acs2015_census_tract_data.csv', newline='') as csvfile:
        data = list(csv.reader(csvfile))
        for income in range(1, len(data)):
            if data[income][13] == '':
                continue
            else:
                incomeList.append(float(data[income][13]))


read_data()
incomeList = sorted(incomeList)
min_income = min(incomeList)
max_income = max(incomeList)


def equiwidth():
    global incomeList, bins
    start = 0
    min = min_income
    width = (max_income - min_income)/100
    for i in range(100):
        temp = [round(min, 2), round(min+width, 2)]
        b = str(temp).replace(']', ')')
        bins[b] = []
        for income in range(start, len(incomeList)):
            if min <= incomeList[income] < min+width:
                bins[b].append(incomeList[income])
            else:
                start = income
                break
        min = round(min + width, 2)


#def equidepth():



print(str(len(incomeList)) + ' valid income values')
print("minimum income = " + str(min_income))
print("maximum income = " + str(max_income))
print("equiwidth:")
equiwidth()
for key in bins:
    print("range: ", key, ", numtuples: ", len(bins[key]))
