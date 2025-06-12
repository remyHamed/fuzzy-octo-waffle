import datetime
import unittest
from app.domain.models.task import Task


class TaskTest(unittest.TestCase):

    def test_default_constructor(self):
        task = Task()
        self.assertIsInstance(task, Task)
        self.assertEqual(task.id, None)
        self.assertEqual(task.title, "")
        self.assertEqual(task.resume, "")
        self.assertFalse(task.is_done)
        self.assertIsInstance(task.creation_date, datetime.datetime)

    def test_custom_constructor(self):
        now = datetime.datetime.now()
        task = Task(1, "Title", now, "Résumé", True)
        self.assertEqual(task.id, 1)
        self.assertEqual(task.title, "Title")
        self.assertEqual(task.resume, "Résumé")
        self.assertTrue(task.is_done)
        self.assertEqual(task.creation_date, now)

    def test_setters_and_getters(self):
        task = Task()
        task.id = 10
        task.title = "New Title"
        task.resume = "New Resume"
        task.is_done = True
        new_date = datetime.datetime.now() + datetime.timedelta(days=1)
        task.creation_date = new_date

        self.assertEqual(task.id, 10)
        self.assertEqual(task.title, "New Title")
        self.assertEqual(task.resume, "New Resume")
        self.assertTrue(task.is_done)
        self.assertEqual(task.creation_date, new_date)

    def test_str_method(self):
        task = Task(1, "Test", datetime.datetime(2023, 1, 1), "Résumé", False)
        result = str(task)
        self.assertIn("Task -> id: 1", result)
        self.assertIn("title : Test", result)
        self.assertIn("resume : Résumé", result)
        self.assertIn("is done : False", result)

    def test_repr_method(self):
        date = datetime.datetime(2022, 5, 4)
        task = Task(2, "Titre", date, "Texte", True)
        result = repr(task)
        expected = f"Task(id=2, title='Titre', creation_date={date}, resume='Texte', is_done=True)"
        self.assertEqual(result, expected)

    def test_equality_true(self):
        date = datetime.datetime(2024, 4, 1)
        task1 = Task(1, "Titre", date, "Résumé", False)
        task2 = Task(1, "Titre", date, "Résumé", False)
        self.assertEqual(task1, task2)

    def test_equality_false(self):
        task1 = Task(1, "Titre", datetime.datetime(2023, 1, 1), "Résumé", False)
        task2 = Task(2, "Autre", datetime.datetime(2023, 1, 1), "Texte", True)
        self.assertNotEqual(task1, task2)

    def test_type_errors(self):
        task = Task()

        with self.assertRaises(TypeError):
            task.id = "not an int"

        with self.assertRaises(TypeError):
            task.title = 123

        with self.assertRaises(TypeError):
            task.resume = 456

        with self.assertRaises(TypeError):
            task.creation_date = "2020-01-01"

        with self.assertRaises(TypeError):
            task.is_done = "oui"
