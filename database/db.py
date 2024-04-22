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

def test_insert_new_related_job_jobinja():
    db = Database()
    title = "Django_Developer"
    category = "backend"
    salary = "20.000.000T"
    location = "tehran"
    description = "python,django,SQL needed"
    date = "1402.1.1"

    db.insert_new_related_job_jobinja(title,category,salary,location,description,date)
        
    cursor = db.connection.cursor()
    cursor.execute("SELECT * FROM jobinja WHERE title=?", (title,))
    result = cursor.fetchone()

    if result is not None:
        print("Job inserted successfully:", result)
    else:
        print("Failed to insert job")

    db.connection.close()


def test_get_alert_system():

    database_instance = Database()

    result = database_instance.get_alert_system()

    print("Alert System:", result)

    database_instance.connection.close()

def test_set_alert_system():

    database_instance = Database()

    alert = "Sample alert message"
    database_instance.set_alert_system(alert)

    cursor = database_instance.connection.cursor()
    cursor.execute("SELECT * FROM alert WHERE system=?", (alert,))
    result = cursor.fetchone()

    if result is not None:
        print("Alert system set successfully:", result[0])
    else:
        print("Failed to set alert system")

    database_instance.connection.close()

# Run the test function
if __name__ == "__main__":
    test_get_alert_system()
    test_set_alert_system()
    test_insert_new_related_job_jobinja()