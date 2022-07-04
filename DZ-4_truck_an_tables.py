class Truck:
    tables_list = []
    total = 0
    def __init__ (self, cap):
        self.cap = cap

    def addTable(self, table):
        self.tables_list.append(table)
        self.total += table.mass
        if(self.total > self.cap):
            print("Перевес! Грузоподъемность грузовика: " + str(tr1.cap) + " кг\n")
        else:
            print("Загружен стол массой: " + str(table.mass))

class Table:
    def __init__(self, mass):
        self.mass = mass

tr1 = Truck (150)

T1 = Table(10)
T2 = Table(20)
T3 = Table(30)
T4 = Table(40)
T5 = Table(50)
T6 = Table(60)

listOfTables = [T1, T2, T3, T4, T5, T6]
for table in listOfTables:
    tr1.addTable(table)



