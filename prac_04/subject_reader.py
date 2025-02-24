"""
CP1404/CP5632 Practical
Data file -> lists program
"""

FILENAME = "prac_04/subject_data.txt"


def load_data(filename):
    #Read data from file and return
    data = []
    with open(filename) as file:
        for line in file:
            parts = line.strip().split(',')
            parts[2] = int(parts[2])
            data.append(parts)
    return data

def display_subjects(data):
    #Display data
    for subject in data:
        code, lecturer, students = subject
        print(f"{code} is taught by {lecturer} and has {students} students")

def main():
    data = load_data(FILENAME)
    display_subjects(data)


main()
