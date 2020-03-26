import csv
from k_uniform import OneUniform

csvfile = open('one-uniform.csv', 'w', newline='')
csvwriter = csv.writer(csvfile, delimiter=',')

list_p = [0.9, 0.8, 0.5, 0.4, 0.3]

row = ["car"]
for p in list_p:
    row.append("p = " + str(p))
csvwriter.writerow(row) #number_of_msg

for m in range(2, 100):
    row = [m]
    for p in list_p:
        four_uniform = OneUniform(p, m)
        four_uniform.compute()
        row.append(four_uniform.getConvTime())
    csvwriter.writerow(row) #number_of_msg