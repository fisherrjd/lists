from .models import User, TodoList, ListItem
import sqlite3

DB_NAME = "todo.db"

def get_connection():
    return sqlite3.connect(DB_NAME)

def init_db():
    conn = get_connection()
    cur = conn.cursor()
    # Users table
    cur.execute("""
        CREATE TABLE IF NOT EXISTS users (
            id TEXT PRIMARY KEY,
            username TEXT UNIQUE NOT NULL
        );
    """)
    # Lists table
    cur.execute("""
        CREATE TABLE IF NOT EXISTS lists (
            id TEXT PRIMARY KEY,
            title TEXT NOT NULL,
            user_id TEXT NOT NULL,
            FOREIGN KEY(user_id) REFERENCES users(id)
        );
    """)
    # List items table
    cur.execute("""
        CREATE TABLE IF NOT EXISTS list_items (
            id TEXT PRIMARY KEY,
            text TEXT NOT NULL,
            completed INTEGER NOT NULL DEFAULT 0,
            list_id TEXT NOT NULL,
            FOREIGN KEY(list_id) REFERENCES lists(id)
        );
    """)
    conn.commit()
    conn.close()

# Call this at app startup
init_db()

def create_user(user: User):
    conn = get_connection()
    cur = conn.cursor()
    cur.execute("INSERT INTO users (id, username) VALUES (?, ?)", (user.id, user.username))
    conn.commit()
    conn.close()

def get_user(user_id: str):
    conn = get_connection()
    cur = conn.cursor()
    cur.execute("SELECT id, username FROM users WHERE id = ?", (user_id,))
    row = cur.fetchone()
    conn.close()
    if row:
        return User(id=row[0], username=row[1])
    return None

def create_list(todo_list: TodoList):
    conn = get_connection()
    cur = conn.cursor()
    cur.execute(
        "INSERT INTO lists (id, title, user_id) VALUES (?, ?, ?)",
        (todo_list.id, todo_list.title, todo_list.user_id)
    )
    conn.commit()
    conn.close()

def get_lists_for_user(user_id: str):
    conn = get_connection()
    cur = conn.cursor()
    cur.execute("SELECT id, title, user_id FROM lists WHERE user_id = ?", (user_id,))
    lists = []
    for row in cur.fetchall():
        items = get_items(row[0])
        lists.append(TodoList(id=row[0], title=row[1], user_id=row[2], items=items))
    conn.close()
    return lists

def get_list(list_id: str):
    conn = get_connection()
    cur = conn.cursor()
    cur.execute("SELECT id, title, user_id FROM lists WHERE id = ?", (list_id,))
    row = cur.fetchone()
    conn.close()
    if row:
        items = get_items(row[0])
        return TodoList(id=row[0], title=row[1], user_id=row[2], items=items)
    return None

def add_item(list_id: str, item: ListItem):
    conn = get_connection()
    cur = conn.cursor()
    cur.execute(
        "INSERT INTO list_items (id, text, completed, list_id) VALUES (?, ?, ?, ?)",
        (item.id, item.text, int(item.completed), list_id)
    )
    conn.commit()
    conn.close()

def get_items(list_id: str):
    conn = get_connection()
    cur = conn.cursor()
    cur.execute("SELECT id, text, completed FROM list_items WHERE list_id = ?", (list_id,))
    items = [ListItem(id=row[0], text=row[1], completed=bool(row[2])) for row in cur.fetchall()]
    conn.close()
    return items

def remove_item(item_id: str):
    conn = get_connection()
    cur = conn.cursor()
    cur.execute("DELETE FROM list_items WHERE id = ?", (item_id,))
    conn.commit()
    conn.close()