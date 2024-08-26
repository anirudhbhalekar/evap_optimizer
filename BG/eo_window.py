# This Python file uses the following encoding: utf-8
import sys
import os
import requests
import datetime 
from PySide6.QtWidgets import QApplication, QWidget, QFileDialog, QMessageBox, QTableWidgetItem


# Important:
# You need to run the following command to generate the ui_form.py file
#     pyside6-uic form.ui -o ui_form.py, or
#     pyside2-uic form.ui -o ui_form.py
from ui_form import Ui_EO_Window
from eo_class import EvapOptimizer

API_KEY = 'ceae7b777cd0dedabf05c94521c97aa9'
BASE_URL = 'api.openweathermap.org'

class EO_Window(QWidget):
    def __init__(self, parent=None):
        super().__init__(parent)
        self.ui = Ui_EO_Window()
        self.ui.setupUi(self)
        self.evap_opt = EvapOptimizer()
        self.ui.LoadExcelFileBttn.clicked.connect(self.load_excel_file)
        self.ui.OptimizerBttn.clicked.connect(self.optimize)
        self.ui.InspectResultsBttn.clicked.connect(self.display_excel_file)
        self.ui.LoadForecast.clicked.connect(self.load_forecast)
    
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

            self.ui.terminal.append(">Succesfully Loaded Excel File")
            self.ui.TargetLine.setText(str(self.evap_opt.target_per_tube))
            
        except Exception as ex:
            msg = QMessageBox()
            msg.setInformativeText("Could not load Excel File")
            msg.setWindowTitle("Warning")
            msg.show()
            
            self.ui.terminal.append(">Failed to Load Excel File")
            self.ui.terminal.append(">" + str(ex))


    def optimize(self):
        try:
            target = float(self.ui.TargetLine.text())
            self.evap_opt.set_target(target)

        except Exception as ex:
            self.ui.terminal.append(">Error Writing Target to Excel File")
            self.ui.terminal.append(">" + str(ex))

        try:
            self.ui.terminal.append(">Running Optimizer")
            self.evap_opt.initialise_arrays()
            self.evap_opt.optimizer()
            if not self.evap_opt.is_optimized:
                self.ui.terminal.append(f">Evaporation Rate unachievable in {self.evap_opt.MAX_ITER} iterations")
                self.evap_opt.store_results()
                self.ui.terminal.append(">Results Stored")
                self.load_controls_data()
                self.load_outlets_data()
                self.load_results_data()
                return
            
            self.ui.terminal.append(">Optimization Ended Successfully")
            self.evap_opt.store_results()
            self.ui.terminal.append(">Results Stored")
            self.load_controls_data()
            self.load_outlets_data()
            self.load_results_data()

        except Exception as ex:
            self.ui.terminal.append(">Optimization Failed")
            self.ui.terminal.append(">" + str(ex))

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
            self.ui.terminal.append(">Error in loading!")
            self.ui.terminal.append(">" + str(ex))


    def display_excel_file(self):
        try:
            if sys.platform.startswith("win32"):
                os.system(f'start "excel" "{self.evap_opt.file_name}"')
            else:
                os.system(f"open -a 'Microsoft Excel' '{self.evap_opt.file_name}'")
        except Exception as ex:
            self.ui.terminal.append(">Failed to open excel file")
            self.ui.terminal.append(">" + str(ex))

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

    def load_forecast(self): 
        global API_KEY

        # Get date for tomorrow
        dt_text = str(datetime.date.today() + datetime.timedelta(days=1))
        loc_string = self.ui.LocationLine.text()

        if loc_string == "": 
            self.ui.terminal.append(">Location not Specified")
            return 
        loc_values = loc_string.split(',')

        city_name = loc_values[0]
        state_code = ""
        country_code = ""
    
        if len(loc_values) == 2: 
            country_code = loc_values[1]
        elif len(loc_values) == 3: 
            state_code = loc_values[1]
            country_code = loc_values[2]
        
        # Get coordinates using Geocoding API 
        geo_url = f"http://api.openweathermap.org/geo/1.0/direct?q={city_name},{state_code},{country_code}&limit={5}&appid={API_KEY}"
        
        try: 
            response = requests.get(geo_url)
            city_data = response.json()
            city_lat = city_data[0]['lat']
            city_lon = city_data[0]['lon']
            self.ui.terminal.append(">Found city location data")
            self.ui.terminal.append(">Lat : " + str(city_lat))
            self.ui.terminal.append(">Lon : " + str(city_lon))
        except Exception as ex:
            self.ui.terminal.append(">Failed to find city location data")
            self.ui.terminal.append(">" + str(ex)) 
            return 
        
        # Get forecast using OpenWeather API

        forecast_url = f"https://api.openweathermap.org/data/2.5/forecast?lat={str(city_lat)}&lon={str(city_lon)}&appid={API_KEY}"
        
        # Create dt_text array 

        dt_text_arr = []
        temp_arr = []
        rh_arr = []

        breakpoint_txt = dt_text + " 00:00:00"
        
        loc_index = None
        flag_found = False

        try: 
            response = requests.get(forecast_url)
            forecast_data = response.json()
            if forecast_data['cod'] != '200':
                self.ui.terminal.append(">Could not find forecast data")
                return 
            
            for i, list_obj in enumerate(forecast_data['list']): 
                this_date = list_obj['dt_txt']
                if this_date == breakpoint_txt: 
                    loc_index = i
                    flag_found = True
                    break
            
            if not flag_found: 
                self.ui.terminal.append(">Datetime Error")
                return 
            
            for j in range(8): 
                dt_text_arr.append(forecast_data['list'][loc_index + j]['dt_txt'])
                temp_arr.append(float(forecast_data['list'][loc_index + j]['main']['temp']) - 273.15)
                rh_arr.append(float(forecast_data['list'][loc_index + j]['main']['humidity']))
            
            print(temp_arr)
            print(rh_arr)
            self.ui.terminal.append(">Forecast retrieved successfully")
            try: 
                self.evap_opt.set_forecast(dt_text_arr, temp_arr, rh_arr)
            except Exception as ex: 
                self.ui.terminal.append(">Failed to write to excel")
                self.ui.terminal.append(">" + str(ex))
                return 
            
            self.display_forecast()
            self.ui.terminal.append(">Loaded Forecast Successfully")
            
        except Exception as ex: 
            self.ui.terminal.append(">Failed to load forecast data")
            self.ui.terminal.append(">" + str(ex)) 
            return 


def open_window():
    app = QApplication(sys.argv)
    widget = EO_Window()
    widget.show()
    sys.exit(app.exec())

if __name__ == "__main__":
    open_window()
