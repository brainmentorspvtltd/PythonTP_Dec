# csv - comma separated files
import csv

# data = [
#     ['First name', 'Last name'],
#     ['Virat','Kohli'],
#     ['Rohit','Sharma'],
#     ['KL','Rahul'],
#     ['MS','Dhoni']
# ]

# with open('players.csv', 'w', newline='') as file:
#     writer = csv.writer(file)
#     for row in data:
#         writer.writerow(row)

with open('players.csv') as file:
    reader = csv.reader(file)
    # print(reader)
    for r in reader:
        print(r)

