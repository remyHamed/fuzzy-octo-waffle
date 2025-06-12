import unittest
from unittest.mock import MagicMock, patch

from app.app import App


class AppTest(unittest.TestCase):
    def setUp(self):
        self.app = App()
        self.app.menu_main.display_tasks = MagicMock()
        self.app.menu_main.display_menu = MagicMock()
        self.app.menu_main.get_input = MagicMock()
        self.app.menu_main.input_matcher = MagicMock()

    def test_run_stops_on_input_matcher_false(self):
        self.app.menu_main.get_input.return_value = "4"
        self.app.menu_main.input_matcher.return_value = False

        with patch("builtins.print") as mock_print:
            self.app.run()

        self.app.menu_main.display_tasks.assert_called_once()
        self.app.menu_main.display_menu.assert_called_once()
        self.app.menu_main.get_input.assert_called_once_with("taper votre commande\n")
        self.app.menu_main.input_matcher.assert_called_once_with("4")
        mock_print.assert_called_with("fin")

    def test_run_multiple_iterations(self):
        self.app.menu_main.get_input.side_effect = ["1", "4"]
        self.app.menu_main.input_matcher.side_effect = [True, False]

        with patch("builtins.print") as mock_print:
            self.app.run()

        self.assertEqual(self.app.menu_main.display_tasks.call_count, 2)
        self.assertEqual(self.app.menu_main.display_menu.call_count, 2)
        self.assertEqual(self.app.menu_main.get_input.call_count, 2)
        self.assertEqual(self.app.menu_main.input_matcher.call_count, 2)
        mock_print.assert_called_with("fin")