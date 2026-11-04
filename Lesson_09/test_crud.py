from sqlalchemy import text


def test_add_student(db_conn):
    # берём свободный user_id, чтобы не пересечься с реальными данными
    user_id = 999001
    try:
        # добавляем студента
        db_conn.execute(
            text(
                "INSERT INTO student "
                "(user_id, level, education_form, subject_id) "
                "VALUES (:user_id, :level, :education_form, :subject_id)"
            ),
            {
                "user_id": user_id,
                "level": "бакалавриат",
                "education_form": "очная",
                "subject_id": 999001,
            },
        )

        # проверяем, что запись появилась
        row = db_conn.execute(
            text(
                "SELECT user_id, level, education_form "
                "FROM student WHERE user_id = :user_id"
            ),
            {"user_id": user_id},
        ).fetchone()

        assert row is not None
        assert row.level == "бакалавриат"
        assert row.education_form == "очная"
    finally:
        # удаляем созданные данные
        db_conn.execute(
            text("DELETE FROM student WHERE user_id = :user_id"),
            {"user_id": user_id},
        )


def test_update_subject(db_conn):
    # создаём предмет
    subject_id = 999002
    try:
        db_conn.execute(
            text(
                "INSERT INTO subject (subject_id, subject_title) "
                "VALUES (:id, :title)"
            ),
            {"id": subject_id, "title": "Старое название"},
        )

        # меняем название предмета
        db_conn.execute(
            text(
                "UPDATE subject SET subject_title = :title "
                "WHERE subject_id = :id"
            ),
            {"title": "Новое название", "id": subject_id},
        )

        # проверяем, что новое имя сохранилось
        new_title = db_conn.execute(
            text(
                "SELECT subject_title FROM subject "
                "WHERE subject_id = :id"
            ),
            {"id": subject_id},
        ).scalar_one()
        assert new_title == "Новое название"
    finally:
        # удаляем созданные данные
        db_conn.execute(
            text("DELETE FROM subject WHERE subject_id = :id"),
            {"id": subject_id},
        )


def test_delete_teacher(db_conn):
    # создаём учителя
    teacher_id = 999003
    try:
        db_conn.execute(
            text(
                "INSERT INTO teacher (teacher_id, email, group_id) "
                "VALUES (:id, :email, :group_id)"
            ),
            {
                "id": teacher_id,
                "email": "test_teacher@example.com",
                "group_id": 999003,
            },
        )

        # удаляем учителя
        db_conn.execute(
            text("DELETE FROM teacher WHERE teacher_id = :id"),
            {"id": teacher_id},
        )

        # проверяем, что его больше нет в базе
        result = db_conn.execute(
            text("SELECT teacher_id FROM teacher WHERE teacher_id = :id"),
            {"id": teacher_id},
        ).fetchone()
        assert result is None
    finally:
        # чистим базу
        db_conn.execute(
            text("DELETE FROM teacher WHERE teacher_id = :id"),
            {"id": teacher_id},
        )
