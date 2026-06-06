attendance=list(map(str,input("Enter the attendance of students: ").casefold().split()))
print(f"Number of Absents: {attendance.count('absent')}")
print(f"Number of Presents: {attendance.count('present')}")