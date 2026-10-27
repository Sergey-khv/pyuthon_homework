import pytest
from api_client import YougileApi


@pytest.fixture
def api():
    return YougileApi()


@pytest.fixture
def created_project(api):
    """Создает проект и удаляет его после теста."""
    response = api.create_project("Test Project for Homework")
    assert response.status_code == 201, f"Не удалось создать проект: {
        response.text}"
    project_id = response.json()["id"]

    yield project_id

    # Очистка: помечаем проект как удаленный
    api.update_project(project_id, deleted=True)
