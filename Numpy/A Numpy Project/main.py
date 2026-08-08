import numpy as np
from loader import load_data
from cleaner import missing_val,duplicate,invalid,handle_missing,handling_duplicates,fix_invalids
from statistic import mean_marks,median_marks,max_marks,min_marks,variance_marks,std_deviation_marks
from analytics import average, percentage, max_percentage

data = load_data("student_performance_dataset.csv")

# data info
print("shape: ",data.shape)
print("Missing values: ",missing_val(data))
print("Duplicate values: ",duplicate(data))

# invalid marks
inval = invalid(data)
print("Total Invalid Marks: ",inval.sum())
print("Location of Invalid Marks: ", np.where(inval))

# removing missing values
print("How do you want to handle missing values?")
print("1. Replace with 0")
print("2. Replace with mean")
choice = int(input("Enter choice: "))
data = handle_missing(data,choice)

# removing duplicates
print("Rows with duplicate values",data.shape[0])
print("Removing Duplicate Student Ids")
data = handling_duplicates(data)
print("Rows after removing duplicate values",data.shape[0])

# fixing invalid values
print("Fixing invalid marks")
data = fix_invalids(data)

subjects = ["       Math", "      Physics", "    Chemistry", "    English"]

print(f"{'':15}", end="")
for subject in subjects:
    print(f"{subject:12}", end="")
print()

for name, values in [
    ("Mean", mean_marks(data)),
    ("Median", median_marks(data)),
    ("Maximum", max_marks(data)),
    ("Minimum", min_marks(data)),
    ("Variance", variance_marks(data)),
    ("Std Dev", std_deviation_marks(data))
]:
    print(f"{name:15}", end="")
    for value in values:
        print(f"{value:12.2f}", end="")
    print()
# print("Mean marks: ", np.round(mean_marks(data), 2))
# print("Median marks: ", np.round(median_marks(data), 2))
# print("Max marks: ", np.round(max_marks(data), 2))
# print("Min marks: ", np.round(min_marks(data), 2))
# print("Varience marks: ", np.round(variance_marks(data), 2))
# print("Standard Deviation marks: ", np.round(std_deviation_marks(data), 2))


print("Average marks of each student: ", average(data))
print("Percentage of each student: ", percentage(data))
print("Student with highest percentage: ", max_percentage(data))
