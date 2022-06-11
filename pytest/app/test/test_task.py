import pytest
from app import Task, DueDateError
from datetime import datetime, timedelta

class TestTask():
    
    def test_task(self):
        assert True

    def test_new_task(self):
        due_date = datetime.now() + timedelta(days=1)
        task = Task('Title', 'Description', 'marco', due_date=due_date)
        assert task.title == 'Title'
        assert task.description == 'Description'
        assert task.assigned_to == 'marco'
        assert task.due_date == due_date

    def test_due_date_error(self):
        with pytest.raises(DueDateError):
            due_date = datetime.now() - timedelta(days=1)
            Task('Title1', 'Description1', 'marco1', due_date=due_date)