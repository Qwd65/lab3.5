import pandas as pd

df = pd.read_csv("students_grades.csv")

# Среднее значение оценок студентов по различным предметам
average_grades = df.iloc[:, 3:].mean()
print("Среднее значение оценок по различным предметам:")
print(average_grades)

# Распределение оценок студентов
grade_distribution = df.iloc[:, 3:].apply(pd.Series.value_counts).fillna(0)
print("\nРаспределение оценок студентов:")
print(grade_distribution)

# Корреляция между оценками по разным предметам
correlation_matrix = df.iloc[:, 3:].corr()
print("\nКорреляция между оценками по разным предметам:")
print(correlation_matrix)

# Среднее значение возраста студентов
average_age = df['Возраст'].mean()
print("\nСреднее значение возраста студентов:", average_age)

# Распределение возраста студентов
age_distribution = df['Возраст'].value_counts().sort_index()
print("\nРаспределение возраста студентов:")
print(age_distribution)