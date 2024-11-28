from PyQt6.QtCore import QSize
from PyQt6.QtCore import Qt
from PyQt6.QtWidgets import QApplication, QPushButton, QVBoxLayout, QWidget, QLabel, QMainWindow, QHBoxLayout, QLineEdit, QGridLayout, QHeaderView
from PyQt6 import QtCore, QtGui, QtWidgets
import pandas as pd


#Отрисовка таблицы
class TableModel(QtCore.QAbstractTableModel):
    def __init__(self, data):
        super().__init__()
        self._data = data

    def data(self, index, role):
        if role == Qt.ItemDataRole.DisplayRole:
            value = self._data.iloc[index.row(), index.column()]
            return str(value)

    def rowCount(self, index):
        return self._data.shape[0]

    def columnCount(self, index):
        return self._data.shape[1]

    def headerData(self, section, orientation, role):
        if role == Qt.ItemDataRole.DisplayRole:
            if orientation == Qt.Orientation.Horizontal:
                return str(self._data.columns[section])

            if orientation == Qt.Orientation.Vertical:
                return str(self._data.index[section])
            

#Добавление образования
class educationsWindowAdding(QWidget):
    def __init__(self):
        super().__init__()
        self.setWindowTitle("Добавление образования")
        layoutInputsAndLabels = QGridLayout()
        layoutBtns = QHBoxLayout()
        layoutItems = QVBoxLayout()
        layout = QHBoxLayout()
        self.inputName = QLineEdit()
        btnAdd = QPushButton(text = "Добавить")
        btnAdd.setFixedSize(170, 30)
        labelName = QLabel("Название образования(строка)", )
        labelStatus = QLabel()
        labelStatus.setFixedHeight(45)
        layoutInputsAndLabels.addWidget(labelName, 0,0)
        layoutInputsAndLabels.addWidget(self.inputName, 1,0)
        layoutBtns.addWidget(btnAdd)
        layoutItems.addLayout(layoutInputsAndLabels)
        layoutItems.addLayout(layoutBtns)
        layoutItems.addWidget(labelStatus)
        self.table = QtWidgets.QTableView()
        clmns = ["Код образования", "Название"]
        lst = [
          [1, 9],
          [1, 0],
          [3, 5],
        ]
        data = pd.DataFrame(lst, index = range(1,len(lst) + 1), columns = clmns)
        self.model = TableModel(data)
        self.table.setModel(self.model)
        layout.addLayout(layoutItems)
        layout.addWidget(self.table)
        self.setLayout(layout)

        btnAdd.clicked.connect(self.adding)
    def adding(self):
        textName = self.inputName.text()
        self.inputName.clear()

#Удаление образования
class educationsWindowDeletion(QWidget):
    def __init__(self):
        super().__init__()
        self.setWindowTitle("Удаление образования")
        layoutInputsAndLabels = QGridLayout()
        layoutBtns = QHBoxLayout()
        layout = QHBoxLayout()
        layoutItems = QVBoxLayout()
        self.inputId = QLineEdit()
        btnDel = QPushButton(text = "Удалить")
        btnDel.setFixedSize(170, 30)
        labelId = QLabel("Код образования(число)", )
        labelStatus = QLabel()
        labelStatus.setFixedHeight(45)
        layoutInputsAndLabels.addWidget(labelId, 0,0)
        layoutInputsAndLabels.addWidget(self.inputId, 1,0)
        layoutBtns.addWidget(btnDel)
        layoutItems.addLayout(layoutInputsAndLabels)
        layoutItems.addLayout(layoutBtns)
        layoutItems.addWidget(labelStatus)
        self.table = QtWidgets.QTableView()
        clmns = ["Код образования", "Название"]
        lst = [
          [1, 9],
          [1, 0],
          [3, 5],
        ]
        data = pd.DataFrame(lst, index = range(1,len(lst) + 1), columns = clmns)
        self.model = TableModel(data)
        self.table.setModel(self.model)
        layout.addLayout(layoutItems)
        layout.addWidget(self.table)
        self.setLayout(layout)

        btnDel.clicked.connect(self.deletion)
    def deletion(self):
        print()

#Изменение образования
class educationsWindowChanging(QWidget):
    def __init__(self):
        super().__init__()
        self.setWindowTitle("Изменение образований")
        layoutInputsAndLabels = QGridLayout()
        layoutBtns = QHBoxLayout()
        layoutItems = QVBoxLayout()
        layout = QHBoxLayout()
        self.inputIdOld = QLineEdit()
        self.inputIdNew = QLineEdit()
        self.inputNameNew = QLineEdit()
        btnChange = QPushButton(text = "Изменить")
        btnChange.setFixedSize(170, 30)
        labelIdNew = QLabel("Код образования(число)", )
        labelNameNew = QLabel("Название образования(строка) новое", )
        labelStatus = QLabel()
        labelStatus.setFixedHeight(45)
        layoutInputsAndLabels.addWidget(labelIdNew, 2,0)
        layoutInputsAndLabels.addWidget(labelNameNew, 2,1)
        layoutInputsAndLabels.addWidget(self.inputIdNew, 3,0)
        layoutInputsAndLabels.addWidget(self.inputNameNew, 3,1)
        layoutBtns.addWidget(btnChange)
        layoutItems.addLayout(layoutInputsAndLabels)
        layoutItems.addLayout(layoutBtns)
        layoutItems.addWidget(labelStatus)
        self.table = QtWidgets.QTableView()
        clmns = ["Код образования", "Название"]
        lst = [
          [1, 9],
          [1, 0],
          [3, 5],
        ]
        data = pd.DataFrame(lst, index = range(1,len(lst) + 1), columns = clmns)
        self.model = TableModel(data)
        self.table.setModel(self.model)
        layout.addLayout(layoutItems)
        layout.addWidget(self.table)
        self.setLayout(layout)

        btnChange.clicked.connect(self.changing)
    def changing(self):
        print()

#Главное окно по образованию     
class educationsWindow(QWidget):
    def __init__(self):
        super().__init__()
        self.setFixedSize(QSize(450, 400))
        self.setWindowTitle("Образование")
        btnAddEducations = QPushButton(text = "Добавить образование")
        btnAddEducations.setFixedSize(170, 60)
        btnRemoveEducations = QPushButton(text = "Удалить образование")
        btnRemoveEducations.setFixedSize(170, 60)
        btnEditEducations = QPushButton(text = "Изменить образование")
        btnEditEducations.setFixedSize(170, 60)
        layoutItems = QVBoxLayout()
        layout = QHBoxLayout()
        layoutItems.addWidget(btnAddEducations)
        layoutItems.addWidget(btnRemoveEducations)
        layoutItems.addWidget(btnEditEducations)
        self.table = QtWidgets.QTableView()
        clmns = ["Код образования", "Тип"]
        lst = [
          [1, 9],
          [1, 0],
          [3, 5],
        ]
        data = pd.DataFrame(lst, index = range(1,len(lst) + 1), columns = clmns)
        self.model = TableModel(data)
        self.table.setModel(self.model)
        layout.addLayout(layoutItems)
        layout.addWidget(self.table)
        self.setLayout(layout)
        
        btnAddEducations.clicked.connect(self.show_education_adding_window)
        btnRemoveEducations.clicked.connect(self.show_education_deletion_window)
        btnEditEducations.clicked.connect(self.show_education_changing_window)
    def show_education_adding_window(self):
        self.educationsAdding = educationsWindowAdding()
        self.educationsAdding.show()
    def show_education_deletion_window(self):
        self.educationDeletion = educationsWindowDeletion()
        self.educationDeletion.show()
    def show_education_changing_window(self):
        self.educationChanging = educationsWindowChanging()
        self.educationChanging.show()


#Добавление отделения
class unitsWindowAdding(QWidget):
    def __init__(self):
        super().__init__()
        self.setWindowTitle("Добавление отделения")
        layoutInputsAndLabels = QGridLayout()
        layoutBtns = QHBoxLayout()
        layoutItems = QVBoxLayout()
        layout = QHBoxLayout()
        self.inputName = QLineEdit()
        btnAdd = QPushButton(text = "Добавить")
        btnAdd.setFixedSize(170, 30)
        labelName = QLabel("Отделения(строка)", )
        labelStatus = QLabel()
        labelStatus.setFixedHeight(45)
        layoutInputsAndLabels.addWidget(labelName, 0,0)
        layoutInputsAndLabels.addWidget(self.inputName, 1,0)
        layoutBtns.addWidget(btnAdd)
        layoutItems.addLayout(layoutInputsAndLabels)
        layoutItems.addLayout(layoutBtns)
        layoutItems.addWidget(labelStatus)
        self.table = QtWidgets.QTableView()
        clmns = ["ID", "Отделение"]
        lst = [
          [1, 9],
          [1, 0],
          [3, 5],
        ]
        data = pd.DataFrame(lst, index = range(1,len(lst) + 1), columns = clmns)
        self.model = TableModel(data)
        self.table.setModel(self.model)
        layout.addLayout(layoutItems)
        layout.addWidget(self.table)
        self.setLayout(layout)

        btnAdd.clicked.connect(self.adding)
    def adding(self):
        textName = self.inputName.text()
        self.inputName.clear()

#Удаление отделения
class unitsWindowDeletion(QWidget):
    def __init__(self):
        super().__init__()
        self.setWindowTitle("Удаление отделения")
        layoutInputsAndLabels = QGridLayout()
        layoutBtns = QHBoxLayout()
        layout = QHBoxLayout()
        layoutItems = QVBoxLayout()
        self.inputId = QLineEdit()
        btnDel = QPushButton(text = "Удалить")
        btnDel.setFixedSize(170, 30)
        labelId = QLabel("Код отделения(число)", )
        labelStatus = QLabel()
        labelStatus.setFixedHeight(45)
        layoutInputsAndLabels.addWidget(labelId, 0,0)
        layoutInputsAndLabels.addWidget(self.inputId, 1,0)
        layoutBtns.addWidget(btnDel)
        layoutItems.addLayout(layoutInputsAndLabels)
        layoutItems.addLayout(layoutBtns)
        layoutItems.addWidget(labelStatus)
        self.table = QtWidgets.QTableView()
        clmns = ["ID", "Отделение"]
        lst = [
          [1, 9],
          [1, 0],
          [3, 5],
        ]
        data = pd.DataFrame(lst, index = range(1,len(lst) + 1), columns = clmns)
        self.model = TableModel(data)
        self.table.setModel(self.model)
        layout.addLayout(layoutItems)
        layout.addWidget(self.table)
        self.setLayout(layout)

        btnDel.clicked.connect(self.deletion)
    def deletion(self):
        print()

#Изменение отделения
class unitsWindowChanging(QWidget):
    def __init__(self):
        super().__init__()
        self.setWindowTitle("Изменение Отделений")
        layoutInputsAndLabels = QGridLayout()
        layoutBtns = QHBoxLayout()
        layoutItems = QVBoxLayout()
        layout = QHBoxLayout()
        self.inputIdOld = QLineEdit()
        self.inputIdNew = QLineEdit()
        self.inputNameNew = QLineEdit()
        btnChange = QPushButton(text = "Изменить")
        btnChange.setFixedSize(170, 30)
        labelIdNew = QLabel("Код отделения(число)", )
        labelNameNew = QLabel("Отделение(строка) новое", )
        labelStatus = QLabel()
        labelStatus.setFixedHeight(45)
        layoutInputsAndLabels.addWidget(labelIdNew, 2,0)
        layoutInputsAndLabels.addWidget(labelNameNew, 2,1)
        layoutInputsAndLabels.addWidget(self.inputIdNew, 3,0)
        layoutInputsAndLabels.addWidget(self.inputNameNew, 3,1)
        layoutBtns.addWidget(btnChange)
        layoutItems.addLayout(layoutInputsAndLabels)
        layoutItems.addLayout(layoutBtns)
        layoutItems.addWidget(labelStatus)
        self.table = QtWidgets.QTableView()
        clmns = ["ID", "Отделение"]
        lst = [
          [1, 9],
          [1, 0],
          [3, 5],
        ]
        data = pd.DataFrame(lst, index = range(1,len(lst) + 1), columns = clmns)
        self.model = TableModel(data)
        self.table.setModel(self.model)
        layout.addLayout(layoutItems)
        layout.addWidget(self.table)
        self.setLayout(layout)

        btnChange.clicked.connect(self.changing)
    def changing(self):
        print()
        
          
#Главное окно по отделениям
class unitsWindow(QWidget):
    def __init__(self):
        super().__init__()
        self.setFixedSize(QSize(450, 400))
        self.setWindowTitle("Отделения")
        
        btnAddUnits = QPushButton(text = "Добавить отделение")
        btnAddUnits.setFixedSize(170, 60)
        btnRemoveUnits = QPushButton(text = "Удалить отделение")
        btnRemoveUnits.setFixedSize(170, 60)
        btnEditUnits = QPushButton(text = "Изменить отделение")
        btnEditUnits.setFixedSize(170, 60)
        layoutItems = QVBoxLayout()
        layout = QHBoxLayout()
        layoutItems.addWidget(btnAddUnits)
        layoutItems.addWidget(btnRemoveUnits)
        layoutItems.addWidget(btnEditUnits)
        self.table = QtWidgets.QTableView()
        clmns = ["ID", "Отделение"]
        lst = [
          [1, 9],
          [1, 0],
          [3, 5],
        ]
        data = pd.DataFrame(lst, index = range(1,len(lst) + 1), columns = clmns)
        self.model = TableModel(data)
        self.table.setModel(self.model)
        layout.addLayout(layoutItems)
        layout.addWidget(self.table)
        self.setLayout(layout)
        
        btnAddUnits.clicked.connect(self.show_units_adding_window)
        btnRemoveUnits.clicked.connect(self.show_units_deletion_window)
        btnEditUnits.clicked.connect(self.show_units_changing_window)
    def show_units_adding_window(self):
        self.unitsAdding = unitsWindowAdding()
        self.unitsAdding.show()
    def show_units_deletion_window(self):
        self.unitsDeletion = unitsWindowDeletion()
        self.unitsDeletion.show()
    def show_units_changing_window(self):
        self.unitsChanging = unitsWindowChanging()
        self.unitsChanging.show()



#Добавление должности
class positionsWindowAdding(QWidget):
    def __init__(self):
        super().__init__()
        self.setWindowTitle("Добавление должности")
        layoutInputsAndLabels = QGridLayout()
        layoutBtns = QHBoxLayout()
        layoutItems = QVBoxLayout()
        layout = QHBoxLayout()
        self.inputName = QLineEdit()
        btnAdd = QPushButton(text = "Добавить")
        btnAdd.setFixedSize(170, 30)
        labelName = QLabel("Должность(строка)", )
        labelStatus = QLabel()
        labelStatus.setFixedHeight(45)
        layoutInputsAndLabels.addWidget(labelName, 0,0)
        layoutInputsAndLabels.addWidget(self.inputName, 1,0)
        layoutBtns.addWidget(btnAdd)
        layoutItems.addLayout(layoutInputsAndLabels)
        layoutItems.addLayout(layoutBtns)
        layoutItems.addWidget(labelStatus)
        self.table = QtWidgets.QTableView()
        clmns = ["ID", "Должность"]
        lst = [
          [1, 9],
          [1, 0],
          [3, 5],
        ]
        data = pd.DataFrame(lst, index = range(1,len(lst) + 1), columns = clmns)
        self.model = TableModel(data)
        self.table.setModel(self.model)
        layout.addLayout(layoutItems)
        layout.addWidget(self.table)
        self.setLayout(layout)

        btnAdd.clicked.connect(self.adding)
    def adding(self):
        textName = self.inputName.text()
        self.inputName.clear()

#Удаление должности
class positionsWindowDeletion(QWidget):
    def __init__(self):
        super().__init__()
        self.setWindowTitle("Удаление должности")
        layoutInputsAndLabels = QGridLayout()
        layoutBtns = QHBoxLayout()
        layout = QHBoxLayout()
        layoutItems = QVBoxLayout()
        self.inputId = QLineEdit()
        btnDel = QPushButton(text = "Удалить")
        btnDel.setFixedSize(170, 30)
        labelId = QLabel("Код должности(число)")
        labelStatus = QLabel()
        labelStatus.setFixedHeight(45)
        layoutInputsAndLabels.addWidget(labelId, 0,0)
        layoutInputsAndLabels.addWidget(self.inputId, 1,0)
        layoutBtns.addWidget(btnDel)
        layoutItems.addLayout(layoutInputsAndLabels)
        layoutItems.addLayout(layoutBtns)
        layoutItems.addWidget(labelStatus)
        self.table = QtWidgets.QTableView()
        clmns = ["ID", "Должность"]
        lst = [
          [1, 9],
          [1, 0],
          [3, 5],
        ]
        data = pd.DataFrame(lst, index = range(1,len(lst) + 1), columns = clmns)
        self.model = TableModel(data)
        self.table.setModel(self.model)
        layout.addLayout(layoutItems)
        layout.addWidget(self.table)
        self.setLayout(layout)

        btnDel.clicked.connect(self.deletion)
    def deletion(self):
        print()

#Изменение должности
class positionsWindowChanging(QWidget):
    def __init__(self):
        super().__init__()
        self.setWindowTitle("Изменение Должностей")
        layoutInputsAndLabels = QGridLayout()
        layoutBtns = QHBoxLayout()
        layoutItems = QVBoxLayout()
        layout = QHBoxLayout()
        self.inputIdOld = QLineEdit()
        self.inputIdNew = QLineEdit()
        self.inputNameNew = QLineEdit()
        btnChange = QPushButton(text = "Изменить")
        btnChange.setFixedSize(170, 30)
        labelIdNew = QLabel("Код должности(число)" )
        labelNameNew = QLabel("Должность(строка) новая")
        labelStatus = QLabel()
        labelStatus.setFixedHeight(45)
        layoutInputsAndLabels.addWidget(labelIdNew, 2,0)
        layoutInputsAndLabels.addWidget(labelNameNew, 2,1)
        layoutInputsAndLabels.addWidget(self.inputIdNew, 3,0)
        layoutInputsAndLabels.addWidget(self.inputNameNew, 3,1)
        layoutBtns.addWidget(btnChange)
        layoutItems.addLayout(layoutInputsAndLabels)
        layoutItems.addLayout(layoutBtns)
        layoutItems.addWidget(labelStatus)
        self.table = QtWidgets.QTableView()
        clmns = ["ID", "Должность"]
        lst = [
          [1, 9],
          [1, 0],
          [3, 5],
        ]
        data = pd.DataFrame(lst, index = range(1,len(lst) + 1), columns = clmns)
        self.model = TableModel(data)
        self.table.setModel(self.model)
        layout.addLayout(layoutItems)
        layout.addWidget(self.table)
        self.setLayout(layout)

        btnChange.clicked.connect(self.changing)
    def changing(self):
        print()
        
        
#Главное окно по должностям      
class positionsWindow(QWidget):
    def __init__(self):
        super().__init__()
        self.setFixedSize(QSize(450, 400))
        self.setWindowTitle("Должности")
        
        btnAddPositions = QPushButton(text = "Добавить должность")
        btnAddPositions.setFixedSize(170, 60)
        btnRemovePositions = QPushButton(text = "Удалить должность")
        btnRemovePositions.setFixedSize(170, 60)
        btnEditPositions = QPushButton(text = "Изменить должность")
        btnEditPositions.setFixedSize(170, 60)
        layoutItems = QVBoxLayout()
        layout = QHBoxLayout()
        layoutItems.addWidget(btnAddPositions)
        layoutItems.addWidget(btnRemovePositions)
        layoutItems.addWidget(btnEditPositions)
        self.table = QtWidgets.QTableView()
        clmns = ["ID", "Должность"]
        lst = [
          [1, 9],
          [1, 0],
          [3, 5],
        ]
        data = pd.DataFrame(lst, index = range(1,len(lst) + 1), columns = clmns)
        self.model = TableModel(data)
        self.table.setModel(self.model)
        layout.addLayout(layoutItems)
        layout.addWidget(self.table)
        self.setLayout(layout)
        
        btnAddPositions.clicked.connect(self.show_positions_adding_window)
        btnRemovePositions.clicked.connect(self.show_positions_deletion_window)
        btnEditPositions.clicked.connect(self.show_positions_changing_window)
    def show_positions_adding_window(self):
        self.positionsAdding = positionsWindowAdding()
        self.positionsAdding.show()
    def show_positions_deletion_window(self):
        self.positionsDeletion = positionsWindowDeletion()
        self.positionsDeletion.show()
    def show_positions_changing_window(self):
        self.positionsChanging = positionsWindowChanging()
        self.positionsChanging.show()

#Добавление сотрудника
class employeesWindowAdding(QWidget):
    def __init__(self):
        super().__init__()
        self.setWindowTitle("Добавление сотрудника")
        self.setFixedSize(QSize(900, 200))
        layoutInputsAndLabels = QGridLayout()
        layoutBtns = QHBoxLayout()
        layoutItems = QVBoxLayout()
        layout = QHBoxLayout()
        self.inputName = QLineEdit()
        self.inputPhoneNumber = QLineEdit()
        self.inputEduId = QLineEdit()
        btnAdd = QPushButton(text = "Добавить")
        btnAdd.setFixedSize(170, 30)
        labelName = QLabel("ФИО(строка)")
        labelPhoneNUmber = QLabel("номер телефона(строка)")
        labelEduId = QLabel("Код образования")
        labelStatus = QLabel()
        labelStatus.setFixedHeight(45)
        layoutInputsAndLabels.addWidget(labelName, 0,0)
        layoutInputsAndLabels.addWidget(labelPhoneNUmber, 0,1)
        layoutInputsAndLabels.addWidget(labelEduId, 0,2)
        layoutInputsAndLabels.addWidget(self.inputName, 1,0)
        layoutInputsAndLabels.addWidget(self.inputPhoneNumber, 1,1)
        layoutInputsAndLabels.addWidget(self.inputEduId, 1,2)
        layoutBtns.addWidget(btnAdd)
        layoutItems.addLayout(layoutInputsAndLabels)
        layoutItems.addLayout(layoutBtns)
        layoutItems.addWidget(labelStatus)
        self.table = QtWidgets.QTableView()
        clmns = ["ID", "ФИО", "номер телефона", "Код образования" ]
        lst = [
          [1, "ФИО1", "89999999999", 1],
          [1, "ФИО2", "89999999999", 2],
          [1, "ФИО3", "89999999999", 3]
        ]
        data = pd.DataFrame(lst, index = range(1,len(lst) + 1), columns = clmns)
        self.model = TableModel(data)
        self.table.setModel(self.model)
        layout.addLayout(layoutItems)
        layout.addWidget(self.table)
        self.setLayout(layout)

        btnAdd.clicked.connect(self.adding)
    def adding(self):
        textName = self.inputName.text()
        self.inputName.clear()

#Удаление сотрудника
class employeesWindowDeletion(QWidget):
    def __init__(self):
        super().__init__()
        self.setWindowTitle("Удаление сотрудника")
        self.setFixedSize(QSize(600, 200))
        layoutInputsAndLabels = QGridLayout()
        layoutBtns = QHBoxLayout()
        layout = QHBoxLayout()
        layoutItems = QVBoxLayout()
        self.inputId = QLineEdit()
        self.inputId.setFixedSize(QSize(120,20))
        btnDel = QPushButton(text = "Удалить")
        btnDel.setFixedSize(170, 30)
        labelId = QLabel("Код сотрудника(число)")
        labelStatus = QLabel()
        labelStatus.setFixedHeight(45)
        layoutInputsAndLabels.addWidget(labelId, 0,0)
        layoutInputsAndLabels.addWidget(self.inputId, 1,0)
        layoutBtns.addWidget(btnDel)
        layoutItems.addLayout(layoutInputsAndLabels)
        layoutItems.addLayout(layoutBtns)
        layoutItems.addWidget(labelStatus)
        self.table = QtWidgets.QTableView()
        clmns = ["ID", "ФИО", "номер телефона", "Код образования" ]
        lst = [
          [1, "ФИО1", "89999999999", 1],
          [1, "ФИО2", "89999999999", 2],
          [1, "ФИО3", "89999999999", 3]
        ]
        data = pd.DataFrame(lst, index = range(1,len(lst) + 1), columns = clmns)
        self.model = TableModel(data)
        self.table.setModel(self.model)
        layout.addLayout(layoutItems)
        layout.addWidget(self.table)
        self.setLayout(layout)

        btnDel.clicked.connect(self.deletion)
    def deletion(self):
        print()

#Изменение данных сотрудника
class employeesWindowChanging(QWidget):
    def __init__(self):
        super().__init__()
        self.setWindowTitle("Изменение данных сотрудника")
        self.setFixedSize(QSize(1100, 200))
        layoutInputsAndLabels = QGridLayout()
        layoutBtns = QHBoxLayout()
        layoutItems = QVBoxLayout()
        layout = QHBoxLayout()
        self.inputId = QLineEdit()
        self.inputName = QLineEdit()
        self.inputPhoneNumber = QLineEdit()
        self.inputEduId = QLineEdit()
        btnChange = QPushButton(text = "Изменить")
        btnChange.setFixedSize(170, 30)
        labelId = QLabel("Код сотрудника")
        labelName = QLabel("ФИО(строка) новое")
        labelPhoneNUmber = QLabel("номер телефона(строка) новое")
        labelEduId = QLabel("Код образования новое")
        labelStatus = QLabel()
        labelStatus.setFixedHeight(45)
        layoutInputsAndLabels.addWidget(labelId, 0,0)
        layoutInputsAndLabels.addWidget(labelName, 0,1)
        layoutInputsAndLabels.addWidget(labelPhoneNUmber, 0,2)
        layoutInputsAndLabels.addWidget(labelEduId, 0,3)
        layoutInputsAndLabels.addWidget(self.inputId, 1,0)
        layoutInputsAndLabels.addWidget(self.inputName, 1,1)
        layoutInputsAndLabels.addWidget(self.inputPhoneNumber, 1,2)
        layoutInputsAndLabels.addWidget(self.inputEduId, 1,3)
        layoutBtns.addWidget(btnChange)
        layoutItems.addLayout(layoutInputsAndLabels)
        layoutItems.addLayout(layoutBtns)
        layoutItems.addWidget(labelStatus)
        self.table = QtWidgets.QTableView()
        clmns = ["ID", "ФИО", "номер телефона", "Код образования" ]
        lst = [
          [1, "ФИО1", "89999999999", 1],
          [1, "ФИО2", "89999999999", 2],
          [1, "ФИО3", "89999999999", 3]
        ]
        data = pd.DataFrame(lst, index = range(1,len(lst) + 1), columns = clmns)
        self.model = TableModel(data)
        self.table.setModel(self.model)
        layout.addLayout(layoutItems)
        layout.addWidget(self.table)
        self.setLayout(layout)


        btnChange.clicked.connect(self.changing)
    def changing(self):
        print()
        

#Главное окно по сотрудникам
class employeesWindow(QWidget):
    def __init__(self):
        super().__init__()
        self.setFixedSize(QSize(650, 400))
        self.setWindowTitle("Сотрудники")
        
        btnAddEmployees = QPushButton(text = "Добавить сотрудника")
        btnAddEmployees.setFixedSize(170, 60)
        btnRemoveEmployees = QPushButton(text = "Удалить сотрудника")
        btnRemoveEmployees.setFixedSize(170, 60)
        btnEditEmployees = QPushButton(text = "Изменить данные сотрудника")
        btnEditEmployees.setFixedSize(170, 60)
        layoutItems = QVBoxLayout()
        layout = QHBoxLayout()
        layoutItems.addWidget(btnAddEmployees)
        layoutItems.addWidget(btnRemoveEmployees)
        layoutItems.addWidget(btnEditEmployees)
        self.table = QtWidgets.QTableView()
        clmns = ["ID", "ФИО", "номер телефона", "Код образования" ]
        lst = [
          [1, "ФИО1", "89999999999", 1],
          [1, "ФИО2", "89999999999", 2],
          [1, "ФИО3", "89999999999", 3]
        ]
        data = pd.DataFrame(lst, index = range(1,len(lst) + 1), columns = clmns)
        self.model = TableModel(data)
        self.table.setModel(self.model)
        layout.addLayout(layoutItems)
        layout.addWidget(self.table)
        self.setLayout(layout)
        
        btnAddEmployees.clicked.connect(self.show_employees_adding_window)
        btnRemoveEmployees.clicked.connect(self.show_employees_deletion_window)
        btnEditEmployees.clicked.connect(self.show_employees_changing_window)
    def show_employees_adding_window(self):
        self.employeesAdding = employeesWindowAdding()
        self.employeesAdding.show()
    def show_employees_deletion_window(self):
        self.employeesDeletion = employeesWindowDeletion()
        self.employeesDeletion.show()
    def show_employees_changing_window(self):
        self.employeesChanging = employeesWindowChanging()
        self.employeesChanging.show()


#Добавление записи
class stringsWindowAdding(QWidget):
    def __init__(self):
        super().__init__()
        self.setWindowTitle("Добавление строки")
        self.setFixedSize(QSize(1600, 200))
        layoutInputsAndLabels = QGridLayout()
        layoutBtns = QHBoxLayout()
        layoutItems = QVBoxLayout()
        layout = QHBoxLayout()
        self.inputIdEmployee = QLineEdit()
        self.inputDate = QLineEdit()
        self.inputIdPost = QLineEdit()
        self.inputIdUnit = QLineEdit()
        self.inputSalary = QLineEdit()
        self.inputPhoneNumber = QLineEdit()
        self.inputEduId = QLineEdit()
        btnAdd = QPushButton(text = "Добавить")
        btnAdd.setFixedSize(170, 30)
        labelIdEmployee= QLabel("Код сотрудника(число)")
        labelDate = QLabel("Дата назначения")
        labelIdPost = QLabel("Код должности")
        labelIdUnit = QLabel("Код подразделения")
        labelSalary = QLabel("ЗП")
        labelStatus = QLabel()
        labelStatus.setFixedHeight(45)
        layoutInputsAndLabels.addWidget(labelIdEmployee, 0,0)
        layoutInputsAndLabels.addWidget(labelDate, 0,1)
        layoutInputsAndLabels.addWidget(labelIdPost, 0,2)
        layoutInputsAndLabels.addWidget(labelIdUnit,0,3)
        layoutInputsAndLabels.addWidget(labelSalary, 0,4)
        layoutInputsAndLabels.addWidget(self.inputIdEmployee, 1,0)
        layoutInputsAndLabels.addWidget(self.inputDate, 1,1)
        layoutInputsAndLabels.addWidget(self.inputIdPost, 1,2)
        layoutInputsAndLabels.addWidget(self.inputIdUnit, 1,3)
        layoutInputsAndLabels.addWidget(self.inputSalary, 1,4)
        layoutBtns.addWidget(btnAdd)
        layoutItems.addLayout(layoutInputsAndLabels)
        layoutItems.addLayout(layoutBtns)
        layoutItems.addWidget(labelStatus)
        self.table = QtWidgets.QTableView()
        clmns = ["ID строки","Номер сотрудника","Номер записи","Дата назначения", "Номер должности", "Номер отделения", "Зарплата"]
        lst = [
            [1,1, 1,"11.11.2011", 1, 1, 50000],
            [2,2, 1,"11.11.2011", 2, 2, 50000],
            [3,3, 1,"11.11.2011", 1, 3, 50000]
        ]
        data = pd.DataFrame(lst, index = range(1,len(lst) + 1), columns = clmns)
        self.model = TableModel(data)
        self.table.setModel(self.model)
        layout.addLayout(layoutItems)
        layout.addWidget(self.table)
        self.setLayout(layout)
        header = self.table.horizontalHeader()       
        header.setSectionResizeMode(1, QHeaderView.ResizeMode.ResizeToContents)
        header.setSectionResizeMode(2, QHeaderView.ResizeMode.ResizeToContents)
        header.setSectionResizeMode(3, QHeaderView.ResizeMode.ResizeToContents)
        header.setSectionResizeMode(4, QHeaderView.ResizeMode.ResizeToContents)
        header.setSectionResizeMode(5, QHeaderView.ResizeMode.ResizeToContents)
        btnAdd.clicked.connect(self.adding)
    def adding(self):
        print()

#Удаление записи
class stringsWindowDeletion(QWidget):
    def __init__(self):
        super().__init__()
        self.setWindowTitle("Добавление строки")
        self.setFixedSize(QSize(1200, 200))
        layoutInputsAndLabels = QGridLayout()
        layoutBtns = QHBoxLayout()
        layoutItems = QVBoxLayout()
        layout = QHBoxLayout()
        self.inputIdString = QLineEdit()
        self.inputIdString.setFixedSize(QSize(100, 25))
        btnDel = QPushButton(text = "Удалить")
        btnDel.setFixedSize(170, 30)
        labelIdString = QLabel("ID строки")
        labelStatus = QLabel()
        labelStatus.setFixedHeight(45)
        layoutInputsAndLabels.addWidget(labelIdString, 0,0)
        layoutInputsAndLabels.addWidget(self.inputIdString, 1,0)
        layoutBtns.addWidget(btnDel)
        layoutItems.addLayout(layoutInputsAndLabels)
        layoutItems.addLayout(layoutBtns)
        layoutItems.addWidget(labelStatus)
        self.table = QtWidgets.QTableView()
        clmns = ["ID строки","Номер сотрудника","Номер записи","Дата назначения", "Номер должности", "Номер отделения", "Зарплата"]
        lst = [
            [1,1, 1,"11.11.2011", 1, 1, 50000],
            [2,2, 1,"11.11.2011", 2, 2, 50000],
            [3,3, 1,"11.11.2011", 1, 3, 50000]
        ]
        data = pd.DataFrame(lst, index = range(1,len(lst) + 1), columns = clmns)
        self.model = TableModel(data)
        self.table.setModel(self.model)
        layout.addLayout(layoutItems)
        layout.addWidget(self.table)
        self.setLayout(layout)
        header = self.table.horizontalHeader()       
        header.setSectionResizeMode(1, QHeaderView.ResizeMode.ResizeToContents)
        header.setSectionResizeMode(2, QHeaderView.ResizeMode.ResizeToContents)
        header.setSectionResizeMode(3, QHeaderView.ResizeMode.ResizeToContents)
        header.setSectionResizeMode(4, QHeaderView.ResizeMode.ResizeToContents)
        header.setSectionResizeMode(5, QHeaderView.ResizeMode.ResizeToContents)
        btnDel.clicked.connect(self.deletion)
    def deletion(self):
        print()

#Изменение данных записи
class stringsWindowChanging(QWidget):
    def __init__(self):
        super().__init__()
        self.setWindowTitle("Добавление строки")
        self.setFixedSize(QSize(1600, 200))
        layoutInputsAndLabels = QGridLayout()
        layoutBtns = QHBoxLayout()
        layoutItems = QVBoxLayout()
        layout = QHBoxLayout()
        self.inputId = QLineEdit()
        self.inputIdEmployee = QLineEdit()
        self.inputDate = QLineEdit()
        self.inputIdPost = QLineEdit()
        self.inputIdUnit = QLineEdit()
        self.inputSalary = QLineEdit()
        self.inputPhoneNumber = QLineEdit()
        self.inputEduId = QLineEdit()
        btnChange = QPushButton(text = "Изменить")
        btnChange.setFixedSize(170, 30)
        labelId= QLabel("ID строки для изменения")
        labelIdEmployee= QLabel("Код сотрудника(число)")
        labelDate = QLabel("Дата назначения")
        labelIdPost = QLabel("Код должности")
        labelIdUnit = QLabel("Код подразделения")
        labelSalary = QLabel("ЗП")
        labelStatus = QLabel()
        labelStatus.setFixedHeight(45)
        layoutInputsAndLabels.addWidget(labelId, 0,0)
        layoutInputsAndLabels.addWidget(labelIdEmployee, 0,1)
        layoutInputsAndLabels.addWidget(labelDate, 0,2)
        layoutInputsAndLabels.addWidget(labelIdPost, 0,3)
        layoutInputsAndLabels.addWidget(labelIdUnit,0,4)
        layoutInputsAndLabels.addWidget(labelSalary, 0,5)
        layoutInputsAndLabels.addWidget(self.inputId, 1,0)
        layoutInputsAndLabels.addWidget(self.inputIdEmployee, 1,1)
        layoutInputsAndLabels.addWidget(self.inputDate, 1,2)
        layoutInputsAndLabels.addWidget(self.inputIdPost, 1,3)
        layoutInputsAndLabels.addWidget(self.inputIdUnit, 1,4)
        layoutInputsAndLabels.addWidget(self.inputSalary, 1,5)
        layoutBtns.addWidget(btnChange)
        layoutItems.addLayout(layoutInputsAndLabels)
        layoutItems.addLayout(layoutBtns)
        layoutItems.addWidget(labelStatus)
        self.table = QtWidgets.QTableView()
        clmns = ["ID строки","Номер сотрудника","Номер записи","Дата назначения", "Номер должности", "Номер отделения", "Зарплата"]
        lst = [
            [1,1, 1,"11.11.2011", 1, 1, 50000],
            [2,2, 1,"11.11.2011", 2, 2, 50000],
            [3,3, 1,"11.11.2011", 1, 3, 50000]
        ]
        data = pd.DataFrame(lst, index = range(1,len(lst) + 1), columns = clmns)
        self.model = TableModel(data)
        self.table.setModel(self.model)
        layout.addLayout(layoutItems)
        layout.addWidget(self.table)
        self.setLayout(layout)
        header = self.table.horizontalHeader()       
        header.setSectionResizeMode(1, QHeaderView.ResizeMode.ResizeToContents)
        header.setSectionResizeMode(2, QHeaderView.ResizeMode.ResizeToContents)
        header.setSectionResizeMode(3, QHeaderView.ResizeMode.ResizeToContents)
        header.setSectionResizeMode(4, QHeaderView.ResizeMode.ResizeToContents)
        header.setSectionResizeMode(5, QHeaderView.ResizeMode.ResizeToContents)
        btnChange.clicked.connect(self.changing)
    def changing(self):
        print()

#Главное окно по записям
class stringsWindow(QWidget):
    def __init__(self):
        super().__init__()
        self.setFixedSize(QSize(1200, 400))
        self.setWindowTitle("Записи")
        
        btnAddString = QPushButton(text = "Добавить запись")
        btnAddString.setFixedSize(170, 60)
        btnRemoveString = QPushButton(text = "Удалить запись")
        btnRemoveString.setFixedSize(170, 60)
        btnEditString = QPushButton(text = "Изменить запись")
        btnEditString.setFixedSize(170, 60)
        layoutItems = QVBoxLayout()
        layout = QHBoxLayout()
        layoutItems.addWidget(btnAddString)
        layoutItems.addWidget(btnRemoveString)
        layoutItems.addWidget(btnEditString)
        self.table = QtWidgets.QTableView()
        clmns = ["ID строки","Номер сотрудника","Номер записи","Дата назначения", "Номер должности", "Номер отделения", "Зарплата"]
        lst = [
            [1,1, 1,"11.11.2011", 1, 1, 50000],
            [2,2, 1,"11.11.2011", 2, 2, 50000],
            [3,3, 1,"11.11.2011", 1, 3, 50000]
        ]
        data = pd.DataFrame(lst, index = range(1,len(lst) + 1), columns = clmns)
        self.model = TableModel(data)
        self.table.setModel(self.model)
        layout.addLayout(layoutItems)
        layout.addWidget(self.table)
        self.setLayout(layout)
        header = self.table.horizontalHeader()       
        header.setSectionResizeMode(1, QHeaderView.ResizeMode.ResizeToContents)
        header.setSectionResizeMode(2, QHeaderView.ResizeMode.ResizeToContents)
        header.setSectionResizeMode(3, QHeaderView.ResizeMode.ResizeToContents)
        header.setSectionResizeMode(4, QHeaderView.ResizeMode.ResizeToContents)
        header.setSectionResizeMode(5, QHeaderView.ResizeMode.ResizeToContents)
        btnAddString.clicked.connect(self.show_string_adding_window)
        btnRemoveString.clicked.connect(self.show_string_deletion_window)
        btnEditString.clicked.connect(self.show_string_changing_window)
        
    def show_string_adding_window(self):
        self.stringsAdding = stringsWindowAdding()
        self.stringsAdding.show()
    def show_string_deletion_window(self):
        self.stringsDeletion = stringsWindowDeletion()
        self.stringsDeletion.show()
    def show_string_changing_window(self):
        self.stringsChanging = stringsWindowChanging()
        self.stringsChanging.show()

        
#Стартовое окно
class MainWindow(QWidget):
    def __init__(self):
        super().__init__()
        self.setFixedSize(QSize(500, 400))
        self.setWindowTitle("Главное окно")
        
        btnEducations = QPushButton(text = "Образование")
        btnEducations.setFixedSize(140, 60)
        btnUnits = QPushButton(text = "Отделения")
        btnUnits.setFixedSize(140, 60)
        btnPositions = QPushButton(text = "Должности")
        btnPositions.setFixedSize(140, 60)
        btnEmployees = QPushButton(text = "Сотрудники")
        btnEmployees.setFixedSize(140, 60)
        btnStrings = QPushButton(text = "Записи назначений")
        btnStrings.setFixedSize(140, 60)
        layout = QVBoxLayout()
        layout.addWidget(btnEducations)
        layout.addWidget(btnUnits)
        layout.addWidget(btnPositions)
        layout.addWidget(btnEmployees)
        layout.addWidget(btnStrings)
        self.setLayout(layout)
        
        btnEducations.clicked.connect(self.show_education_window)
        btnUnits.clicked.connect(self.show_units_window)
        btnPositions.clicked.connect(self.show_positions_window)
        btnEmployees.clicked.connect(self.show_employees_window)
        btnStrings.clicked.connect(self.show_strings_window)
        
    def show_education_window(self):
        self.educations = educationsWindow()
        self.educations.show()
    
    def show_units_window(self):
        self.units = unitsWindow()
        self.units.show()
    
    def show_positions_window(self):
        self.positions = positionsWindow()
        self.positions.show()
    
    def show_employees_window(self):
        self.employees = employeesWindow()
        self.employees.show()
    
    def show_strings_window(self):
        self.strings = stringsWindow()
        self.strings.show()
        

        
app = QApplication([])

window = MainWindow()
window.show()
app.exec()