import unittest
from classroom_organizer import ClassroomOrganizer

class TestClassroomOrganizer(unittest.TestCase):
    def setUp(self):
        self.classroom = ClassroomOrganizer()
        self.student_roster = [
            {'name': 'Alice', 'favorite_subject': 'Math'},
            {'name': 'Bob', 'favorite_subject': 'Science'},
            {'name': 'Charlie', 'favorite_subject': 'Math'},
            {'name': 'David', 'favorite_subject': 'English'},
            {'name': 'Eve', 'favorite_subject': 'Science'}
        ]

    def test_sort_alphabetically(self):
        sorted_names = ['Alice', 'Bob', 'Charlie', 'David', 'Eve']
        self.assertEqual(self.classroom._sort_alphabetically(self.student_roster), sorted_names)

    def test_get_students_with_subject(self):
        math_lovers = [('Alice', 'Math'), ('Charlie', 'Math')]
        self.assertEqual(self.classroom.get_students_with_subject('Math'), math_lovers)

    def test_iterator(self):
        sorted_names = ['Alice', 'Bob', 'Charlie', 'David', 'Eve']
        for student in self.classroom:
            self.assertEqual(student, sorted_names.pop(0))

    def test_get_table_arrangements(self):
        pairs = [('Alice', 'Bob'), ('Alice', 'Charlie'), ('Alice', 'David'), ('Alice', 'Eve'), ('Bob', 'Charlie'), ('Bob', 'David'), ('Bob', 'Eve'), ('Charlie', 'David'), ('Charlie', 'Eve'), ('David', 'Eve')]
        self.assertEqual(self.classroom.get_table_arrangements(), pairs)

if __name__ == '__main__':
    unittest.main()