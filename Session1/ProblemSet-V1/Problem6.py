'''Write a function calculate_gpa() that calculates the grade point average (GPA) for a student based on their course grades and returns the gpa as a float. The function takes in a dictionary report_card as a parameter where each key-value pair represents a course and the grade received in that course respectively. The grades are represented as strings ("A", "B", "C", "D", "F") and each grade corresponds to a certain number of grade points:

"A" = 4
"B" = 3
"C" = 2
"D" = 1
"F" = 0

A GPA is calculated by finding the average of all grade points.

def calculate_gpa(report_card):
    pass
Example Usage:

report_card = {"Math": "A", "Science": "C", "History": "A", "Art": "B", "English": "B", "Spanish": "A"}
print(calculate_gpa(report_card))
Example Output: 3.33

'''

'''
    The repitetive if else statements can be removed using dictionaries, check below
    

    def calculate_gpa(report_card):
    just_values = report_card.values()
    sum = 0
    for grade in just_values:
        if grade == "A":
            sum += 4
        elif grade == "B":
            sum += 3
        elif grade == "C":
            sum += 2
        elif grade == "D":
            sum += 1
    GPA = sum/len(report_card)
    return round(GPA, 2)

report_card = {"Math": "A", "Science": "C", "History": "A", "Art": "B", "English": "B", "Spanish": "A"}
print(calculate_gpa(report_card)) '''

def calculate_gpa(report_card):
     grade_points = {
        "A": 4,
        "B": 3,
        "C": 2,
        "D": 1,
        "F": 0
        }
     total = 0 

     for grade in report_card.values():
          total += grade_points.get(grade)
     
     GPA = total/len(report_card)
     return round(GPA, 2)

report_card = {"Math": "A", "Science": "C", "History": "A", "Art": "B", "English": "B", "Spanish": "A"}
print(calculate_gpa(report_card))
     
    