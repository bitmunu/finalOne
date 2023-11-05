import csv
import random
import os

def DelNaN(new_name, delim=','):
    with open("data.csv", "r") as kek:
        reader = csv.reader(kek, delimiter=delim)

        with open("neweedata.csv", "w", newline="") as xd:
            writer = csv.writer(xd, delimiter=delim, quotechar='"')

            for row in reader:
                if all(cell != '' for cell in row):
                    writer.writerow(row)
def Parse(name, type="top", number_of_rows=5, b=False, delim = ','):
    rows = []
    aligns = []
    number = 0
    filename = name + ".csv"
    with open(filename, "r") as csvfile:
        reader = csv.reader(csvfile, delimiter=delim, quotechar='"')
        for row in reader:
            for column_index, entry in enumerate(row):
                if column_index >= len(aligns):
                    aligns.append(len(entry))
                else:
                    aligns[column_index] = max(aligns[column_index], len(entry))
            rows.append(row)

    if type == "top" and b == True:
        try:
            for j in range(0, number_of_rows):
                for i in range(0, len(aligns)):
                    print("      ".join([f"{rows[j][i].ljust(int(aligns[i] + 1))}"]), end='')
                print(end='\n')
        except Exception as e:
            print(f"xdError: {str(e)}")

    elif type == "bottom" and b == True:
        try:
            for i in range(0, len(aligns)):
                print("      ".join([f"{rows[0][i].ljust(int(aligns[i] + 1))}"]), end='')
            print(end='\n')
            for j in range(len(rows)-2, len(rows)-number_of_rows, -1):
                for i in range(0, len(aligns)):
                    print("      ".join([f"{rows[j][i].ljust(int(aligns[i] + 1))}"]), end='')
                print(end='\n')
        except Exception as e:
            print(f"xdError: {str(e)}")

    elif type == "random" and b == True:
        try:
            for i in range(0, len(aligns)):
                print("      ".join([f"{rows[0][i].ljust(int(aligns[i] + 1))}"]), end='')
            print(end='\n')

            for j in range(0, number_of_rows):
                for i in range(0, len(aligns)):
                    print("      ".join([f"{rows[random.randint(1, len(rows))][i].ljust(int(aligns[i] + 1))}"]), end='')
                print(end='\n')
        except Exception as e:
            print(f"xdError: {str(e)}")
    return len(rows), len(aligns)
def Show(type="top", number_of_rows=5, delim=','):
    if type == "top":
        Parse("neweedata","top", number_of_rows, True)
    elif type == "bottom":
        Parse("neweedata", "bottom", number_of_rows, True)
    elif type == "random":
        Parse("neweedata", "random", number_of_rows, True)

def Info(name, new_name, delim=','):
    a, b = Parse(name)
    ss = '\u0425'
    print(f"{a} {ss} {b}")
    filename = name + ".csv"
    with open(filename, "r") as csvfile:
        reader = csv.reader(csvfile, delimiter=",", quotechar='"')
        counts = [0]*b
        fields = csvfile.readline()
        fields = list(map(str, fields.split(delim)))
        for row in reader:
            for i in range(0, len(row)):
                if row[i] != '':
                    counts[i]+=1
        for j in range(0, len(counts)):
            print(f"{fields[j]} {counts[j]}")

def MakeDS(name, delim =','):
    filename = name +".csv"
    rows=[]
    with open(filename, "r") as csvfile:
        reader = csv.reader(csvfile, delimiter=delim, quotechar='"')
        fields = csvfile.readline()
        for row in csvfile:
            rows.append(row)
        #fields = list(map(str, fields.split(delim)))
    if not os.path.isdir("workData"):
        os.mkdir("workData")
        os.chdir("workData")
        os.mkdir("Learning")
        os.mkdir("Testing")
    random.shuffle(rows)
    split_index = int(0.7 * len(rows))
    train = rows[:split_index]
    test = rows[split_index:]

    with open('workData/Learning/train.csv', 'w', newline='') as f:
        writer = csv.writer(f, delimiter=',')
        f.write(fields)
        for i in range(0, len(test)):
            f.write(train[i])
        #writer.writerows(train)
    with open('workData/Testing/test.csv', 'w', newline='') as f:
        writer = csv.writer(f, delimiter=',')
        f.write(fields)
        for i in range(0, len(test)):
            f.write(test[i])
        #writer.writerows(test)




DelNaN("neweedata")
Info("data", "neweedata")
Show("random", 7)
MakeDS("neweedata")