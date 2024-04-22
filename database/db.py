import sqlite3


class Database:
    """
    Database to manage required
    datas on alerting system
    """

    def __init__(self):
        self.connection = sqlite3.connect(".session/job_call.db")
        self.cursor = self.connection.cursor()
        self.cursor.execute("""
            CREATE TABLE IF NOT EXISTS jobinja (
                id INTEGER PRIMARY KEY AUTOINCREMENT,
                title TEXT NOT NULL,
                category TEXT,
                salary INTEGER,
                location TEXT,
                description TEXT,
                date TEXT
            )""")
        self.cursor.execute("""
            CREATE TABLE IF NOT EXISTS linkedin (
                id INTEGER PRIMARY KEY AUTOINCREMENT,
                title TEXT NOT NULL,
                category TEXT,
                country TEXT,
                description TEXT,
                date TEXT)
            """)
        self.cursor.execute("""
            CREATE TABLE IF NOT EXISTS alert (
                id INTEGER PRIMARY KEY AUTOINCREMENT,
                system TEXT NOT NULL
            )""")

    def set_alert_system(self, alert: str) -> bool:
        just_once = self.cursor.execute("SELECT * FROM alert")
        response = just_once.fetchone()
        if response:
            self.cursor.execute(f"UPDATE alert set system = {alert} where id = 1")
        else:
            self.cursor.execute(f"INSERT INTO alert (system) VALUES ('{alert}')")
            self.connection.commit()

    def get_alert_system(self) -> str:
        response = self.cursor.execute("SELECT * FROM alert WHERE ROWID IN (SELECT max(ROWID) FROM alert)")
        return response.fetchone()

    def insert_new_related_job_jobinja(self, title: str, category: str,
                               salary: str, location, description: str, date: str):
        self.cursor.execute(f"""INSERT INTO jobinja (title, category, salary, location, description, date) VALUES 
                            ('{title}', '{category}', '{salary}', '{location}', '{description}', '{date}')""")
        self.connection.commit()

    def insert_new_related_job_linkedin(self, title: str, category: str,
                               country: str, description: str, date: str):
        self.cursor.execute(f"""INSERT INTO linkedin (title, category, country, description, date) VALUES 
                            ('{title}', '{category}', '{country}', '{description}', '{date}')""")
        self.connection.commit()

    def get_related_job_jobinja(self, id: int):
        response = self.cursor.execute(f"SELECT * FROM jobinja WHERE id={id}")
        return response.fetchone()

    def get_related_job_linkedin(self, id: int):
        response = self.cursor.execute(f"SELECT * FROM linkedin WHERE id={id}")
        return response.fetchone()

    def get_all_related_jobs_jobinja(self):
        response = self.cursor.execute(f"SELECT * FROM jobinja")
        return response.fetchall()

    def get_all_related_jobs_linkedin(self):
        response = self.cursor.execute(f"SELECT * FROM linkedin")
        return response.fetchall()


db = Database()
