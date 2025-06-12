import datetime
import unittest
from unittest.mock import MagicMock
from app.controller.task_controller import TaskController
from app.domain.models.task import Task
from app.domain.services.task_service import TaskService
from app.dto.requests.create_task_request import CreateTaskRequest
from app.dto.requests.update_task_request import UpdateTaskRequest
from app.mappers.task_mapper import TaskMapper



class TestTaskController(unittest.TestCase):
    def setUp(self):
        self.mock_service = MagicMock(spec=TaskService)
        self.controller = TaskController(task_service=self.mock_service)

    def test_create_new_task_calls_service(self):
        test_request = CreateTaskRequest(title="Test", resume="resume_test")
        self.controller.create_new_task(test_request)
        self.mock_service.execute_task_creation.assert_called_once_with(test_request)

    def test_update_task_calls_service(self):
        test_request = UpdateTaskRequest(id=1, title="Updated", resume="resume_test", creation_date=datetime.datetime.now(), is_done=False)
        self.controller.update_task(test_request)
        self.mock_service.execute_update_task.assert_called_once_with(test_request)

    def test_get_one_task_returns_service_value(self):
        expected_task = Task(id=1, title="Test")
        self.mock_service.get_task.return_value = expected_task
        
        result = self.controller.get_one_task(1)
        self.assertEqual(result, expected_task)
        self.mock_service.get_task.assert_called_once_with(1)

    def test_get_all_tasks_returns_service_value(self):
        expected_tasks = [Task(id=1), Task(id=2)]
        self.mock_service.get_tasks.return_value = expected_tasks
        
        result = self.controller.get_all_tasks()
        self.assertEqual(result, expected_tasks)

    def test_delete_task_calls_service(self):
        test_task = Task(id=1)
        self.controller.delete_task(test_task)
        self.mock_service.execute_delete_task.assert_called_once_with(test_task)

    def test_close_db_calls_service(self):
        self.controller.close_db()
        self.mock_service.close_data_base.assert_called_once()