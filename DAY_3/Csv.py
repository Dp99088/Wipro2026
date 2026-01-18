import csv
with open("student.csv","w",newline="") as file:
    writer=csv.writer(file)
    writer.writerow(["Name","ID","Age"])
    writer.writerow(["Durga",1,23])
    writer.writerow(["Balu", 2, 22])
    writer.writerow(["Manoj", 3, 24])
    writer.writerow(["Lawrence", 4, 25])