import os.path
from operator import itemgetter
import time


# Validate selected file
def validateS(files, text=""):
    while True:
        try:
            value = int(input(text))
        except ValueError:
            print("Enter a valid value")
            continue
        else:
            if 0 < value <= files:
                return value
            else:
                print("Select an existing file")


# Validate heuristic selected
def validateH(text=""):
    while True:
        try:
            value = int(input(text))
        except ValueError:
            print("Enter a valid value")
            continue
        else:
            if 0 < value <= 3:
                return value
            else:
                print("Select a valid heuristic")


print('-- Select a file to apply the heuristic --')

# Get the instances files
i_arr = os.listdir(os.path.dirname(__file__) + '/instances')
for x in range(len(i_arr)):
    print(str(x + 1) + '.- ' + i_arr[x])
s_file = i_arr[validateS(len(i_arr), 'Enter the number of the selected file: ') - 1]
o_file = open(os.path.dirname(__file__) + '/instances/' + s_file, "r")

# Store n, W and data from items
k_data = o_file.readline().strip().split(' ')
n = int(k_data[0])
W = int(k_data[1])
data = []
for line in o_file.readlines():
    data.append([int(x) for x in line.strip().split(' ')])

# Ask for heuristic to use
heuristic = validateH('Heuristics:\n1.-Heuristic 1\n2.-Heuristic 2\n3.-Heuristic 3\nSelect the heuristic that you '
                      'want to use: ')

# Starting time of file creation
s_count = time.time()

# Sort heuristics
if heuristic == 1:
    data.sort(key=itemgetter(0), reverse=True)
elif heuristic == 2:
    data.sort(key=itemgetter(1))
else:
    for x in range(len(data)):
        r = (data[x][0]) / (data[x][1])
        data[x].append(r)
    data.sort(key=itemgetter(2), reverse=True)

# Calculus
totalW = 0
totalV = 0
for y in range(len(data)):
    if (totalW + data[y][1]) <= W:
        totalW += data[y][1]
        totalV += data[y][0]

# Print results
print("-- Results --")
print('Total of items: ' + str(n))
print('Total weight: ' + str(totalW))
print('Residual capacity: ' + str((W - totalW)))
print('Objective function: ' + str(totalV))
print("-- Running time: " + str(round(time.time() - s_count)) + " seconds --")
