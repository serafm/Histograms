import random
import histograms

global accuracy_equiwidth_list, accuracy_equidepth_list, histogram


def experiments(csv_path, csv_attribute, n, r):
    global accuracy_equiwidth_list, accuracy_equidepth_list, histogram

    accuracy_equiwidth_list = list()
    accuracy_equidepth_list = list()

    histogram = histograms.Histogram(csv_path, csv_attribute)
    histogram.read_income_data()
    histogram.equiwidth()
    histogram.equidepth()
    histogram.print()

    for i in range(1, n):
        a = random.randint(r[0], r[1])
        b = random.randint(r[0], r[1])
        while a > b:
            a = random.randint(r[0], r[1])
        #print("Experiment ", i)
        #print("a= ", a)
        #print("b= ", b)
        #print("\n")

        act_result = histogram.actual_result(a, b)
        est_equiwidth = histogram.equiwidth_estimated_result(a, b)
        est_equidepth = histogram.equidepth_estimated_result(a, b)

        if act_result > 0:
            error_rate_equiwidth = (abs((est_equiwidth - act_result)) / act_result) * 100
            accuracy_equiwidth = 100 - error_rate_equiwidth

            error_rate_equidepth = (abs((est_equidepth - act_result)) / act_result) * 100
            accuracy_equidepth = 100 - error_rate_equidepth
        else:
            accuracy_equiwidth = 0
            accuracy_equidepth = 0
        accuracy_equiwidth_list.append(accuracy_equiwidth)
        accuracy_equidepth_list.append(accuracy_equidepth)

    class bcolors:
        green = '\033[92m'
        end = '\033[0m'
        bold = '\033[1m'

    # Metrics
    mo_equiwidth = sum(accuracy_equiwidth_list) / len(accuracy_equiwidth_list)
    mo_equidepth = sum(accuracy_equidepth_list) / len(accuracy_equidepth_list)
    print(bcolors.green + bcolors.bold + "\nAccuracy of histograms" + bcolors.end)
    print("equiwidth accuracy = ", round(mo_equiwidth, 2), "%")
    print("equidepth accuracy = ", round(mo_equidepth, 2), "%")


def main():
    csv_path = input("Please enter csv file path: ")
    csv_attribute = input("Please enter attribute (ex. Income): ")
    select = input("\n1. Run a single range query. \n2. Run experiments with random range queries. \nPlease enter a "
                   "number: ")

    if select == '1':
        a, b = input("\nPlease enter a range query [a,b). Each value seperated by space (ex. 1000 5500): \n").split()
        histogram = histograms.Histogram(csv_path, csv_attribute)
        histogram.read_income_data()
        histogram.equiwidth()
        histogram.equidepth()
        histogram.print()
        result = histogram.actual_result(a, b)
        equiwidth_result = histogram.equiwidth_estimated_result(a, b)
        equidepth_result = histogram.equidepth_estimated_result(a, b)
        print("\nactual result: ", result)
        print("estimated equiwidth result: ", equiwidth_result)
        print("estimated equidepth result: ", equidepth_result)
    elif select == '2':
        n = input("\nEnter a number of experiments to run: ")
        a, b = input("Enter range (ex. 1000 2000): ").split()
        r = [int(a), int(b)]
        experiments(csv_path, csv_attribute, int(n), r)


if __name__ == "__main__":
    main()

