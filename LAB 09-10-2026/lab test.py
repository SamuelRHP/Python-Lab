# Samuel Rohlupuia
# 25BTRCA049
# Lab-Exam Question 7. Common Elements in Student Courses
c1 = set(map(int, input("Enter roll numbers in Course 1: ").split()))
c2 = set(map(int, input("Enter roll numbers in Course 2: ").split()))
c3 = set(map(int, input("Enter roll numbers in Course 3: ").split()))

all_three = c1 & c2 & c3
at_least_one = c1 | c2 | c3

exactly_one = (c1 - c2 - c3) | (c2 - c1 - c3) | (c3 - c1 - c2)

c1_not_c2 = c1 - c2

exactly_two = ((c1 & c2) - c3) | ((c1 & c3) - c2) | ((c2 & c3) - c1)

print("\nStudents in all three courses:", sorted(all_three))
print("Students in at least one course:", sorted(at_least_one))
print("Students in exactly one course:", sorted(exactly_one))
print("Students in Course 1 but not Course 2:", sorted(c1_not_c2))
print("Number of students taking exactly two courses:", len(exactly_two))
