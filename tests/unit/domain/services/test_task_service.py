import pytest
from datetime import datetime
from unittest.mock import Mock, patch
from app.domain.models.task import Task
from app.dto.requests.create_task_request import CreateTaskRequest
from app.dto.requests.update_task_request import UpdateTaskRequest
from app.domain.services.task_service import TaskService

class TestTaskService:
    @pytest.fixture
    def mock_repo(self):
        return Mock()

    @pytest.fixture
    def sample_task(self):
        return Task(
            id=1,
            title="Test Task",
            creation_date=datetime(2023, 1, 1),
            resume="Sample resume",
            is_done=False
        )


    def test_create_task_success(self, mock_repo, sample_task):
        #setting
        service = TaskService(mock_repo)
        create_request = CreateTaskRequest(title="Test Task", resume="Sample resume")
        

        mock_repo.save_task.return_value = sample_task

        #test
        result = service.execute_task_creation(create_request)


        assert result == sample_task
        mock_repo.save_task.assert_called_once()
        args, _ = mock_repo.save_task.call_args
        saved_task = args[0]
        assert saved_task.title == "Test Task"
        assert saved_task.resume == "Sample resume"
        assert saved_task.id is None 
        assert isinstance(saved_task.creation_date, datetime)

    def test_create_task_empty_title(self, mock_repo):

        service = TaskService(mock_repo)
        create_request = CreateTaskRequest(title="", resume="Invalid")


        with pytest.raises(ValueError, match="Le titre ne peut pas être vide"):
            service.execute_task_creation(create_request)
        mock_repo.save_task.assert_not_called()


    def test_update_task_success(self, mock_repo, sample_task):

        service = TaskService(mock_repo)
        update_request = UpdateTaskRequest(
            id=1,
            title="Updated Title",
            creation_date=datetime(2023, 1, 1),
            resume="Updated resume",
            is_done=True
        )
        mock_repo.update_task.return_value = sample_task


        result = service.execute_update_task(update_request)


        assert result == sample_task
        mock_repo.update_task.assert_called_once()
        updated_task = mock_repo.update_task.call_args[0][0]
        assert updated_task.title == "Updated Title"
        assert updated_task.is_done is True

    def test_get_task_found(self, mock_repo, sample_task):
        
        service = TaskService(mock_repo)
        mock_repo.get_task.return_value = sample_task


        result = service.get_task(1)

   
        assert result == sample_task
        mock_repo.get_task.assert_called_once_with(1)

    def test_get_task_not_found(self, mock_repo):
        
        service = TaskService(mock_repo)
        mock_repo.get_task.return_value = None


        result = service.get_task(999)

   
        assert result is None

    def test_get_tasks_with_results(self, mock_repo, sample_task):
        
        service = TaskService(mock_repo)
        mock_repo.get_all_tasks.return_value = [sample_task]


        result = service.get_tasks()

   
        assert len(result) == 1
        assert result[0] == sample_task

    def test_get_tasks_empty(self, mock_repo):
        
        service = TaskService(mock_repo)
        mock_repo.get_all_tasks.return_value = []


        result = service.get_tasks()

   
        assert result == []

    def test_delete_task(self, mock_repo, sample_task):
        
        service = TaskService(mock_repo)


        service.execute_delete_task(sample_task)

   
        mock_repo.execute_delete_task.assert_called_once_with(sample_task)

    def test_close_database(self, mock_repo):
        
        service = TaskService(mock_repo)


        service.close_data_base()

   
        mock_repo.close.assert_called_once()

    def test_update_task_empty_title(self, mock_repo):
        service = TaskService(mock_repo)
        update_request = UpdateTaskRequest(
            id=1,
            title="",
            creation_date=datetime(2023, 1, 1),
            resume="Updated resume",
            is_done=True
        )


        with pytest.raises(ValueError, match="Le titre ne peut pas être vide"):
            service.execute_update_task(update_request)
        
    def test_delete_nonexistent_task(self, mock_repo, sample_task):
        service = TaskService(mock_repo)
        mock_repo.execute_delete_task.side_effect = ValueError("Tâche non trouvée")

        with pytest.raises(ValueError, match="Tâche non trouvée"):
            service.execute_delete_task(sample_task)

    def test_delete_nonexistent_task(self, mock_repo, sample_task):
        service = TaskService(mock_repo)
        mock_repo.execute_delete_task.side_effect = ValueError("Tâche non trouvée")

        with pytest.raises(ValueError, match="Tâche non trouvée"):
            service.execute_delete_task(sample_task)

    def test_get_tasks_return_type(self, mock_repo):
        service = TaskService(mock_repo)
        mock_repo.get_all_tasks.return_value = []

        result = service.get_tasks()

        assert isinstance(result, list)

    def test_create_task_title_spaces_only(self, mock_repo):
        service = TaskService(mock_repo)
        create_request = CreateTaskRequest(title="   ", resume="Résumé")

        with pytest.raises(ValueError, match="Le titre ne peut pas être vide"):
            service.execute_task_creation(create_request)

    def test_create_task_returns_task_instance(self, mock_repo, sample_task):
        service = TaskService(mock_repo)
        mock_repo.save_task.return_value = sample_task
        create_request = CreateTaskRequest(title="Test", resume="Résumé")

        result = service.execute_task_creation(create_request)

        assert isinstance(result, Task)




