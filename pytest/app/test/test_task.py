import pytest
from app import Task, DueDateError
from datetime import datetime, timedelta

@pytest.fixture
def username():
    print(">>> Antes de la prueba")
    yield 'Cody'
    print(">>> Después de la prueba")

@pytest.fixture
def password():
    return 'password'

def test_username(username):
    assert username == 'Cody'

def test_username_and_password(username, password):
    assert username == 'Cody'
    assert password == 'password'


def is_available_to_skip():
    return True
# To run marked tests: pytest app/test/test_task.py -v -m due_date
class TestTask():
    
    @pytest.mark.news
    def test_task(self):
        assert True

    @pytest.mark.news
    @pytest.mark.parametrize(
        'title, description, assigned_to, due_date',
        [
            ("Title 1", "Description 1", "User 1", datetime.now() + timedelta(days=1)),
            ("Title 2", "Description 2", "User 2", datetime.now() + timedelta(days=1)),
            ("Title 3", "Description 3", "User 3", datetime.now() + timedelta(days=1)),
            ("Title 4", "Description 4", "User 4", datetime.now() + timedelta(days=1)),
            ("Title 5", "Description 5", "User 5", datetime.now() + timedelta(days=1)),
            ("Title 6", "Description 6", "User 6", datetime.now() + timedelta(days=1)),
        ]
    )
    def test_new_task(self, title, description, assigned_to, due_date):
        due_date = datetime.now() + timedelta(days=1)
        task = Task(title, description, assigned_to, due_date=due_date)
        assert task.title == title
        assert task.description == description
        assert task.assigned_to == assigned_to
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

    # @pytest.mark.skip(reason='Lo sentimos, la prueba no cumple con los requerimientos')
    @pytest.mark.skipif(is_available_to_skip(), reason='Lo sentimos, la prueba no cumple con los requerimientos')
    def test_skip(self):
        pass