subjects = ["Math", "Science", "English", "History", "Geography"]

print("Original Subjects:")
print(subjects)

print("\nTotal Subjects:", len(subjects))

subjects.sort()
print("\nSubjects in Ascending Order:")
print(subjects)

subjects.sort(reverse=True)
print("\nSubjects in Descending Order:")
print(subjects)

print("\nFirst Three Subjects:") #used slicing
print(subjects[:3])

print("\nRemaining Subjects:")
print(subjects[3:])