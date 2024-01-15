"""O foco desse programa e receber uma nota de um aluno de 0 a 10, e validar se o valor digitado está dentro desse range de valores aceitos"""

def is_validation_type_grade(student_grade):
    if not isinstance(student_grade, (float, int)):
        raise Exception ("The format this grade is not valid!!! \n")
    
    elif student_grade < 0:
        raise Exception ("Its no possible to have grades below zero")
    
    else:
        return "The grades type is correct!!!"
    
def is_analys_range_grade(student_grade):
    ranges_grades = range(0, 10, 1)
    for range_grade in ranges_grades:
        if student_grade < range_grade.start and student_grade < range_grade.stop:
            return f"{student_grade}, is outside the accepted grade range"

def main():
    student_grade = int(input("Please enter a grade this your student for validation: "))

    validation_type_grade = is_validation_type_grade(student_grade)
    print(validation_type_grade)

    range_analysis = is_analys_range_grade(student_grade)
    print(range_analysis)

main()
