import csv
with open('data.csv', mode='w', newline='') as file:
    writer = csv.writer(file)
    writer.writerow(['Name', 'Age', 'City'])
    writer.writerow(['Alice', 28, 'Los Angeles'])
    writer.writerow(['Bob', 34, 'Chicago'])
    writer.writerow(['Charlie', 25, 'New York'])
with open('data.csv', mode='r') as file:
    reader=csv.reader(file)
    i=0
    for row in reader:
        print(row)
        i+=1
    print(f'Total rows: {i}')