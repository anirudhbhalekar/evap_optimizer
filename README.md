# evap_optimizer
Evaporation Optimizer Forecast Application 

On Windows run: ```launcher.exe```

## Steps to run application: 
Refer to ```UI.png``` for layout

### Step 1
Load the excel file using the ```Load Excel File``` button (then clicking on database.xlsx)

The terminal should read that the file has loaded successfully

### Step 2
Enter the location of the site in the corresponding text field (middle panel) and then click ```Load Tomorrow's Forecast```

The forecast should load successfully (note terminal messages). If not, try specifying the country/state of the place, 

(Lat/Lon entries will be added in a future update)

### Step 3 
Set the target evaporation volume (this will be Litres/Day) in the corresponding text field

### Step 4 
Run the optimization by clicking ```Run Optimizer```

### Step 5
Check if optimization succeeds by clicking on the ```Results``` tab on the right-hand table, heating power and fan power will be given here

Also note outlet conditions in the ```Outlets``` Tab

The inputs necessary to achieve result will be given in the ```Controls``` tab, values can be scraped and fed into the machine (API for this will be available soon)   

Note: this application uses openweathermap.org for forecast loading (API Key is free, available on request if source-code modifications need to be made) 
