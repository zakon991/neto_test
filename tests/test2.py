import unittest
from main_task2 import create_course_dict, group_courses_by_duration, format_sorted_courses

class TestCourseSorting(unittest.TestCase):

    def test_create_course_dict(self):
        result = create_course_dict("Test Course", ["Test Mentor"], 10)
        expected = {"title": "Test Course", "mentors": ["Test Mentor"], "duration": 10}
        self.assertEqual(result, expected)

    def test_group_courses_by_duration(self):
        courses_list = [
            {"title": "Course1", "mentors": ["Mentor1"], "duration": 10},
            {"title": "Course2", "mentors": ["Mentor2"], "duration": 20},
            {"title": "Course3", "mentors": ["Mentor3"], "duration": 10}
        ]
        result = group_courses_by_duration(courses_list)
        expected = {10: [0, 2], 20: [1]}
        self.assertEqual(result, expected)

    def test_format_sorted_courses(self):
        courses_list = [
            {"title": "Course1", "mentors": ["Mentor1"], "duration": 10},
            {"title": "Course2", "mentors": ["Mentor2"], "duration": 20},
            {"title": "Course3", "mentors": ["Mentor3"], "duration": 10}
        ]
        durations_dict = {10: [0, 2], 20: [1]}
        result = format_sorted_courses(courses_list, durations_dict)
        expected = [
            "Course1 - 10 месяцев",
            "Course3 - 10 месяцев",
            "Course2 - 20 месяцев"
        ]
        self.assertEqual(result, expected)

if __name__ == '__main__':
    unittest.main()
