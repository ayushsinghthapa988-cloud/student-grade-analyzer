from database import connect_db
from queries import get_top_students, Class_average
import pandas as pd

# Read CSV
df = pd.read_csv("data/students.csv")

print("Original Data:\n")
print(df)

print("\nMissing Values:\n")
print(df.isnull().sum())

df = df.dropna()

for subject in ["math", "science", "english"]:
    if (df[subject] > 100).any() or (df[subject] < 0).any():
        print(f"Invalid marks found in {subject}")

df["Total"] = df["math"] + df["science"] + df["english"]
df["Average"] = df["Total"] / 3

def assign_grade(avg):
    if avg >= 90:
        return "A"
    elif avg >= 80:
        return "B"
    elif avg >= 60:
        return "C"
    else:
        return "Fail"

df["Grade"] = df["Average"].apply(assign_grade)

conn = connect_db()

df.to_sql("Students", conn, if_exists="replace", index=False)

print("\nTop Students:\n")
print(get_top_students(conn))

print("\nClass Average:\n")
print(Class_average(conn))

df.to_csv("final_report.csv", index=False)

print(f"\nProject Completed Successfully. Students Processed: {len(df)}")

conn.close()
