import numpy as np
from loader import load_data
from cleaner import missing_val,duplicate,invalid,handle_missing,handling_duplicates,fix_invalids
from statistic import mean_marks,median_marks,max_marks,min_marks,variance_marks,std_deviation_marks
from analytics import average, percentage, top_student, bottom_student, top_n_students, subject_toppers
from normalization import min_max_scale, standardize
from correlation import correlation_matrix, subject_correlation, correlation_with_average

data = load_data("student_performance_dataset.csv")

# data info
print("============================Data Info============================")
print("shape: ",data.shape)
print("Missing values: ",missing_val(data))
print("Duplicate values: ",duplicate(data))

# invalid marks
print("===========================Invalid Marks===========================")
inval = invalid(data)
print("Total Invalid Marks: ",inval.sum())
print("Location of Invalid Marks: ", np.where(inval))
# fixing invalid values
print("Fixing invalid marks")
data = fix_invalids(data)

# removing missing values
print("==========================Handling Missing Values==========================")
print("How do you want to handle missing values?")
print("1. Replace with 0")
print("2. Replace with mean")
choice = int(input("Enter choice: "))
data = handle_missing(data,choice)

# removing duplicates
print("============================Removing Duplicates============================")
print("Rows with duplicate values",data.shape[0])
print("Removing Duplicate Student Ids")
data = handling_duplicates(data)
print("Rows after removing duplicate values",data.shape[0])


print("============================Analysis============================")
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

print("============================Top and Bottom Students============================")
# print("Average marks of each student: ", average(data))
# print("Percentage of each student: ", percentage(data))
print("Student with highest percentage: ", top_student(data)[0], "with percentage: ", top_student(data)[1])
print("Student with lowest percentage: ", bottom_student(data)[0], "with percentage: ", bottom_student(data)[1])
print("Top 3 students: ", top_n_students(data, 3)[0], "with percentages: ", top_n_students(data, 3)[1])
print("Topper in each subject: ", subject_toppers(data))

print("============================Normalization============================")
print("Normalizing the data using Min-Max Scaling")
print("Min-Max Scaled Data: \n",min_max_scale(data))
scaled_data = min_max_scale(data)
print(scaled_data.shape)
print(np.min(scaled_data[:, 1:], axis=0))
print(np.max(scaled_data[:, 1:], axis=0))
print("Standardizing the data using Z-score Normalization")
standardized_data = standardize(data)

print(standardized_data.shape)
print(np.mean(standardized_data, axis=0))
print(np.std(standardized_data, axis=0))

print("============================Correlation============================")
print("Correlation Matrix: \n",correlation_matrix(data))
print("Correlation between Math and Physics: ",subject_correlation(data, 1, 2))
print("Correlation with average marks: \n",correlation_with_average(data))