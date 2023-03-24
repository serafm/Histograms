# Serafeim Themistokleous 4555

import histograms
import random


def experiments(csv_path, csv_attribute, n):

    accuracy_equiwidth_list = list()
    accuracy_equidepth_list = list()

    histogram = histograms.Histogram(csv_path, csv_attribute)
    min_max = histogram.read_income_data()
    histogram.equiwidth()
    histogram.equidepth()
    histogram.print_result()

    min = min_max[0]
    max = min_max[1]

    for i in range(1, n):
        a = random.randint(min, max)
        b = random.randint(min, max)
        while a > b:
            a = random.randint(min, max)

        act_result = histogram.actual_result(a, b)
        est_equiwidth_result = histogram.equiwidth_estimated_result(a, b)
        est_equidepth_result = histogram.equidepth_estimated_result(a, b)

        # calculate the accuracy of the two histograms to the actual results
        if act_result > 0:
            error_rate_equiwidth = (abs((est_equiwidth_result - act_result)) / act_result) * 100
            accuracy_equiwidth = 100 - error_rate_equiwidth

            error_rate_equidepth = (abs((est_equidepth_result - act_result)) / act_result) * 100
            accuracy_equidepth = 100 - error_rate_equidepth
        else:
            accuracy_equiwidth = 0
            accuracy_equidepth = 0
        accuracy_equiwidth_list.append(accuracy_equiwidth)
        accuracy_equidepth_list.append(accuracy_equidepth)

    # Metrics
    mo_equiwidth = sum(accuracy_equiwidth_list) / len(accuracy_equiwidth_list)
    mo_equidepth = sum(accuracy_equidepth_list) / len(accuracy_equidepth_list)
    print("\nAccuracy of histograms")
    print("equiwidth accuracy = ", round(mo_equiwidth, 2), "%")
    print("equidepth accuracy = ", round(mo_equidepth, 2), "%")
