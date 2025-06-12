
import unittest
from unittest.mock import MagicMock, patch

from app.presentation.cli.main_menu import MainMenu


class MainMenuTest(unittest.TestCase):

    def setUp(self):
        self.mock_task_controller = MagicMock()
        self.mock_menu_displayer = MagicMock()
        self.menu = MainMenu(self.mock_task_controller, self.mock_menu_displayer)

    @patch('builtins.input', return_value='1')
    def test_yes_or_not_input_catcher_yes(self, mock_input):
        self.assertTrue(self.menu.yes_or_not_input_catcher("Question ?"))

    @patch('builtins.input', return_value='2')
    def test_yes_or_not_input_catcher_no(self, mock_input):
        self.assertFalse(self.menu.yes_or_not_input_catcher("Question ?"))

    @patch('builtins.input', return_value='Test input')
    def test_get_input(self, mock_input):
        result = self.menu.get_input("Message :")
        self.assertEqual(result, 'Test input')

    def test_display_tasks(self):
        self.mock_task_controller.get_all_tasks.return_value = ['task1', 'task2']
        self.menu.display_tasks()
        self.mock_menu_displayer.show_tasks.assert_called_with(['task1', 'task2'])

    @patch('builtins.input', side_effect=['1', 'Title', 'Description'])
    def test_input_matcher_create_task(self, mock_input):
        result = self.menu.input_matcher('1')
        self.assertTrue(result)
        self.mock_task_controller.create_new_task.assert_called()

    @patch('builtins.input', side_effect=['42', '1', 'Updated title', '2'])
    def test_input_matcher_update_task(self, mock_input):
        task_mock = MagicMock()
        self.mock_task_controller.get_one_task.return_value = task_mock
        result = self.menu.input_matcher('2')
        self.assertTrue(result)
        self.mock_task_controller.update_task.assert_called_with(task_mock)

    @patch('builtins.input', side_effect=['99'])
    def test_input_matcher_delete_task(self, mock_input):
        task_mock = MagicMock()
        self.mock_task_controller.get_one_task.return_value = task_mock
        result = self.menu.input_matcher('3')
        self.assertTrue(result)
        self.mock_task_controller.delete_task.assert_called_with(task_mock)

    @patch('builtins.input', return_value='')
    def test_input_matcher_exit(self, mock_input):
        result = self.menu.input_matcher('4')
        self.assertFalse(result)
        self.mock_task_controller.close_db.assert_called()

    @patch('builtins.input', return_value='')
    def test_input_matcher_default(self, mock_input):
        result = self.menu.input_matcher('invalid')
        self.assertTrue(result)