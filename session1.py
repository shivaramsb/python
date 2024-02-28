instructor_name="Sumit Mittal"
course_fee="800"
course_rating=4.95
starting_soon=True
total_income=None


print(type(instructor_name))
print(type(course_fee))
print(type(course_rating))
print(type(starting_soon))
print(type(total_income))
print(course_fee+50)

print(course_fee+50.5)
print(course_fee)
print(course_fee+50.5)
course_fee=course_fee + (course_fee * .1)
print(course_fee)

print(type(course_fee))

course_fee="800"

print(type(course_fee))

course_fee=int(int(course_fee))+(int(int(course_fee)*.1))
print(course_fee)

first_name="Shivaram"
last_name="Babar"
print(first_name+last_name)
print(first_name +" "+ last_name)

print("My name is " +first_name + " and my last name is "+ last_name)

print("-----"*9)
print(f"My First name is {first_name} and my last name is {last_name}")
print("-----"*9)

salary = input ("what is your current salary: ")
hike = input ("what is the hike percentage : ")
new_salary=int(salary) + (int(salary)) * int(hike)/100
print(new_salary)

salary = input("what is your current salary: ")
hike = input("what is the hike percentage: ")

new_salary = int(salary) + (int(salary) * int(hike)/100)
print(new_salary)

print(f"The new salary after the hike is : {new_salary}")


