'''Check the exam
'''


def is_answer_correct(correct, answer):
    return correct == answer


def check_exam(correct_ans, student_ans):
    return max(sum([0 if answer == "" else
                    (+4 if is_answer_correct(correct, answer) else -1)
                    for correct, answer in zip(correct_ans, student_ans)]), 0)
