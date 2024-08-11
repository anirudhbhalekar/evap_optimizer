# This Python file uses the following encoding: utf-8
import sys
import os
from PySide6.QtWidgets import QApplication, QWidget, QFileDialog, QMessageBox, QTableWidgetItem


# Important:
# You need to run the following command to generate the ui_form.py file
#     pyside6-uic form.ui -o ui_form.py, or
#     pyside2-uic form.ui -o ui_form.py
from ui_form import Ui_EO_Window
from eo_class import EvapOptimizer

class EO_Window(QWidget):
    def __init__(self, parent=None):
        super().__init__(parent)
        self.ui = Ui_EO_Window()
        self.ui.setupUi(self)
        self.evap_opt = EvapOptimizer()
        self.ui.LoadExcelFileBttn.clicked.connect(self.load_excel_file)
        self.ui.OptimizerBttn.clicked.connect(self.optimize)
        self.ui.InspectResultsBttn.clicked.connect(self.display_excel_file)
    
    def load_excel_file(self): 
        try: 
            fileName = QFileDialog.getOpenFileName(self, "Open Excel File")
            self.evap_opt.load_file(fileName[0])
            self.evap_opt.load_forecast()
            self.display_forecast()
            
            msg = QMessageBox()
            msg.setInformativeText("Successfully Loaded Excel File")
            msg.setWindowTitle("Information")
            msg.show()

            self.ui.terminal.append("\n>Succesfully Loaded Excel File")
            self.ui.TargetLine.setText(str(self.evap_opt.target_per_tube))
            
        except Exception as ex:
            msg = QMessageBox()
            msg.setInformativeText("Could not load Excel File")
            msg.setWindowTitle("Warning")
            msg.show()
            
            self.ui.terminal.append("\n>Failed to Load Excel File")
            self.ui.terminal.append(str(ex))


    def optimize(self):
        try:
            target = float(self.ui.TargetLine.text())
            self.evap_opt.set_target(target)

        except Exception as ex:
            self.ui.terminal.append("\n>Error Writing Target to Excel File")
            self.ui.terminal.append(str(ex))

        try:
            self.ui.terminal.append("\n>Running Optimizer")
            self.evap_opt.initialise_arrays()
            self.evap_opt.optimizer()
            if not self.evap_opt.is_optimized:
                self.ui.terminal.append(f"\n>Evaporation Rate unachievable in {self.evap_opt.MAX_ITER} iterations")
                return
            self.ui.terminal.append("\n>Optimization Ended Successfully")
            self.evap_opt.store_results()
            self.ui.terminal.append("\n>Results Stored")
            self.load_controls_data()
            self.load_outlets_data()
            self.load_results_data()

        except Exception as ex:
            self.ui.terminal.append("\n>Optimization Failed")
            self.ui.terminal.append(str(ex))

    def display_forecast(self):
        try:
            self.ui.forecastTable.setRowCount(len(self.evap_opt.time_array))
            count = 0
            for time, values in zip(self.evap_opt.time_array, self.evap_opt.forecast_array):
                self.ui.forecastTable.setItem(count, 0, QTableWidgetItem(str(time)))
                self.ui.forecastTable.setItem(count, 1, QTableWidgetItem(str(values[0])))
                self.ui.forecastTable.setItem(count, 2, QTableWidgetItem(str(values[1])))
                count += 1

        except Exception as ex:
            self.ui.terminal.append("\n>Error in loading!")
            self.ui.terminal.append(str(ex))


    def display_excel_file(self):
        try:
            if sys.platform.startswith("win32"):
                os.system(f'start "excel" "{self.evap_opt.file_name}"')
            else:
                os.system(f"open -a 'Microsoft Excel' '{self.evap_opt.file_name}'")
        except Exception as ex:
            self.ui.terminal.append("\n>Failed to open excel file")
            self.ui.terminal.append(str(ex))

    def load_controls_data(self):
        self.ui.controlTable.setRowCount(len(self.evap_opt.time_array))
        for i, row in enumerate(self.evap_opt.optimal_config):
            time = self.evap_opt.time_array[i]

            self.ui.controlTable.setItem(i, 0, QTableWidgetItem(str(time)))
            self.ui.controlTable.setItem(i, 1, QTableWidgetItem(str(row[3])))
            self.ui.controlTable.setItem(i, 2, QTableWidgetItem(str(row[4])))
            self.ui.controlTable.setItem(i, 3, QTableWidgetItem(str(row[5])))

    def load_outlets_data(self):
        self.ui.outputsTable.setRowCount(len(self.evap_opt.time_array))
        for i, row in enumerate(self.evap_opt.optimal_config):
            time = self.evap_opt.time_array[i]

            self.ui.outputsTable.setItem(i, 0, QTableWidgetItem(str(time)))
            self.ui.outputsTable.setItem(i, 1, QTableWidgetItem(str(row[10])))
            self.ui.outputsTable.setItem(i, 2, QTableWidgetItem(str(row[11])))
            self.ui.outputsTable.setItem(i, 3, QTableWidgetItem(str(row[12])))

    def load_results_data(self):
        self.ui.OER_line.setText(str(round(self.evap_opt.current_evap,3)))
        self.ui.HP_line.setText(str(round(self.evap_opt.energy_consumption,3)))

def open_window():
    app = QApplication(sys.argv)
    widget = EO_Window()
    widget.show()
    sys.exit(app.exec())

if __name__ == "__main__":
    open_window()
