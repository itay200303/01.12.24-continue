
from collections import Counter
# 1.
for i in range(12, 24 + 1):
    print(i)
print()

# 2.
for i in range(7, 31 + 1):
    if i % 2 != 0:
        print(i)
print()

# 3.
for x in range(-20, 10 + 1):
    if x % 2 == 0:
        print(x)

# 4.
for i in range(1, 45 + 1):
    if i % 3 == 0:
        print("Fizz", i)
    if i % 5 == 0:
        print("Buzz", i)
    if i % 3 == 0 and i % 5 == 0:
        print("FizzBuzz", i)
print()


# 5.
def calculate(arr):
    total = 0
    for arr in arr:
        total += arr
    return total


numbers = [1, 13, 22, 123, 49, 34, 5, 24, 57, 45]
result = calculate(numbers)
print(result)
print()

# 6.
students = [
    {'id': 1, 'first_name': 'Itay', 'last_name': 'Trauner', 'age': 21, 'country': 'Isreal', 'city': 'Hadera'},
    {'id': 2, 'first_name': 'Daniel', 'last_name': 'Chaba', 'age': 25, 'country': 'Canada', 'city': 'Toronto'},
    {'id': 3, 'first_name': 'Maddy', 'last_name': 'Rose', 'age': 20, 'country': 'Russia', 'city': 'Moscow'}

]


def delete_property(students1, property_name):
    for student in students1:
        if property_name in student:
            del student[property_name]
    return students1


def print_student_property(students1):
    for student in students1:
        print("student Details: ")
        for key, value in student.items():
            print(f"{key}: {value}")
        print("---")


def age_student(student):
    sorted_age = sorted(student, key=lambda s: s["age"], reverse=True)
    return sorted_age


students = delete_property(students, 'country')
print_student_property(students)
sorted_students = age_student(students)
print("Sorted Students by Age:")
age_student(sorted_students)

# 7.
our_pets = [
    {
        "animal_type": "cat",
        "names": [
            "Meowzer",
            "Fluffy",
            "Kit-Cat"
        ]
    },
    {
        "animal_type": "dog",
        "names": [
            "Spot",
            "Bowser",
            "Frankie"
        ]
    }
]

def print_cat(pets):
    for pet in pets:
        if pet["animal_type"] == "cat":
            print(f"animalType: {pet["animal_type"]}")
            print(f"names: {', '.join(pet['names'])}")

def print_all_animal_type(pets , animal_type):
    found = False
    for pet in pets:
        if pet["animal_type"] == animal_type:
            found = True
            print(f"animalType: {pet['animal_type']}")
            print(f"names: {', '.join(pet['names'])}")
            break
    if not found:
        print(f"No animals of type {animal_type} found")

def add_name_to_animals(pets, animal_name):
    for pet in pets:
        if animal_name not in pet['names']:
            pet['names'].append(animal_name)

print_cat(our_pets)
print_all_animal_type(our_pets, "cat")
print_all_animal_type(our_pets, "dog")
print_all_animal_type(our_pets, "bird")
add_name_to_animals(our_pets, "Buddy")
add_name_to_animals(our_pets, "Meowzer")
print(our_pets)

# 8.
student = {
'name': 'John',
'age': 20,
'hobbies': ['reading', 'games', 'coding'],
}

def print_all_student_data(student1):
    for key, value in student1.items():
        print(f"{key}: {value}")

def add_hobby(student1, hobby):
    if hobby not in student1['hobbies']:
        student1['hobbies'].append(hobby)

add_hobby(student, 'painting')
print_all_student_data(student)

def remove_hobby(student3, hobby):
    if hobby in student3['hobbies']:
        student3['hobbies'].remove(hobby)

remove_hobby(student, 'reading')
print_all_student_data(student)

student['family_name'] = 'Doe'

#9.
matrix = [
[1, 2],
[3, 4],
[5, 6]
]

def print_all_elements(matrix):
    for row in matrix:
        for element in row:
            print(element, end=' ')
        print()
print_all_elements(matrix)

# 10.
matrix = [
[0,1,1],
[0,1,0],
[1,0,0]
]

def count_zero(matrix):
    zero_count = 0
    for row in matrix:
        for element in row:
            if element == 0:
                zero_count += 1
    return zero_count

zero_count = count_zero(matrix)
print(f"Numbers of zero in the matrix: {zero_count}")

# 11.
arr = [4,2,34,4,1,12,1,4]

def find_dup(arr):
    element_count = Counter(arr)
    duplicates = [key for key, value in element_count.items() if value > 1]
    return duplicates

duplicates = find_dup(arr)
print(f"Repeated elements: {duplicates}")

# 12.
arr = [43, "what", 9, True, "cannot", False, "be", 3, True]
def rev_arr(arr):
    reversed_arr = []
    for i in range(len(arr) - 1, -1, -1):
        reversed_arr.append(arr[i])
    return reversed_arr
print(rev_arr(arr))

# 13.
first_array = [4, 6, 7]
second_array = [8, 1, 9]
def sum_arrays(first_array, second_array):
    return [first_array[i] + second_array[i] for i in range(len(first_array))]

print(sum_arrays(first_array, second_array))

# 14.
first_str = "racecar"
second_str = "Java"
def is_palindrome(s):
    return s == s[::-1]

print(is_palindrome(first_str))
print(is_palindrome(second_str))

# 15.
counter = 1
while counter < 100:
    counter *= 2
    print(counter)

# 16.
counter = 900000
while counter > 50:
    counter /= 2
    print(counter)

# 17.
def find_duplicates_using_while(arr):
    counts = {}
    i = 0
    duplicates = []
    while i < len(arr):
        if arr[i] in counts:
            counts[arr[i]] += 1
        else:
            counts[arr[i]] = 1
        i += 1
    for key, value in counts.items():
        if value > 1:
            duplicates.append(key)
    return duplicates

arr = ["apple", "banana", "apple", "orange", "banana"]
print(find_duplicates_using_while(arr))

# 18.
def remove_duplicates_using_while(arr):
    unique_elements = []
    i = 0
    while i < len(arr):
        if arr[i] not in unique_elements:
            unique_elements.append(arr[i])
        i += 1
    return unique_elements
names = ['Chris', 'Kevin', 'Naveed', 'Pete', 'Victor', 'Chris', 'Kevin']
print(remove_duplicates_using_while(names))

# 19.
def remove_duplicates_skip_pete(arr):
    unique_elements = []
    i = 0
    while i < len(arr):
        if arr[i] != 'Pete' and arr[i] not in unique_elements:
            unique_elements.append(arr[i])
        i += 1
    return unique_elements

names = ['Chris', 'Kevin', 'Naveed', 'Pete', 'Victor', 'Chris', 'Kevin']
print(remove_duplicates_skip_pete(names))

# 20.
def find_successive_equal(array):
    i = 1
    while i < len(array):
        if array[i] == array[i-1]:
            return i
        i += 1
    return -1

array1 = [True, False, False, True, True, False]
array2 = [True, False, True, False, True, True]
array3 = [True, False, True, False, True, False]

print(find_successive_equal(array1))
print(find_successive_equal(array2))
print(find_successive_equal(array3))

# 21.

def get_valid_user_input():
    while True:
        full_name = input("Enter your full name (first and last): ")
        if len(full_name.split()) == 2:
            break
        else:
            print("Invalid input. Please provide both first and last name.")

    while True:
        try:
            age = int(input("Enter your age: "))
            if 1 <= age <= 130:
                break
            else:
                print("Invalid age. Please enter a valid age between 1 and 130.")
        except ValueError:
            print("Invalid input. Please enter an integer for age.")

    # Validate email
    while True:
        email = input("Enter your email: ")
        if '@' in email:
            break
        else:
            print("Invalid email. Please make sure your email contains '@'.")

    print(f"Name: {full_name}, Age: {age}, Email: {email}")


get_valid_user_input()
