from unittest import TestCase, main
from project.student import Student


class TestStudent(TestCase):
    def setUp(self):
        self.student = Student("Manol")

    def test_attr_are_set(self):
        self.assertEqual("Manol", self.student.name)
        self.assertEqual({}, self.student.courses)

    def test_enroll_course_with_notes(self):
        result = self.student.enroll("Python OOP", ["Inheritance", "Solid"])
        self.assertEqual(1, len(self.student.courses))
        self.assertEqual(2, len(self.student.courses["Python OOP"]))
        self.assertEqual("Course and course notes have been added.", result)

    def test_enroll_course_with_notes_without_saving_them(self):
        result = self.student.enroll("Python OOP", ["Inheritance", "Solid"], "N")
        self.assertEqual(1, len(self.student.courses))
        self.assertEqual(0, len(self.student.courses["Python OOP"]))
        self.assertEqual("Course has been added.", result)

    def test_enroll_add_notes_to_existing_course(self):
        # Add course and notes to this student
        result = self.student.enroll("Python OOP", ["Inheritance", "Solid"])
        self.assertEqual(1, len(self.student.courses))
        self.assertEqual(2, len(self.student.courses["Python OOP"]))
        self.assertEqual("Course and course notes have been added.", result)

        # Test if new notes area appended to existing course
        result = self.student.enroll("Python OOP", ["ABC", "Testing"])
        self.assertEqual(1, len(self.student.courses))
        self.assertEqual(4, len(self.student.courses["Python OOP"]))
        self.assertEqual("Course already added. Notes have been updated.", result)

    def test_add_notes_not_existing_course_raises(self):
        with self.assertRaises(Exception) as ex:
            self.student.add_notes("Python OOP", ['ABC', 'BCD'])
        self.assertEqual("Cannot add notes. Course not found.", str(ex.exception))

    def test_add_notes_to_existing_course(self):
        # Add course and notes to student
        result = self.student.enroll("Python OOP", ["Inheritance", "Solid"])
        self.assertEqual(1, len(self.student.courses))
        self.assertEqual(2, len(self.student.courses["Python OOP"]))
        self.assertEqual("Course and course notes have been added.", result)

        # Test notes are added
        result = self.student.add_notes("Python OOP", "Testing")
        self.assertEqual("Notes have been updated", result)
        self.assertEqual(3, len(self.student.courses["Python OOP"]))

    def test_leave_course_remove_unexisting_course_raises(self):
        with self.assertRaises(Exception) as ex:
            self.student.leave_course("Python OOP")
        self.assertEqual("Cannot remove course. Course not found.", str(ex.exception))

    def test_leave_existing_course(self):
        # Add course to student
        result = self.student.enroll("Python OOP", ["Inheritance", "Solid"])
        self.assertEqual(1, len(self.student.courses))
        self.assertEqual(2, len(self.student.courses["Python OOP"]))
        self.assertEqual("Course and course notes have been added.", result)

        # Remove course
        result = self.student.leave_course("Python OOP")
        self.assertEqual("Course has been removed", result)
        self.assertEqual(0, len(self.student.courses))


if __name__ == '__main__':
    main()
