# write a broken program to determine the score

import random


def main():
    """Input score"""
    score = float(input("Enter score: "))
    grade = get_grade(score)
    print(grade)
    print(f"The random score is", get_grade(random.randint(0, 100)))


def get_grade(score):
    """This function is to determine the grade of a score"""
    if score < 0 or score > 100:
        return "Invalid Score"

    else:
        if score >= 90:
            return "Excellent"
        elif score >= 50:
            return "Passable"
        elif score >= 50:
            return "Bad"



main()