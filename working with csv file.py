import csv
with open("data.csv", "w") as file:
    writer = csv.writer(file)
    writer.writerow(["id","name","year"])
    writer.writerow([1,"sahana",2001])
    writer.writerow([2,"gowtham",2000])
    writer.writerow([3,"preethi",2002])
    writer.writerow([4,"karun",1999])