from contextlib import redirect_stdout
from io import StringIO
import unittest
from app.domain.models.task import Task
from app.presentation.cli.menu_displayer import MenuDisplayer


class MenuDisplayerTest(unittest.TestCase):

    def setUp(self):
        self.displayer = MenuDisplayer()

    def test_show_menu(self):
        options = {
            "1": "Option A",
            "2": "Option B"
        }
        expected_output = "\n=== MENU ===\n1. Option A\n2. Option B\n============\n"

        with StringIO() as buf, redirect_stdout(buf):
            self.displayer.show(options)
            output = buf.getvalue()
        
        self.assertEqual(output, expected_output)

    def test_show_tasks(self):
        tasks = [
            Task(id=1, title="Task 1", resume="Résumé 1"),
            Task(id=2, title="Task 2", resume="Résumé 2")
        ]
        expected_output = (
            "→ 1: Task 1: Résumé 1\n"
            "→ 2: Task 2: Résumé 2\n"
        )

        with StringIO() as buf, redirect_stdout(buf):
            self.displayer.show_tasks(tasks)
            output = buf.getvalue()

        self.assertEqual(output, expected_output)

    def test_show_error(self):
        message = "Une erreur s'est produite"
        expected_output = "⚠️ Une erreur s'est produite\n"

        with StringIO() as buf, redirect_stdout(buf):
            self.displayer.show_error(message)
            output = buf.getvalue()

        self.assertEqual(output, expected_output)