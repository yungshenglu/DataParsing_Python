from operator import itemgetter
import csv


# Main function
def main():
    file = open('../Data/example.csv')
    fileReader = csv.reader(file)
    
    # Transfer the last column from string to integer for sorting
    data = []
    for row in fileReader:
        lastData = int(row[len(row) - 1])
        newRow = row[0 : len(row) - 1]
        newRow.append(lastData)
        data.append(newRow)
    
    data.sort(key = itemgetter(len(data[0]) - 1))
    
    # Transfer the last column from integer to string
    for row in data:
        newRow = row[0 : len(row) - 1]
        lastData = str(row[len(row) - 1])
        newRow.append(lastData)
        data[data.index(row)] = newRow
    
    # Print the result
    for row in data:
        print('Row #' + str(data.index(row) + 1) + ' ' + str(row))


# Main function
if __name__ == "__main__":
    main()