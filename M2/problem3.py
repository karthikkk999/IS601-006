a1 = [-1, -2, -3, -4, -5, -6, -7, -8, -9, -10]
a2 = [-1, 1, -2, 2, 3, -3, -4, 5]
a3 = [-0.01, -0.0001, -.15]
a4 = ["-1", "2", "-3", "4", "-5", "5", "-6", "6", "-7", "7"]


def process_array(num, arr):
    print("\nProcessing Array({}): \n\n".format(num))
    print(arr)
    print("\nPositive Output:\n")
    for x in arr:
        if type(x) == int:
            if x > 0:
                print(x, end=" ")
        elif type(x) == float:
            if x > 0.0:
                print("{:.4f}".format(x), end=" ")
        elif type(x) == str:
            if x.startswith("-"):
                continue
            else:
                print(x, end=" ")
        print("\n")
    # TODO add new code here to print the desired result


print("Problem 3")
process_array(1, a1)
process_array(2, a2)
process_array(3, a3)
process_array(4, a4)