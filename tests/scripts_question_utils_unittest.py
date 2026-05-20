import unittest
from pathlib import Path
from scripts.question_utils import get_answered_questions, get_question_list


def open_test_case_file(n: int) -> str:
    path = Path(__file__).parent / "testcases" / f"testcase{n}.md"
    return path.read_text(encoding="utf-8")


class QuestionCount(unittest.TestCase):

    def test_case_1(self):
        raw = open_test_case_file(1)
        question_list = get_question_list(raw)
        answers = get_answered_questions(raw)

        self.assertEqual(len(question_list), 11)
        self.assertEqual(len(answers), 3)

    def test_case_2(self):
        raw = open_test_case_file(2)
        question_list = get_question_list(raw)
        answers = get_answered_questions(raw)

        self.assertEqual(len(question_list), 16)
        self.assertEqual(len(answers), 11)
