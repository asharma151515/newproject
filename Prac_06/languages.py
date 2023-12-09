"""
Estimated time : 30 minutes
Actual time : 40 minutes
"""

from Prac_06.programming_language import ProgrammingLanguage

python = ProgrammingLanguage("Python", "Dynamic", True, 1991)
ruby = ProgrammingLanguage("Ruby", "Dynamic", True, 1995)
visual_basic = ProgrammingLanguage("Visual Basic", "Static", False, 1991)
print(python)

programming_languages = [python, ruby, visual_basic]
dynamic_language = [language for language in programming_languages if language.is_dynamic()]
print("The dynamically typed languages are:")
for language in dynamic_language:
    print(f"{language.name}", end="\n")
from Prac_06.programming_language import ProgrammingLanguage


def main():
    ruby = ProgrammingLanguage("Ruby", "Dynamic", True, 1995)
    python = ProgrammingLanguage("Python", "Dynamic", True, 1991)
    visual_basic = ProgrammingLanguage("Visual Basic", "Static", False, 1991)

    print("The Languages are ruby, python and visual_basic")

    languages = [ruby, python, visual_basic]

    print("The dynamically typed languages are:")
    for language in languages:
        if language.is_dynamic():
            print(language.name)


main()