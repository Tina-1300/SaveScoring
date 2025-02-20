import sqlite3 # pour géré les base de donner


# Documentation :
# https://docs.python.org/3/library/sqlite3.html


class MXDBB:
    #Constructeur qui prend en paramètre le nom de la Base de donner 
    def __init__(self, NameBdd):
        self.NameBdd = NameBdd
        self.creat_data_base()

    # Permet de cree la Base de donner si elle existe pas et de configurer ça table avec les champs pseudo et password
    def creat_data_base(self):
        con = sqlite3.connect(self.NameBdd) # users.db
        cursor = con.cursor()
        cursor.execute('''
        CREATE TABLE IF NOT EXISTS users (
            id INTEGER PRIMARY KEY AUTOINCREMENT,
            Site TEXT NOT NULL UNIQUE,
            Score INTEGER NOT NULL,
            Place INTEGER NOT NULL           
        )
        ''')
        con.commit()
        con.close()
   
    def insert_in_data_base(self, Site, Score, Place):
        con = sqlite3.connect(self.NameBdd)
        cursor = con.cursor()
        try:
            cursor.execute('INSERT INTO users (Site, Score, Place) VALUES (?, ?, ?)', (Site, Score, Place))
            con.commit()
        except sqlite3.IntegrityError:
            print("Le nom du site est déjà utiliser")
        finally:
            con.close()

    def read_in_data_base(self):
        con = sqlite3.connect(self.NameBdd)
        cursor = con.cursor()
        cursor.execute("SELECT Site, Score, Place FROM users")
        result = cursor.fetchall()
        return [{'Site': row[0], 'Score': row[1], 'Place': row[2]} for row in result]

    def update_in_data_base_score(self,  Score, Site):
        con = sqlite3.connect(self.NameBdd)
        cursor = con.cursor()
        cursor.execute("UPDATE users SET Score = ? WHERE Site = ?", (Score, Site))
        con.commit()
        con.close()

    def update_in_data_base_place(self,  Place, Site):
        con = sqlite3.connect(self.NameBdd)
        cursor = con.cursor()
        cursor.execute("UPDATE users SET Place = ? WHERE Site = ?", (Place, Site))
        con.commit()
        con.close()

    def p():
        d = {"id": "INTEGER PRIMARY KEY AUTOINCREMENT", "Site": "TEXT NOT NULL UNIQUE"}
        # implémenter cela dans la fonction creat_data_base_table
        # comme cela on peut crée nous même les colomn

    def creat_data_base_table(self, name_table, columns_dico:dict):
        con = sqlite3.connect(self.NameBdd)
        cursor = con.cursor()
        
        cursor.execute(f'''
        CREATE TABLE IF NOT EXISTS {name_table} (
            id INTEGER PRIMARY KEY AUTOINCREMENT,
            Site TEXT NOT NULL UNIQUE,
            Score INTEGER NOT NULL,
            Place INTEGER NOT NULL           
        )
        ''')
        con.commit()
        con.close()



def test(name_table, column:dict):
    
    
    print(f'''
        CREATE TABLE IF NOT EXISTS {name_table} (
            id INTEGER PRIMARY KEY AUTOINCREMENT,
            Site TEXT NOT NULL UNIQUE,
            Score INTEGER NOT NULL,
            Place INTEGER NOT NULL           
        )
        ''')

params = {
    "id": "INTEGER PRIMARY KEY AUTOINCREMENT", 
    "Site": "TEXT NOT NULL UNIQUE", 
    "Score": "INTEGER NOT NULL",
    "Place": "INTEGER NOT NULL"
}




print(params.values())
print(params.keys())