import sqlite3

FILE_LOC = "..\\data\\savagebot.db3"

class Mydata:
    def __init__(self, file):
        self.filename = file
        self.conn = sqlite3.connect(self.filename)

    def get(self, SQL):
        curs = self.conn.cursor()
        result = curs.execute(SQL).fetchall()
        return result









if __name__ == "__main__":
    source = mydata(FILE_LOC)
    sql = "SELECT * FROM Users WHERE clue>0; "
    clued_in = source.get(sql)
    print("Clued in =", len(clued_in))
