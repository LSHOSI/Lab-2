def main():
    print("ET0735 (DevOps for AIoT) - Lab 2 - Introduction to Python")
    display_main_menu()
    num_list = get_user_input()
    x = calc_average(num_list)
    print(x)
    find_min_max(num_list)


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


#def sort_temperature():
#def calc_median_temperature():

if __name__ == "__main__":
    main()
