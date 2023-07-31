import sqlite3
DATABASE_FILE = r"C:\New folder\MyComputerAssistant\savedCommands.db"

class DatabaseHandler(object):

    def create_table_if_not_exists():
        conn = sqlite3.connect(DATABASE_FILE)
        cursor = conn.cursor()

        cursor.execute('''CREATE TABLE IF NOT EXISTS saved_commands (
                            id INTEGER PRIMARY KEY AUTOINCREMENT,
                            command TEXT NOT NULL,
                            input TEXT NOT NULL
                        )''')

        conn.commit()
        conn.close()

    def create_table():
        conn = sqlite3.connect(DATABASE_FILE)
        cursor = conn.cursor()

        cursor.execute('''CREATE TABLE IF NOT EXISTS saved_commands (
                            id INTEGER PRIMARY KEY AUTOINCREMENT,
                            command TEXT NOT NULL,
                            input TEXT NOT NULL
                        )''')

        conn.commit()
        conn.close()

    def insert_command(command, audio_input):
        conn = sqlite3.connect(DATABASE_FILE)
        cursor = conn.cursor()

        cursor.execute("INSERT INTO saved_commands (command, input) VALUES (?, ?)", (command, audio_input))
        conn.commit()

        conn.close()

    def find_command_by_input(audio_input):
        conn = sqlite3.connect(DATABASE_FILE)
        cursor = conn.cursor()

        cursor.execute("SELECT command FROM saved_commands WHERE input = ?", (audio_input,))
        result = cursor.fetchone()

        conn.close()

        return result[0] if result else None




