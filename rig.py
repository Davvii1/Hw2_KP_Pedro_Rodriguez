import random
import os.path
import time


# Method to validate k, n, min inputs
def validate(text=""):
    while True:
        try:
            value = int(input(text))
        except ValueError :
            print("Enter a valid value")
            continue
        else:
            if value > 0:
                return value
            else:
                print("Input can`t be 0")


# Method to validate range
def validateR(minvalue, text=""):
    while True:
        try:
            value = int(input(text))
        except ValueError:
            print("Enter a valid value")
            continue
        else:
            if value > minvalue:
                return value
            else:
                print("Input must be greater than minimum value")


# Asking for instances to be generated INPUT
k = validate('Instances to be generated: ')

for x in range(k):
    # Asking for items, min and max values INPUT
    n = validate('Number of items on instance ' + str(x + 1) + ': ')
    v_min = validate('Minimum value on instance ' + str(x + 1) + ': ')
    v_max = validateR(v_min, 'Maximum value on instance ' + str(x + 1) + ': ')
    w_min = validate('Minimum weight on instance ' + str(x + 1) + ': ')
    w_max = validateR(w_min, 'Maximum weight on instance ' + str(x + 1) + ': ')
    # Starting time of file creation
    s_count = time.time()
    # Getting number of previous files in 'instances' directory
    p_files = len(os.listdir(os.path.dirname(__file__) + '/instances'))
    # Creating the instance file OUTPUT
    path = os.path.join(os.path.dirname(__file__) + '/instances', 'instance#' + str(p_files + 1) + '.txt')
    i_file = open(path, 'w')
    print('instance#' + str(p_files + 1) + '.txt' + " successfully generated")
    # Write first line of file with n and W
    W = int(((n * (w_max + w_min) / 2) * 0.3))
    i_file.write(str(n) + ' ' + str(W) + '\n')
    # Fill lines with random numbers for every item
    for y in range(n):
        v_i = random.randint(v_min, v_max)
        w_i = random.randint(w_min, w_max)
        i_file.write(str(v_i) + ' ' + str(w_i) + '\n')
    i_file.close()
# Showing the running time OUTPUT
print("-- Running time: " + str(round(time.time() - s_count)) + " seconds --")
