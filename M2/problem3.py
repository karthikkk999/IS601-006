a1 = [-1, -2, -3, -4, -5, -6, -7, -8, -9, -10]
a2 = [-1, 1, -2, 2, 3, -3, -4, 5]
a3 = [-0.01, -0.0001, -.15]
a4 = ["-1", "2", "-3", "4", "-5", "5", "-6", "6", "-7", "7"]

def process_array(num, arr):
    print("\nProcessing Array({}): \n\n".format(num))
    print(arr)
    print("\nPositive Output:\n")
    # TODO add new code here to print the desired result
    #check the datatype of each element and convert to +ve using abs(value) 
    final_arr = []
    for value in arr:
        if type(value) == int or type(value) == float:
            final_arr.append(abs(value))
        elif type(value) == str:
            final_arr.append(str(abs(int(value)))) #converted the datatype as original after making +ve 
    print(final_arr)


print("Problem 3")
process_array(1, a1)
process_array(2, a2)
process_array(3, a3)
process_array(4, a4)