def main():
    print("ET0735 (DevOps for AIoT) - Lab 2 - Introduction to Python")
    display_main_menu()
    num_list = get_user_input()
    x = calc_average(num_list)
    print("Mean = ", x)
    find_min_max(num_list)
    sort_temperature(num_list)
    print(sort_temperature(num_list))
    calc_median_temperature(num_list)


def display_main_menu():
    print("Enter some numbers separated by commas (e.g. 5,67, 32)");


def get_user_input():
    x = input()
    y = x.split(",")
    float_list = []
    for x in y:
        float_list.append(float(x))
    print(float_list)
    return float_list


def calc_average(float_list):
    avg = sum(float_list) / len(float_list)
    return float(avg)


def find_min_max(float_list):
    maximum = max(float_list)
    minimum = min(float_list)
    print("Maximum = ",maximum)
    print("Minimum = ",minimum)


def sort_temperature(float_list):
    float_list.sort()
    return float_list


def calc_median_temperature(float_list):
    n = len(float_list)
    if n % 2 == 0:
        median1 = float_list[n//2]
        median2 = float_list[n//2-1]
        median = (median1 + median2)/2
    else:
        median = float_list[n//2]

    print("Median is: " + str(median))


if __name__ == "__main__":
    main()
