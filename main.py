import sys
from PyQt5.QtWidgets import (
    QApplication, QWidget, QVBoxLayout, QTableWidget, QTableWidgetItem,
    QPushButton, QFileDialog, QLabel
)
from pymongo import MongoClient
import matplotlib.pyplot as plt
import csv

class ProjektApp(QWidget):
    def __init__(self):
        super().__init__()
        self.setWindowTitle("Zarządzanie projektami")
        self.resize(800, 600)
        self.layout = QVBoxLayout()
        self.setLayout(self.layout)

        self.table = QTableWidget()
        self.layout.addWidget(self.table)

        self.load_button = QPushButton("Załaduj dane")
        self.load_button.clicked.connect(self.load_data)
        self.layout.addWidget(self.load_button)

        self.export_button = QPushButton("Eksportuj do CSV")
        self.export_button.clicked.connect(self.export_to_csv)
        self.layout.addWidget(self.export_button)

        self.plot_button = QPushButton("Pokaż wykresy")
        self.plot_button.clicked.connect(self.show_charts)
        self.layout.addWidget(self.plot_button)

        self.client = MongoClient("mongodb://localhost:27017/")
        self.db = self.client["projektyDB"]
        self.collection = self.db["projekty"]

    def load_data(self):
        projects = list(self.collection.find())
        self.table.setRowCount(len(projects))
        self.table.setColumnCount(6)
        self.table.setHorizontalHeaderLabels(
            ["Nazwa", "Status", "Termin", "Postęp (%)", "Budżet (PLN)", "Wydatki (PLN)"]
        )
        for row, project in enumerate(projects):
            self.table.setItem(row, 0, QTableWidgetItem(project["nazwa"]))
            self.table.setItem(row, 1, QTableWidgetItem(project["status"]))
            self.table.setItem(row, 2, QTableWidgetItem(project["termin"]))
            self.table.setItem(row, 3, QTableWidgetItem(str(project["postep"])))
            self.table.setItem(row, 4, QTableWidgetItem(str(project["budzet"])))
            self.table.setItem(row, 5, QTableWidgetItem(str(project["wydatki"])))

    def export_to_csv(self):
        path, _ = QFileDialog.getSaveFileName(self, "Zapisz jako", "", "CSV files (*.csv)")
        if path:
            with open(path, 'w', newline='', encoding='utf-8') as file:
                writer = csv.writer(file)
                headers = ["Nazwa", "Status", "Termin", "Postęp (%)", "Budżet (PLN)", "Wydatki (PLN)"]
                writer.writerow(headers)
                for row in range(self.table.rowCount()):
                    data = []
                    for col in range(self.table.columnCount()):
                        item = self.table.item(row, col)
                        data.append(item.text() if item else "")
                    writer.writerow(data)

    def show_charts(self):
        projects = list(self.collection.find())
        names = [p["nazwa"] for p in projects]
        postepy = [p["postep"] for p in projects]

        plt.figure()
        plt.bar(names, postepy)
        plt.xlabel("Projekty")
        plt.ylabel("Postęp (%)")
        plt.title("Postęp projektów")
        plt.xticks(rotation=45)
        plt.tight_layout()
        plt.show()

if __name__ == "__main__":
    app = QApplication(sys.argv)
    window = ProjektApp()
    window.show()
    sys.exit(app.exec_())
