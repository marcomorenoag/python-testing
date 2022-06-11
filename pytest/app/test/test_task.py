import pytest
from app import Task, DueDateError
from datetime import datetime, timedelta

# To run marked tests: pytest app/test/test_task.py -v -m due_date
class TestTask():
    
    @pytest.mark.news
    def test_task(self):
        assert True

    @pytest.mark.news
    def test_new_task(self):
        due_date = datetime.now() + timedelta(days=1)
        task = Task('Title', 'Description', 'marco', due_date=due_date)
        assert task.title == 'Title'
        assert task.description == 'Description'
        assert task.assigned_to == 'marco'
        assert task.due_date == due_date

    @pytest.mark.due_date
    @pytest.mark.errors
    def test_due_date_error(self):
        with pytest.raises(DueDateError):
            due_date = datetime.now() - timedelta(days=1)
            Task('Title1', 'Description1', 'marco1', due_date=due_date)

    @pytest.mark.due_date
    def test_due_date(self):
        due_date = datetime.now() + timedelta(days=1)
        task = Task('Title2', 'Description2', 'marco2', due_date=due_date)
        assert task.due_date > datetime.now()