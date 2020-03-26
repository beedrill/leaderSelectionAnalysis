import csv
from k_uniform import FourUniform

csvfile = open('four-uniform.csv', 'w', newline='')
csvwriter = csv.writer(csvfile, delimiter=',')

list_p = [0.9, 0.6]

list_q = [0.1, 0.2, 0.5]

row = ["4 x car"]
for p in list_p:
    for q in list_q:
        row.append("p = " + str(p) + ", q = " + str(q))
csvwriter.writerow(row) #number_of_msg

for m in range(1, 11):
    row = [m]
    for p in list_p:
        for q in list_q:
            four_uniform = FourUniform(p, q, [m, m, m, m])
            four_uniform.compute()
            row.append(four_uniform.getConvTime())
    csvwriter.writerow(row) #number_of_msg
    print("computation done for m = " + str(m))
    