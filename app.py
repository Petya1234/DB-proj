from PyQt6.QtCore import QSize
from PyQt6.QtCore import Qt
from PyQt6.QtWidgets import QApplication, QPushButton, QVBoxLayout, QWidget, QLabel, QMainWindow, QHBoxLayout, QLineEdit, QGridLayout, QHeaderView, QComboBox
from PyQt6 import QtCore, QtGui, QtWidgets
import pandas as pd
from db import educationsTable, unitsTable, positionsTable, employeesTable, stringsTable

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
            

#Окно "по образованиям"
class checkByEducations(QWidget):
    def __init__(self):
        super().__init__()
        self.setWindowTitle("По образованиям")
        layoutInputsAndLabels = QVBoxLayout()
        layoutItems = QVBoxLayout()
        layout = QHBoxLayout()
        self.inputEducationIdLabel = QLabel("Коды образования")
        self.comboBoxEducations = QComboBox()
        self.comboBoxEducations.addItems([str(x[0]) for x in educationsTable.show_educations_table()])
        layoutInputsAndLabels.addWidget(self.inputEducationIdLabel)
        layoutInputsAndLabels.addWidget(self.comboBoxEducations)
        layoutItems.addLayout(layoutInputsAndLabels)
        self.table = QtWidgets.QTableView()
        self.clmns = ["Сотрудники"]
        lst = employeesTable.show_employees_table_by_edu(educationsTable.show_educations_table()[0][0])
        self.data = pd.DataFrame(lst, index = range(1,len(lst) + 1), columns = self.clmns)
        self.model = TableModel(self.data)
        self.table.setModel(self.model)
        layout.addLayout(layoutItems)
        layout.addWidget(self.table)
        self.table.resizeColumnsToContents()
        self.setLayout(layout)
        self.comboBoxEducations.currentTextChanged.connect(self.showByEdu)
            
    def showByEdu(self):
        eduId = int(self.comboBoxEducations.currentText())
        lst = employeesTable.show_employees_table_by_edu(eduId)
        self.data = pd.DataFrame(lst, index = range(1,len(lst) + 1), columns = self.clmns)
        self.model = TableModel(self.data)
        self.table.setModel(self.model)
        self.table.resizeColumnsToContents()
            
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
        self.inputEduId = QLineEdit()
        btnAdd = QPushButton(text = "Добавить")
        btnAdd.setFixedSize(170, 30)
        labelEduId = QLabel("Код образования(число)")
        labelName = QLabel("Тип образования образования(строка)", )
        self.labelStatus = QLabel()
        self.labelStatus.setFixedHeight(45)
        self.labelStatus.setAlignment(Qt.AlignmentFlag.AlignCenter)
        layoutInputsAndLabels.addWidget(labelEduId, 0,0)
        layoutInputsAndLabels.addWidget(labelName, 0,1)
        layoutInputsAndLabels.addWidget(self.inputEduId, 1,0)
        layoutInputsAndLabels.addWidget(self.inputName, 1,1)
        layoutBtns.addWidget(btnAdd)
        layoutItems.addLayout(layoutInputsAndLabels)
        layoutItems.addLayout(layoutBtns)
        layoutItems.addWidget(self.labelStatus)
        self.table = QtWidgets.QTableView()
        self.clmns = ["Код образования", "Тип образования"]
        lst = educationsTable.show_educations_table()
        self.data = pd.DataFrame(lst, index = range(1,len(lst) + 1), columns = self.clmns)
        self.model = TableModel(self.data)
        self.table.setModel(self.model)
        layout.addLayout(layoutItems)
        layout.addWidget(self.table)
        self.setLayout(layout)
        btnAdd.clicked.connect(self.adding)
        
    def adding(self):
        eduId = self.inputEduId.text()
        eduType = self.inputName.text()
        if educationsTable.add_to_educations_table(edu_id=eduId, eduType=eduType) == "repeat":
            self.labelStatus.setText("Код уже добавлен")
        else:
            self.labelStatus.setText("Успешно")
        self.inputEduId.clear()
        self.inputName.clear()
        lst = educationsTable.show_educations_table()
        self.data = pd.DataFrame(lst, index = range(1,len(lst) + 1), columns = self.clmns)
        self.model = TableModel(self.data)
        self.table.setModel(self.model)
        window.educations.table.setModel(self.model)

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
        self.labelStatus = QLabel()
        self.labelStatus.setFixedHeight(45)
        self.labelStatus.setAlignment(Qt.AlignmentFlag.AlignCenter)
        layoutInputsAndLabels.addWidget(labelId, 0,0)
        layoutInputsAndLabels.addWidget(self.inputId, 1,0)
        layoutBtns.addWidget(btnDel)
        layoutItems.addLayout(layoutInputsAndLabels)
        layoutItems.addLayout(layoutBtns)
        layoutItems.addWidget(self.labelStatus)
        self.table = QtWidgets.QTableView()
        self.clmns = ["Код образования", "Тип образования"]
        lst = educationsTable.show_educations_table()
        self.data = pd.DataFrame(lst, index = range(1,len(lst) + 1), columns = self.clmns)
        self.model = TableModel(self.data)
        self.table.setModel(self.model)
        layout.addLayout(layoutItems)
        layout.addWidget(self.table)
        self.setLayout(layout)
        btnDel.clicked.connect(self.deletion)
        
    def deletion(self):
        eduId = int(self.inputId.text())
        self.inputId.clear()
        res = educationsTable.delete_from_education_table(edu_id=eduId)
        if res == "FK error":
            self.labelStatus.setText("Код образования присвоен сотрудникам")
        elif res == "Not in table":
            self.labelStatus.setText("Ключа нет в таблице")
        else:
            self.labelStatus.setText("Успешно")
        lst = educationsTable.show_educations_table()
        self.data = pd.DataFrame(lst, index = range(1,len(lst) + 1), columns = self.clmns)
        self.model = TableModel(self.data)
        self.table.setModel(self.model)
        window.educations.table.setModel(self.model)
        

#Изменение образования
class educationsWindowChanging(QWidget):
    def __init__(self):
        super().__init__()
        self.setWindowTitle("Изменение образований")
        layoutInputsAndLabels = QGridLayout()
        layoutBtns = QHBoxLayout()
        layoutItems = QVBoxLayout()
        layout = QHBoxLayout()
        self.inputEduId = QLineEdit()
        self.inputNameNew = QLineEdit()
        btnChange = QPushButton(text = "Изменить")
        btnChange.setFixedSize(170, 30)
        labelEduId = QLabel("Код образования(число)")
        labelNameNew = QLabel("Тип образования(строка) новое")
        self.labelStatus = QLabel()
        self.labelStatus.setFixedHeight(45)
        self.labelStatus.setAlignment(Qt.AlignmentFlag.AlignCenter)
        layoutInputsAndLabels.addWidget(labelEduId, 0,0)
        layoutInputsAndLabels.addWidget(labelNameNew, 0,1)
        layoutInputsAndLabels.addWidget(self.inputEduId, 1,0)
        layoutInputsAndLabels.addWidget(self.inputNameNew, 1,1)
        layoutBtns.addWidget(btnChange)
        layoutItems.addLayout(layoutInputsAndLabels)
        layoutItems.addLayout(layoutBtns)
        layoutItems.addWidget(self.labelStatus)
        self.table = QtWidgets.QTableView()
        self.clmns = ["Код образования", "Тип образования"]
        lst = educationsTable.show_educations_table()
        self.data = pd.DataFrame(lst, index = range(1,len(lst) + 1), columns = self.clmns)
        self.model = TableModel(self.data)
        self.table.setModel(self.model)
        layout.addLayout(layoutItems)
        layout.addWidget(self.table)
        self.setLayout(layout)
        btnChange.clicked.connect(self.changing)
    def changing(self):
        eduId = int(self.inputEduId.text())
        eduType = self.inputNameNew.text()
        res = educationsTable.update_education_table(edu_id=eduId, eduType=eduType) 
        if res == "Not in table":
            self.labelStatus.setText("Ключа нет в таблице")
        else:
            self.labelStatus.setText("Успешно")
        self.inputEduId.clear()
        self.inputNameNew.clear()
        lst = educationsTable.show_educations_table()
        self.data = pd.DataFrame(lst, index = range(1,len(lst) + 1), columns = self.clmns)
        self.model = TableModel(self.data)
        self.table.setModel(self.model)
        window.educations.table.setModel(self.model)

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
        clmns =  ["Код образования", "Тип образования"]
        lst = educationsTable.show_educations_table()
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



#Окно "по отделениям"
class checkByUnits(QWidget):
    def __init__(self):
        super().__init__()
        self.setWindowTitle("По отделениям")
        layoutInputsAndLabels = QVBoxLayout()
        layoutItems = QVBoxLayout()
        layout = QHBoxLayout()
        self.inputUnitLabel = QLabel("Отделения")
        self.comboBoxUnits = QComboBox()
        self.comboBoxUnits.addItems([str(x[1]) for x in unitsTable.show_units_table()])
        layoutInputsAndLabels.addWidget(self.inputUnitLabel)
        layoutInputsAndLabels.addWidget(self.comboBoxUnits)
        layoutItems.addLayout(layoutInputsAndLabels)
        self.table = QtWidgets.QTableView()
        self.clmns = ["Сотрудники"]
        lst = unitsTable.show_units_table_by_name(unitsTable.show_units_table()[0][1])
        self.data = pd.DataFrame(lst, index = range(1,len(lst) + 1), columns = self.clmns)
        self.model = TableModel(self.data)
        self.table.setModel(self.model)
        layout.addLayout(layoutItems)
        layout.addWidget(self.table)
        self.table.resizeColumnsToContents()
        self.setLayout(layout)
        self.comboBoxUnits.currentTextChanged.connect(self.showByUnit)
            
    def showByUnit(self):
        unit = self.comboBoxUnits.currentText()
        lst = unitsTable.show_units_table_by_name(unit)
        self.data = pd.DataFrame(lst, index = range(1,len(lst) + 1), columns = self.clmns)
        self.model = TableModel(self.data)
        self.table.setModel(self.model)
        self.table.resizeColumnsToContents()
        
        
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
        labelName = QLabel("Отделения(строка)" )
        self.labelStatus = QLabel()
        self.labelStatus.setFixedHeight(45)
        self.labelStatus.setAlignment(Qt.AlignmentFlag.AlignCenter)
        layoutInputsAndLabels.addWidget(labelName, 0,0)
        layoutInputsAndLabels.addWidget(self.inputName, 1,0)
        layoutBtns.addWidget(btnAdd)
        layoutItems.addLayout(layoutInputsAndLabels)
        layoutItems.addLayout(layoutBtns)
        layoutItems.addWidget(self.labelStatus)
        self.table = QtWidgets.QTableView()
        self.clmns = ["Код отделения", "Отделение"]
        lst = unitsTable.show_units_table()
        self.data = pd.DataFrame(lst, index = range(1,len(lst) + 1), columns = self.clmns)
        self.model = TableModel(self.data)
        self.table.setModel(self.model)
        layout.addLayout(layoutItems)
        layout.addWidget(self.table)
        self.setLayout(layout)
        btnAdd.clicked.connect(self.adding)
    def adding(self):
        unitName = self.inputName.text()
        self.inputName.clear()
        res = unitsTable.add_to_units_table(unit = unitName)
        if res == "repeat":
            self.labelStatus.setText("Отделение уже добавлено")
        else:
            self.labelStatus.setText("Успешно")
        lst = unitsTable.show_units_table()
        self.data = pd.DataFrame(lst, index = range(1,len(lst) + 1), columns = self.clmns)
        self.model = TableModel(self.data)
        self.table.setModel(self.model)
        window.units.table.setModel(self.model)

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
        self.labelStatus = QLabel()
        self.labelStatus.setFixedHeight(45)
        self.labelStatus.setAlignment(Qt.AlignmentFlag.AlignCenter)
        layoutInputsAndLabels.addWidget(labelId, 0,0)
        layoutInputsAndLabels.addWidget(self.inputId, 1,0)
        layoutBtns.addWidget(btnDel)
        layoutItems.addLayout(layoutInputsAndLabels)
        layoutItems.addLayout(layoutBtns)
        layoutItems.addWidget(self.labelStatus)
        self.table = QtWidgets.QTableView()
        self.clmns = ["Код отделения", "Отделение"]
        lst = unitsTable.show_units_table()
        self.data = pd.DataFrame(lst, index = range(1,len(lst) + 1), columns = self.clmns)
        self.model = TableModel(self.data)
        self.table.setModel(self.model)
        layout.addLayout(layoutItems)
        layout.addWidget(self.table)
        self.setLayout(layout)
        btnDel.clicked.connect(self.deletion)
        
    def deletion(self):
        unitId = int(self.inputId.text())
        res = unitsTable.delete_from_units_table(unit_id=unitId)
        if  res == "FK error":
            self.labelStatus.setText("Данное отделение есть у сотрудников")
        elif res == "Not in table":
            self.labelStatus.setText("Ключа нет в таблице")
        else:
            self.labelStatus.setText("Успешно")
        lst = unitsTable.show_units_table()
        self.data = pd.DataFrame(lst, index = range(1,len(lst) + 1), columns = self.clmns)
        self.model = TableModel(self.data)
        self.table.setModel(self.model)
        self.inputId.clear()
        window.units.table.setModel(self.model)

#Изменение отделения
class unitsWindowChanging(QWidget):
    def __init__(self):
        super().__init__()
        self.setWindowTitle("Изменение Отделений")
        layoutInputsAndLabels = QGridLayout()
        layoutBtns = QHBoxLayout()
        layoutItems = QVBoxLayout()
        layout = QHBoxLayout()
        self.inputId = QLineEdit()
        self.inputNameNew = QLineEdit()
        btnChange = QPushButton(text = "Изменить")
        btnChange.setFixedSize(170, 30)
        labelId = QLabel("Код отделения(число)", )
        labelNameNew = QLabel("Отделение(строка) новое", )
        self.labelStatus = QLabel()
        self.labelStatus.setFixedHeight(45)
        self.labelStatus.setAlignment(Qt.AlignmentFlag.AlignCenter)
        layoutInputsAndLabels.addWidget(labelId, 0,0)
        layoutInputsAndLabels.addWidget(labelNameNew, 0,1)
        layoutInputsAndLabels.addWidget(self.inputId, 1,0)
        layoutInputsAndLabels.addWidget(self.inputNameNew, 1,1)
        layoutBtns.addWidget(btnChange)
        layoutItems.addLayout(layoutInputsAndLabels)
        layoutItems.addLayout(layoutBtns)
        layoutItems.addWidget(self.labelStatus)
        self.table = QtWidgets.QTableView()
        self.clmns = ["Код отделения", "Отделение"]
        lst = unitsTable.show_units_table()
        self.data = pd.DataFrame(lst, index = range(1,len(lst) + 1), columns = self.clmns)
        self.model = TableModel(self.data)
        self.table.setModel(self.model)
        layout.addLayout(layoutItems)
        layout.addWidget(self.table)
        self.setLayout(layout)
        btnChange.clicked.connect(self.changing)
    def changing(self):
        unitId = int(self.inputId.text())
        unit = self.inputNameNew.text()
        res = unitsTable.update_units_table(unit_id=unitId, unit = unit)
        if res == "Not in table":
            self.labelStatus.setText("Ключа нет в таблице")
        else:
            self.labelStatus.setText("Успешно")
        self.inputId.clear()
        self.inputNameNew.clear()
        lst = unitsTable.show_units_table()
        self.data = pd.DataFrame(lst, index = range(1,len(lst) + 1), columns = self.clmns)
        self.model = TableModel(self.data)
        self.table.setModel(self.model)
        window.units.table.setModel(self.model)
        
          
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
        clmns = ["Код отделения", "Отделение"]
        lst = unitsTable.show_units_table()
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


#Окно "по должностям"
class checkByPositions(QWidget):
    def __init__(self):
        super().__init__()
        self.setWindowTitle("По должностям")
        layoutInputsAndLabels = QVBoxLayout()
        layoutItems = QVBoxLayout()
        layout = QHBoxLayout()
        self.inputPostLabel = QLabel("Должности")
        self.comboBoxPositions = QComboBox()
        self.comboBoxPositions.addItems([str(x[1]) for x in positionsTable.show_positions_table()])
        layoutInputsAndLabels.addWidget(self.inputPostLabel)
        layoutInputsAndLabels.addWidget(self.comboBoxPositions)
        layoutItems.addLayout(layoutInputsAndLabels)
        self.table = QtWidgets.QTableView()
        self.clmns = ["Сотрудники"]
        lst = positionsTable.show_positions_table_by_name(positionsTable.show_positions_table()[0][1])
        self.data = pd.DataFrame(lst, index = range(1,len(lst) + 1), columns = self.clmns)
        self.model = TableModel(self.data)
        self.table.setModel(self.model)
        layout.addLayout(layoutItems)
        layout.addWidget(self.table)
        self.table.resizeColumnsToContents()
        self.setLayout(layout)
        self.comboBoxPositions.currentTextChanged.connect(self.showByPosition)
            
    def showByPosition(self):
        unit = self.comboBoxPositions.currentText()
        lst = positionsTable.show_positions_table_by_name(unit)
        self.data = pd.DataFrame(lst, index = range(1,len(lst) + 1), columns = self.clmns)
        self.model = TableModel(self.data)
        self.table.setModel(self.model)
        self.table.resizeColumnsToContents()
        
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
        labelName = QLabel("Должность(строка)")
        self.labelStatus = QLabel()
        self.labelStatus.setFixedHeight(45)
        self.labelStatus.setAlignment(Qt.AlignmentFlag.AlignCenter)
        layoutInputsAndLabels.addWidget(labelName, 0,0)
        layoutInputsAndLabels.addWidget(self.inputName, 1,0)
        layoutBtns.addWidget(btnAdd)
        layoutItems.addLayout(layoutInputsAndLabels)
        layoutItems.addLayout(layoutBtns)
        layoutItems.addWidget(self.labelStatus)
        self.table = QtWidgets.QTableView()
        self.clmns = ["Код должности", "Должность"]
        lst = positionsTable.show_positions_table()
        self.data = pd.DataFrame(lst, index = range(1,len(lst) + 1), columns = self.clmns)
        self.model = TableModel(self.data)
        self.table.setModel(self.model)
        layout.addLayout(layoutItems)
        layout.addWidget(self.table)
        self.setLayout(layout)
        btnAdd.clicked.connect(self.adding)
        
    def adding(self):
        postName = self.inputName.text()
        self.inputName.clear()
        res = positionsTable.add_to_positions_table(post = postName)
        if res == "repeat":
            self.labelStatus.setText("Должность уже добавлена")
        else:
            self.labelStatus.setText("Успешно")
        lst = positionsTable.show_positions_table()
        self.data = pd.DataFrame(lst, index = range(1,len(lst) + 1), columns = self.clmns)
        self.model = TableModel(self.data)
        self.table.setModel(self.model)
        window.positions.table.setModel(self.model)

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
        self.labelStatus = QLabel()
        self.labelStatus.setFixedHeight(45)
        self.labelStatus.setAlignment(Qt.AlignmentFlag.AlignCenter)
        layoutInputsAndLabels.addWidget(labelId, 0,0)
        layoutInputsAndLabels.addWidget(self.inputId, 1,0)
        layoutBtns.addWidget(btnDel)
        layoutItems.addLayout(layoutInputsAndLabels)
        layoutItems.addLayout(layoutBtns)
        layoutItems.addWidget(self.labelStatus)
        self.table = QtWidgets.QTableView()
        self.clmns = ["Код должности", "Должность"]
        lst = positionsTable.show_positions_table()
        self.data = pd.DataFrame(lst, index = range(1,len(lst) + 1), columns = self.clmns)
        self.model = TableModel(self.data)
        self.table.setModel(self.model)
        layout.addLayout(layoutItems)
        layout.addWidget(self.table)
        self.setLayout(layout)

        btnDel.clicked.connect(self.deletion)
    def deletion(self):
        postId = int(self.inputId.text())
        self.inputId.clear()
        res = positionsTable.delete_from_positions_table(post_id = postId)
        if res == "FK error":
            self.labelStatus.setText("Данная должность есть у сотридников")
        elif res == "Not in table":
            self.labelStatus.setText("Ключа нет в таблице")
        else:
            self.labelStatus.setText("Успешно")
        lst = positionsTable.show_positions_table()
        self.data = pd.DataFrame(lst, index = range(1,len(lst) + 1), columns = self.clmns)
        self.model = TableModel(self.data)
        self.table.setModel(self.model)
        window.positions.table.setModel(self.model)


#Изменение должности
class positionsWindowChanging(QWidget):
    def __init__(self):
        super().__init__()
        self.setWindowTitle("Изменение Должностей")
        layoutInputsAndLabels = QGridLayout()
        layoutBtns = QHBoxLayout()
        layoutItems = QVBoxLayout()
        layout = QHBoxLayout()
        self.inputId = QLineEdit()
        self.inputNameNew = QLineEdit()
        btnChange = QPushButton(text = "Изменить")
        btnChange.setFixedSize(170, 30)
        labelId = QLabel("Код должности(число)" )
        labelNameNew = QLabel("Должность(строка) новая")
        self.labelStatus = QLabel()
        self.labelStatus.setFixedHeight(45)
        self.labelStatus.setAlignment(Qt.AlignmentFlag.AlignCenter)
        layoutInputsAndLabels.addWidget(labelId ,0,0)
        layoutInputsAndLabels.addWidget(labelNameNew, 0,1)
        layoutInputsAndLabels.addWidget(self.inputId, 1,0)
        layoutInputsAndLabels.addWidget(self.inputNameNew, 1,1)
        layoutBtns.addWidget(btnChange)
        layoutItems.addLayout(layoutInputsAndLabels)
        layoutItems.addLayout(layoutBtns)
        layoutItems.addWidget(self.labelStatus)
        self.table = QtWidgets.QTableView()
        self.clmns = ["Код должности", "Должность"]
        lst = positionsTable.show_positions_table()
        self.data = pd.DataFrame(lst, index = range(1,len(lst) + 1), columns = self.clmns)
        self.model = TableModel(self.data)
        self.table.setModel(self.model)
        layout.addLayout(layoutItems)
        layout.addWidget(self.table)
        self.setLayout(layout)

        btnChange.clicked.connect(self.changing)
    def changing(self):
        postId = int(self.inputId.text())
        post = self.inputNameNew.text()
        res = positionsTable.update_positions_table(post_id=postId, post = post)
        if res == "Not in table":
            self.labelStatus.setText("Ключа нет в таблице")
        else:
            self.labelStatus.setText("Успешно")
        self.inputId.clear()
        self.inputNameNew.clear()
        lst = positionsTable.show_positions_table()
        self.data = pd.DataFrame(lst, index = range(1,len(lst) + 1), columns = self.clmns)
        self.model = TableModel(self.data)
        self.table.setModel(self.model)
        window.positions.table.setModel(self.model)
        
        
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
        clmns = ["Код должности", "Должность"]
        lst = positionsTable.show_positions_table()
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
        lst = employeesTable.show_employees_table()
        self.setWindowTitle("Добавление сотрудника")
        self.setFixedSize(QSize(1100, 200))
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
        self.comboBoxEducations = QComboBox()
        self.comboBoxEducations.addItems([str(i[0]) for i in educationsTable.show_educations_table()])
        labelEduId = QLabel("Код образования")
        self.labelStatus = QLabel()
        self.labelStatus.setFixedHeight(45)
        self.labelStatus.setAlignment(Qt.AlignmentFlag.AlignCenter)
        layoutInputsAndLabels.addWidget(labelName, 0,0)
        layoutInputsAndLabels.addWidget(labelPhoneNUmber, 0,1)
        layoutInputsAndLabels.addWidget(labelEduId, 0,2)
        layoutInputsAndLabels.addWidget(self.inputName, 1,0)
        layoutInputsAndLabels.addWidget(self.inputPhoneNumber, 1,1)
        layoutInputsAndLabels.addWidget(self.comboBoxEducations, 1,2)
        layoutBtns.addWidget(btnAdd)
        layoutItems.addLayout(layoutInputsAndLabels)
        layoutItems.addLayout(layoutBtns)
        layoutItems.addWidget(self.labelStatus)
        self.table = QtWidgets.QTableView()
        self.clmns = ["Код сотрудника", "ФИО", "Номер телефона", "Тип образования" ]
        self.data = pd.DataFrame(lst, index = range(1,len(lst) + 1), columns = self.clmns)
        self.model = TableModel(self.data)
        self.table.setModel(self.model)
        layout.addLayout(layoutItems)
        layout.addWidget(self.table)
        self.table.resizeColumnsToContents()
        self.setLayout(layout)
        btnAdd.clicked.connect(self.adding)
    def adding(self):
        surname = self.inputName.text()
        phoneNum = self.inputPhoneNumber.text()
        eduId = int(self.comboBoxEducations.currentText())
        self.inputName.clear()
        self.inputPhoneNumber.clear()
        res = employeesTable.add_to_employees_table(surname=surname, phone_num=phoneNum, edu_id=eduId)
        if res == "repeat":
            self.labelStatus.setText("Уже есть такой сотрудник")
        else:
            self.labelStatus.setText("Успешно")
        lst = employeesTable.show_employees_table()
        self.data = pd.DataFrame(lst, index = range(1,len(lst) + 1), columns = self.clmns)
        self.model = TableModel(self.data)
        self.table.setModel(self.model)
        self.table.resizeColumnsToContents()
        window.employees.table.setModel(self.model)
        window.employees.table.resizeColumnsToContents()

#Удаление сотрудника
class employeesWindowDeletion(QWidget):
    def __init__(self):
        super().__init__()
        self.setWindowTitle("Удаление сотрудника")
        self.setFixedSize(QSize(900, 200))
        layoutInputsAndLabels = QGridLayout()
        layoutBtns = QHBoxLayout()
        layout = QHBoxLayout()
        layoutItems = QVBoxLayout()
        self.inputId = QLineEdit()
        self.inputId.setFixedSize(QSize(150, 25))
        btnDel = QPushButton(text = "Удалить")
        btnDel.setFixedSize(170, 30)
        labelId = QLabel("Код сотрудника(число)")
        self.labelStatus = QLabel()
        self.labelStatus.setFixedHeight(45)
        self.labelStatus.setAlignment(Qt.AlignmentFlag.AlignCenter)
        layoutInputsAndLabels.addWidget(labelId, 0,0)
        layoutInputsAndLabels.addWidget(self.inputId, 1,0)
        layoutBtns.addWidget(btnDel)
        layoutItems.addLayout(layoutInputsAndLabels)
        layoutItems.addLayout(layoutBtns)
        layoutItems.addWidget(self.labelStatus)
        self.table = QtWidgets.QTableView()
        self.clmns = ["Код сотрудника", "ФИО", "Номер телефона", "Тип образования" ]
        lst = employeesTable.show_employees_table()
        self.data = pd.DataFrame(lst, index = range(1,len(lst) + 1), columns = self.clmns)
        self.model = TableModel(self.data)
        self.table.setModel(self.model)
        layout.addLayout(layoutItems)
        layout.addWidget(self.table)
        self.table.resizeColumnsToContents()
        self.setLayout(layout)
        btnDel.clicked.connect(self.deletion)
    def deletion(self):
        employeeId = int(self.inputId.text())
        self.inputId.clear()
        res = employeesTable.delete_from_employees_table(employee_id=employeeId)
        if res == "Not in table":
            self.labelStatus.setText("Ключа нет в таблице")
        else:
            self.labelStatus.setText("Успешно")
        lst = employeesTable.show_employees_table()
        self.data = pd.DataFrame(lst, index = range(1,len(lst) + 1), columns = self.clmns)
        self.model = TableModel(self.data)
        self.table.setModel(self.model)
        window.employees.table.setModel(self.model)
        
#Изменение данных сотрудника
class employeesWindowChanging(QWidget):
    def __init__(self):
        super().__init__()
        self.setWindowTitle("Изменение данных сотрудника")
        self.setFixedSize(QSize(1200, 200))
        layoutInputsAndLabels = QGridLayout()
        layoutBtns = QHBoxLayout()
        layoutItems = QVBoxLayout()
        layout = QHBoxLayout()
        self.inputId = QLineEdit()
        self.inputName = QLineEdit()
        self.inputPhoneNumber = QLineEdit()
        self.comboBoxEduId = QComboBox()
        self.comboBoxEduId.addItems([str(i[0]) for i in educationsTable.show_educations_table()])
        btnChange = QPushButton(text = "Изменить")
        btnChange.setFixedSize(170, 30)
        labelId = QLabel("Код сотрудника")
        labelName = QLabel("ФИО(строка) новое")
        labelPhoneNUmber = QLabel("номер телефона(строка) новое")
        labelEduId = QLabel("Код образования новое")
        self.labelStatus = QLabel()
        self.labelStatus.setFixedHeight(45)
        self.labelStatus.setAlignment(Qt.AlignmentFlag.AlignCenter)
        layoutInputsAndLabels.addWidget(labelId, 0,0)
        layoutInputsAndLabels.addWidget(labelName, 0,1)
        layoutInputsAndLabels.addWidget(labelPhoneNUmber, 0,2)
        layoutInputsAndLabels.addWidget(labelEduId, 0,3)
        layoutInputsAndLabels.addWidget(self.inputId, 1,0)
        layoutInputsAndLabels.addWidget(self.inputName, 1,1)
        layoutInputsAndLabels.addWidget(self.inputPhoneNumber, 1,2)
        layoutInputsAndLabels.addWidget(self.comboBoxEduId, 1,3)
        layoutBtns.addWidget(btnChange)
        layoutItems.addLayout(layoutInputsAndLabels)
        layoutItems.addLayout(layoutBtns)
        layoutItems.addWidget(self.labelStatus)
        self.table = QtWidgets.QTableView()
        self.clmns = ["Код сотрудника", "ФИО", "Номер телефона", "Тип образования" ]
        lst = employeesTable.show_employees_table()
        self.data = pd.DataFrame(lst, index = range(1,len(lst) + 1), columns = self.clmns)
        self.model = TableModel(self.data)
        self.table.setModel(self.model)
        layout.addLayout(layoutItems)
        layout.addWidget(self.table)
        self.table.resizeColumnsToContents()
        self.setLayout(layout)
        btnChange.clicked.connect(self.changing)
        
    def changing(self):
        employeeId = int(self.inputId.text())
        surnameNew = self.inputName.text()
        phoneNum = self.inputPhoneNumber.text()
        eduId = self.comboBoxEduId.currentText()
        self.inputId.clear()
        self.inputName.clear()
        self.inputPhoneNumber.clear()
        res = employeesTable.update_employees_table(employee_id=employeeId, surname=surnameNew, phone_number=phoneNum, edu_id=eduId)
        if res == "Not in table":
            self.labelStatus.setText("Ключа нет в таблице")
        else:
            self.labelStatus.setText("Успешно")
        lst = employeesTable.show_employees_table()
        self.data = pd.DataFrame(lst, index = range(1,len(lst) + 1), columns = self.clmns)
        self.model = TableModel(self.data)
        self.table.setModel(self.model)
        window.employees.table.setModel(self.model)

#Главное окно по сотрудникам
class employeesWindow(QWidget):
    def __init__(self):
        super().__init__()
        self.setFixedSize(QSize(800, 400))
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
        clmns = ["Код сотрудника", "ФИО", "Номер телефона", "Тип образования" ]
        lst = employeesTable.show_employees_table()
        data = pd.DataFrame(lst, index = range(1,len(lst) + 1), columns = clmns)
        self.model = TableModel(data)
        self.table.setModel(self.model)
        layout.addLayout(layoutItems)
        layout.addWidget(self.table)
        self.table.resizeColumnsToContents()
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
        self.setFixedSize(QSize(1400, 300))
        layoutInputsAndLabels = QGridLayout()
        layoutBtns = QHBoxLayout()
        layoutItems = QVBoxLayout()
        layout = QHBoxLayout()
        self.comboBoxInputIdEmployee = QComboBox()
        self.inputDate = QLineEdit()
        self.comboBoxIdPost = QComboBox()
        self.comboBoxIdUnit = QComboBox()
        self.inputSalary = QLineEdit()
        btnAdd = QPushButton(text = "Добавить")
        btnAdd.setFixedSize(170, 30)
        labelIdEmployee= QLabel("Сотрудник")
        labelDate = QLabel("Дата назначения")
        labelIdPost = QLabel("Должноость")
        labelIdUnit = QLabel("Подразделение")
        labelSalary = QLabel("ЗП")
        self.labelStatus = QLabel()
        self.labelStatus.setFixedHeight(45)
        self.labelStatus.setAlignment(Qt.AlignmentFlag.AlignCenter)
        self.comboBoxInputIdEmployee.addItems(str(i[1]) for i in employeesTable.show_employees_table())
        self.comboBoxIdPost.addItems([str(i[1]) for i in positionsTable.show_positions_table()])
        self.comboBoxIdUnit.addItems([str(i[1]) for i in unitsTable.show_units_table()])
        layoutInputsAndLabels.addWidget(labelIdEmployee, 0,0)
        layoutInputsAndLabels.addWidget(labelDate, 0,1)
        layoutInputsAndLabels.addWidget(labelIdPost, 0,2)
        layoutInputsAndLabels.addWidget(labelIdUnit,0,3)
        layoutInputsAndLabels.addWidget(labelSalary, 0,4)
        layoutInputsAndLabels.addWidget(self.comboBoxInputIdEmployee, 1,0)
        layoutInputsAndLabels.addWidget(self.inputDate, 1,1)
        layoutInputsAndLabels.addWidget(self.comboBoxIdPost, 1,2)
        layoutInputsAndLabels.addWidget(self.comboBoxIdUnit, 1,3)
        layoutInputsAndLabels.addWidget(self.inputSalary, 1,4)
        layoutBtns.addWidget(btnAdd)
        layoutItems.addLayout(layoutInputsAndLabels)
        layoutItems.addLayout(layoutBtns)
        layoutItems.addWidget(self.labelStatus)
        self.table = QtWidgets.QTableView()
        self.clmns = ["Сотрудник","Дата назначения", "Должность", "Отделение", "Зарплата"]
        lst = stringsTable.show_string_a_table()
        self.data = pd.DataFrame(lst, index = range(1,len(lst) + 1), columns = self.clmns)
        self.model = TableModel(self.data)
        self.table.setModel(self.model)
        layout.addLayout(layoutItems)
        layout.addWidget(self.table)
        self.table.resizeColumnsToContents()
        self.setLayout(layout)
        btnAdd.clicked.connect(self.adding)
    def adding(self):
        emplName = self.comboBoxInputIdEmployee.currentText()
        postName = self.comboBoxIdPost.currentText()
        unitName = self.comboBoxIdUnit.currentText()
        emplId = [x[0] for x in employeesTable.show_employees_table() if x[1] == emplName][0]
        assgnDate = self.inputDate.text()
        postId = [x[0] for x in positionsTable.show_positions_table() if x[1] == postName][0]
        unitId = [x[0] for x in unitsTable.show_units_table() if x[1] == unitName][0]
        salary = self.inputSalary.text()
        self.inputDate.clear()
        self.inputSalary.clear()
        res = stringsTable.add_to_string_a_table(empl_id=emplId, assign_date=assgnDate, post_id=postId, unit_id=unitId, salary=salary)
        if res == "Invalid date":
            self.labelStatus.setText("Неверная дата или она не задана")
        elif res == "Invalid salary":
            self.labelStatus.setText("Неверная зп или она не задана")
        else:
            self.labelStatus.setText("Успешно")
        lst = stringsTable.show_string_a_table()
        self.data = pd.DataFrame(lst, index = range(1,len(lst) + 1), columns = self.clmns)
        self.model = TableModel(self.data)
        self.table.setModel(self.model)
        window.strings.table.setModel(self.model)

#Удаление записи
class stringsWindowDeletion(QWidget):
    def __init__(self):
        super().__init__()
        self.setWindowTitle("Удаление строки")
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
        self.labelStatus = QLabel()
        self.labelStatus.setFixedHeight(45)
        self.labelStatus.setAlignment(Qt.AlignmentFlag.AlignCenter)
        layoutInputsAndLabels.addWidget(labelIdString, 0,0)
        layoutInputsAndLabels.addWidget(self.inputIdString, 1,0)
        layoutBtns.addWidget(btnDel)
        layoutItems.addLayout(layoutInputsAndLabels)
        layoutItems.addLayout(layoutBtns)
        layoutItems.addWidget(self.labelStatus)
        self.table = QtWidgets.QTableView()
        self.clmns = ["Id строки","Сотрудник","Дата назначения", "Должность", "Отделение", "Зарплата"]
        lst = stringsTable.show_string_a_table_with_ids()
        self.data = pd.DataFrame(lst, index = range(1,len(lst) + 1), columns = self.clmns)
        self.model = TableModel(self.data)
        self.table.setModel(self.model)
        layout.addLayout(layoutItems)
        layout.addWidget(self.table)
        self.setLayout(layout)
        self.table.resizeColumnsToContents()
        btnDel.clicked.connect(self.deletion)
    def deletion(self):
        stringId = int(self.inputIdString.text())
        self.inputIdString.clear()
        res = stringsTable.delete_from_string_a_table(string_id= stringId)
        if res == "Not in table":
            self.labelStatus.setText("Ключа нет в таблице")
        else:
            self.labelStatus.setText("Успешно")
            print("")
        lst = stringsTable.show_string_a_table_with_ids()
        self.data = pd.DataFrame(lst, index = range(1,len(lst) + 1), columns = self.clmns)
        self.model = TableModel(self.data)
        self.table.setModel(self.model)

#Изменение данных записи
class stringsWindowChanging(QWidget):
    def __init__(self):
        super().__init__()
        self.setWindowTitle("Изменение строки")
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
        labelDate = QLabel("Дата назначения новая")
        labelSalary = QLabel("ЗП новая")
        self.labelStatus = QLabel()
        self.labelStatus.setFixedHeight(45)
        self.labelStatus.setAlignment(Qt.AlignmentFlag.AlignCenter)
        layoutInputsAndLabels.addWidget(labelId, 0,0)
        layoutInputsAndLabels.addWidget(labelDate, 0,1)
        layoutInputsAndLabels.addWidget(labelSalary, 0,2)
        layoutInputsAndLabels.addWidget(self.inputId, 1,0)
        layoutInputsAndLabels.addWidget(self.inputDate, 1,1)
        layoutInputsAndLabels.addWidget(self.inputSalary, 1,2)
        layoutBtns.addWidget(btnChange)
        layoutItems.addLayout(layoutInputsAndLabels)
        layoutItems.addLayout(layoutBtns)
        layoutItems.addWidget(self.labelStatus)
        self.table = QtWidgets.QTableView()
        self.clmns = ["id строки", "Сотрудник", "Дата назначения", "ЗП"]
        lst = [(x[0], x[1], x[2],x[-1]) for x in stringsTable.show_string_a_table_with_ids()]
        self.data = pd.DataFrame(lst, index = range(1,len(lst) + 1), columns = self.clmns)
        self.model = TableModel(self.data)
        self.table.setModel(self.model)
        layout.addLayout(layoutItems)
        layout.addWidget(self.table)
        self.setLayout(layout)
        self.table.resizeColumnsToContents()
        btnChange.clicked.connect(self.changing)
    def changing(self):
        stringId = int(self.inputId.text())
        date = self.inputDate.text()
        salary = self.inputSalary.text()
        self.inputId.clear()
        self.inputDate.clear()
        self.inputSalary.clear()
        res = stringsTable.update_string_a_table(string_id=stringId, assign_date=date, salary=salary)
        if res == "Invalid date":
            self.labelStatus.setText("Неверная дата или она не задана")
        elif res == "Invalid salary":
            self.labelStatus.setText("Неверная зп или она не задана")
        elif res == "Not in table":
            self.labelStatus.setText("Ключа нет в таблице")
        else:
            self.labelStatus.setText("Успешно")
        lst = [(x[0], x[1], x[2],x[-1]) for x in stringsTable.show_string_a_table_with_ids()]
        self.data = pd.DataFrame(lst, index = range(1,len(lst) + 1), columns = self.clmns)
        self.model = TableModel(self.data)
        self.table.setModel(self.model)

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
        clmns = ["Сотрудник","Дата назначения", "Должность", "Отделение", "Зарплата"]
        lst = stringsTable.show_string_a_table()
        data = pd.DataFrame(lst, index = range(1,len(lst) + 1), columns = clmns)
        self.model = TableModel(data)
        self.table.setModel(self.model)
        layout.addLayout(layoutItems)
        layout.addWidget(self.table)
        self.table.resizeColumnsToContents()
        self.setLayout(layout)
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
        self.setFixedSize(QSize(700, 400))
        self.setWindowTitle("Главное окно")
        
        btnEducations = QPushButton(text = "Образование")
        btnEducations.setFixedSize(140, 60)
        btnUnits = QPushButton(text = "Отделения")
        btnUnits.setFixedSize(140, 60)
        btnPositions = QPushButton(text = "Должности")
        btnPositions.setFixedSize(140, 60)
        btnEmployees = QPushButton(text = "Сотрудники")
        btnEmployees.setFixedSize(140, 60)
        btnByEducations = QPushButton(text = "По образованиям")
        btnByEducations.setFixedSize(140, 60)
        btnByUnits = QPushButton(text = "По отделением")
        btnByUnits.setFixedSize(140, 60)
        btnByPositions = QPushButton(text = "По должностям")
        btnByPositions.setFixedSize(140, 60)
        btnStrings = QPushButton(text = "Записи назначений")
        btnStrings.setFixedSize(140,60)
        layout = QGridLayout()
        layout.addWidget(btnEducations,0,0)
        layout.addWidget(btnUnits,0,1)
        layout.addWidget(btnPositions,0,2)
        layout.addWidget(btnEmployees,0,3)
        layout.addWidget(btnByEducations,1,0)
        layout.addWidget(btnByUnits,1,1)
        layout.addWidget(btnByPositions,1,2)
        layout.addWidget(btnStrings, 1,3)
        self.setLayout(layout)
        
        btnEducations.clicked.connect(self.show_education_window)
        btnUnits.clicked.connect(self.show_units_window)
        btnPositions.clicked.connect(self.show_positions_window)
        btnEmployees.clicked.connect(self.show_employees_window)
        btnStrings.clicked.connect(self.show_strings_window)
        btnByEducations.clicked.connect(self.show_byEducations_window)
        btnByUnits.clicked.connect(self.show_byUnits_window)
        btnByPositions.clicked.connect(self.show_byPositions_window)
        
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
        
    def show_byEducations_window(self):
        self.byEducation = checkByEducations()
        self.byEducation.show()
    
    def show_byUnits_window(self):
        self.byUnits = checkByUnits()
        self.byUnits.show()

    def show_byPositions_window(self):
        self.byPositions = checkByPositions()
        self.byPositions.show()
        
app = QApplication([])

window = MainWindow()
window.show()
app.exec()