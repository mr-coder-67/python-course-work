# Student exam data with attendance status and subject scores
# Each student has a nested dictionary containing their exam status and marks

data = {
    'subbu': {'status': True, 'python': 98, 'Mqsql': 95, 'flask': 94},
    'nagendra': {'status': True, 'python': 78, 'Mqsql': 65, 'flask': 84},
    'dinesh': {'status': False, 'python': None, 'Mqsql': None, 'flask': None},
    'ashu': {'status': True, 'python': 68, 'Mqsql': 55, 'flask': 64},
    'rishi': {'status': True, 'python': 33, 'Mqsql': 25, 'flask': 34},
}

# Ask the user to enter a student name
name = input("enter the name:")

# Check whether the entered name exists in the data dictionary
if name in data:
    # If the student exists, check if they attended/wrote the exam
    if data[name]['status']:
        # Calculate total marks from all subjects
        total = data[name]['python'] + data[name]['Mqsql'] + data[name]['flask']
        # Compute the average score
        avg = total / 3

        # Show different messages based on the average score
        if avg > 90:
            print(f"congrats {name}, you got first in class!!!")
        elif avg > 70:
            print(f"Good {name}, keep it up for the next time!!")
        elif avg > 35:
            print(f"Better {name}, work hard next time!")
        else:
            print(f"{name}, you have failed in the exam. Bring your parents")
    else:
        # Student record exists but exam was not written
        print(f"{name} didn't write the exam. Bring your parents")
else:
    # Student name not found in the data dictionary
    print(f"{name}'s data is not found")
