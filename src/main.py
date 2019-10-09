from PyInquirer import prompt

from questions import meta_questions, standard_questions

ignore_answers = prompt(meta_questions)
standard_answers = prompt(standard_questions)
print(ignore_answers)
print(standard_answers)
