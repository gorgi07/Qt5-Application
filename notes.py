import sqlite3
from colorama import Fore


def get_id_list(db_name) -> list[int] | None:
    """
    Функция для получения id всех записей в базе данных
    """
    data_base = sqlite3.connect(db_name)
    cur = data_base.cursor()
    try:
        cur.execute("BEGIN")
        data = cur.execute("""SELECT id FROM notes""").fetchall()
        cur.execute("COMMIT")
        new_data = [x[0] for x in data]
        print(Fore.LIGHTGREEN_EX + "[УСПЕХ] Данные получены")
        return new_data
    except:
        cur.execute("ROLLBACK")
        print(Fore.RED + "[ОШИБКА] Не удалось получить записи")
        return None
    finally:
        data_base.commit()
        data_base.close()


def get_note(db_name, note_id) -> tuple | None:
    """
    Функция для получения заметки по id
    """
    data_base = sqlite3.connect(db_name)
    cur = data_base.cursor()
    try:
        cur.execute("BEGIN")
        data = cur.execute("""SELECT title, content FROM notes WHERE id = ?""",
                           (note_id, )).fetchone()
        cur.execute("COMMIT")
        print(Fore.LIGHTGREEN_EX + "[УСПЕХ] Данные получены")
        return data
    except:
        cur.execute("ROLLBACK")
        print(Fore.RED + "[ОШИБКА] Не удалось получить запись "
                         "(ID не существует)")
        return None
    finally:
        data_base.commit()
        data_base.close()


def get_notes_for_table(db_name) -> list[tuple] | None:
    """
    Функция для получения данных (id и название) для заполнения таблицы
    """
    data_base = sqlite3.connect(db_name)
    cur = data_base.cursor()
    try:
        cur.execute("BEGIN")
        data = cur.execute("""SELECT id, title FROM notes""").fetchall()
        cur.execute("COMMIT")
        print(Fore.LIGHTGREEN_EX + "[УСПЕХ] Данные для таблицы получены")
        return data
    except:
        cur.execute("ROLLBACK")
        print(Fore.RED + "[ОШИБКА] Не удалось получить данные для таблицы")
        return None
    finally:
        data_base.commit()
        data_base.close()


def find_missing_id(db_name) -> int | None:
    """
    Функция для поиска id, которого ещё нет в базе данных
    """
    data_base = sqlite3.connect(db_name)
    cur = data_base.cursor()
    try:
        cur.execute("BEGIN")
        id_list = cur.execute("""SELECT id FROM notes""").fetchall()
        cur.execute("COMMIT")

        new_id_list = list()
        for element in id_list:
            if not (element[0] is None):
                new_id_list.append(element[0])

        for i in range(1, max(new_id_list) + 1):
            if not (i in new_id_list):
                new_id = i
                break
        else:
            new_id = max(new_id_list) + 1
        print(Fore.LIGHTGREEN_EX + "[УСПЕХ] Новый ID найден")
        return new_id
    except:
        cur.execute("ROLLBACK")
        print(Fore.RED + "[ОШИБКА] Не удалось найти новый ID")
        return None
    finally:
        data_base.commit()
        data_base.close()


def create_note(db_name, new_id, title, content) -> None:
    """
    Функция для добавления заметки в базу данных
    """
    data_base = sqlite3.connect(db_name)
    cur = data_base.cursor()
    try:
        cur.execute("BEGIN")
        cur.execute(
            """INSERT INTO notes(id, title, content) VALUES(?, ?, ?)""",
            (new_id, title, content))
        cur.execute("COMMIT")
        print(Fore.LIGHTGREEN_EX + "[УСПЕХ] Запись добавлена в БД")
    except:
        cur.execute("ROLLBACK")
        print(Fore.RED + "[ОШИБКА] Не удалось добавить запись в БД")
    finally:
        data_base.commit()
        data_base.close()


def edit_note(db_name, previous_id, new_title="", new_content="") -> None:
    """
    Функция для редактирования заметки в базе данных
    """
    data_base = sqlite3.connect(db_name)
    cur = data_base.cursor()
    try:
        title, content = cur.execute("""SELECT title, 
        content FROM notes WHERE id = ?""", (previous_id,)).fetchone()

        if not new_title:
            new_title = title
        if not new_content:
            new_content = content

        try:
            cur.execute("BEGIN")
            cur.execute("""UPDATE notes 
            SET title = ?, content = ? WHERE id = ?""",
                        (new_title, new_content, previous_id))
            cur.execute("COMMIT")
            print(Fore.LIGHTGREEN_EX + f"[УСПЕХ] Запись {previous_id} "
                                       f"изменена")
        except:
            cur.execute("ROLLBACK")
            print(Fore.RED + f"[ОШИБКА] Не удалось изменить запись "
                             f"{previous_id}")
    except:
        print(Fore.RED + "[ОШИБКА] Непредвиденная ошибка")
    finally:
        data_base.commit()
        data_base.close()


def delete_note(db_name, previous_id) -> None:
    """
    Функция для удаления заметки из базы данных
    """
    data_base = sqlite3.connect(db_name)
    cur = data_base.cursor()
    try:
        cur.execute("BEGIN")
        cur.execute("DELETE FROM notes WHERE id = ?", (previous_id,))
        cur.execute("COMMIT")
        print(Fore.LIGHTGREEN_EX + f"[УСПЕХ] Запись {previous_id} удалена")
    except:
        cur.execute("ROLLBACK")
        print(Fore.RED + f"[ОШИБКА] Не удалось удалить запись {previous_id}")
    finally:
        data_base.commit()
        data_base.close()


