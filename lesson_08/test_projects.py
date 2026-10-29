import uuid


class TestProjects:

    # --- POST /api-v2/projects ---

    def test_create_project_positive(self, api):
        """Позитивный тест: создание проекта с уникальным названием."""
        title = f"New Positive Project {uuid.uuid4().hex[:8]}"
        response = api.create_project(title)

        assert response.status_code == 201
        data = response.json()
        assert "id" in data

        get_resp = api.get_project(data["id"])
        assert get_resp.json()["title"] == title

        api.update_project(data["id"], deleted=True)

    def test_create_project_negative_empty_title(self, api):
        """Негативный тест: создание проекта с пустым названием."""
        response = api.create_project("")

        assert response.status_code == 400
        body = response.text.lower()
        assert "error" in body or "title" in body

    # --- PUT /api-v2/projects/{id} ---

    def test_update_project_positive(self, api, created_project):
        """Позитивный тест: обновление названия существующего проекта."""
        project_id = created_project
        new_title = f"Updated Title {uuid.uuid4().hex[:8]}"

        response = api.update_project(project_id, title=new_title)

        assert response.status_code == 200
        get_resp = api.get_project(project_id)
        assert get_resp.json()["title"] == new_title

    def test_update_project_negative_not_found(self, api):
        """Негативный тест: обновление несуществующего проекта."""
        fake_id = "00000000-0000-0000-0000-000000000000"
        response = api.update_project(fake_id, title="Does not matter")

        assert response.status_code == 404
        body = response.text.lower()
        assert "error" in body or "not found" in body

    # --- GET /api-v2/projects/{id} ---

    def test_get_project_positive(self, api, created_project):
        """Позитивный тест: получение созданного проекта."""
        project_id = created_project

        response = api.get_project(project_id)

        assert response.status_code == 200
        data = response.json()
        assert data["id"] == project_id
        assert "title" in data

    def test_get_project_negative_invalid_id(self, api):
        """Негативный тест: запрос проекта с некорректным ID."""
        invalid_id = "invalid-uuid-string"
        response = api.get_project(invalid_id)

        assert response.status_code in [400, 404]
        body = response.text.lower()
        assert "error" in body or "not found" in body
