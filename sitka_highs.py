# Made By Deadcode
import csv

from datetime import datetime

import matplotlib.pyplot as plt


# CSV File name.
filename = 'sitka_weather_2018_simple.csv'

with open (filename) as f:
    reader = csv.reader(f)
    header_row = next(reader)
    # print(header_row)

    """
    for index, column_header in  enumerate(header_row):
        print(index, column_header)
    """

    # Get Dates, and High and low Temperatures from this file.
    
    dates,highs,lows = [],[],[]
    for row in reader:
        current_date = datetime.strptime(row[2],'%Y-%m-%d')
        high = int(row[5])
        low = int(row[6])
        dates.append(current_date)
        highs.append(high)
        lows.append(low)
    print(highs)
    
### Matplotlib ###

#Plot tthe High and Low temperatures.
plt.style.use('bmh')
fig,ax = plt.subplots(figsize=(15,9))
ax.plot(dates,highs, c = 'red',alpha=0.5)
ax.plot(dates,lows,c = 'blue',alpha=0.5)
plt.fill_between(dates,highs,lows,facecolor='blue',alpha=0.1)

#Format Plot.
plt.title("Daile High and Low temperatures - 2018", fontsize = 24)
plt.xlabel('',fontsize=16)
fig.autofmt_xdate()
plt.ylabel('Temperature (F)',fontsize=16)
plt.tick_params(axis='both',which='major', labelsize=16)

# Create Image Name
file_path = 'img_name.txt'
with open(file_path) as f:
    old_name = f.read().strip()
if old_name == '':
    new_name = 0
else:
    new_name = int(old_name) + 1
with open(file_path, 'w') as f:
    f.write(str(new_name))

plt.savefig(f'sitka_weather{new_name}.png', bbox_inches='tight')
plt.show()
