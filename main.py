# Serafeim Themistokleous 4555

import experiment
import histograms


def main():
    csv_path = input("Please enter csv file path: ")
    csv_attribute = input("Please enter attribute (ex. Income): ")
    select = input("\n1. Run a single range query. \n2. Run experiments with random range queries. \nPlease enter a "
                   "number: ")

    if select == '1':
        a, b = input("\nPlease enter a range query [a,b). Each value seperated by space (ex. 19000 55000): \n").split()
        histogram = histograms.Histogram(csv_path, csv_attribute)
        histogram.read_income_data()
        histogram.equiwidth()
        histogram.equidepth()
        histogram.print_result()
        histogram.print_equiwidth_result()
        histogram.print_equidepth_result()
        result = histogram.actual_result(a, b)
        equiwidth_result = histogram.equiwidth_estimated_result(a, b)
        equidepth_result = histogram.equidepth_estimated_result(a, b)
        print("\nestimated equiwidth result: ", equiwidth_result)
        print("estimated equidepth result: ", equidepth_result)
        print("actual result: ", result)
    elif select == '2':
        n = input("\nEnter a number of experiments to run: ")
        experiment.experiments(csv_path, csv_attribute, int(n))


if __name__ == "__main__":
    main()

