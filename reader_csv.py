import csv
#data = ['2,True', '3,True', '12,False', '13,False']

data = [[2, True], [3, True], [12, False], [13, False]]
csv_writer = csv.writer(open('prime.csv', 'w'))
csv_writer.writerows(data)

with open('prime.csv', 'r') as output_file:
    csv_writer = csv.writer(output_file)
    for line in csv_writer:
        print(line)