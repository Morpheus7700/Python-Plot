import pandas as pd
import matplotlib.pyplot as plt
import numpy as np

file_path = r'C:\Users\Aniket Roy\Desktop\PV Doctor Pte.ltd Project\Output\merged_data.csv'
data = pd.read_csv(file_path)

data['Date'] = pd.to_datetime(data['Date'])
data['30_day_MA'] = data['PR'].rolling(window=30).mean()

def get_colour(ghi):
    if ghi < 2:
        return 'navy'
    elif 2 <= ghi < 4:
        return 'lightblue'
    elif 4 <= ghi < 6:
        return 'orange'
    else:
        return 'brown'

plt.figure(figsize=(14,8))

plt.scatter(data['Date'], data['PR'],c=data['GHI'].apply(get_colour),label='PR (scatter)',alpha=0.6)

plt.plot(data['Date'],data['30_day_MA'],color='red',label='30-day Moving Average',linewidth=2)

budget_line = []
initial_budget = 73.9
previous_year = None

for date in data['Date']:
    year = date.year
    if previous_year is None or year != previous_year:
        if previous_year is not None:
            initial_budget *= (1 - 0.008)
        previous_year = year
    budget_line.append(initial_budget)

budget_line = budget_line[:len(data)]

plt.plot(data['Date'],budget_line, color='darkgreen', label='Budget Line',linewidth=2)

pr_7_day_avg= data['PR'].rolling(window=7).mean()
pr_30_day_avg= data['PR'].rolling(window=30).mean()
pr_60_day_avg= data['PR'].rolling(window=60).mean()

plt.text(data['Date'].iloc[-1], pr_7_day_avg.iloc[-1], f'7-day avg: {pr_7_day_avg.iloc[-1]:.2f}', color='blue', fontsize=12)
plt.text(data['Date'].iloc[-1], pr_30_day_avg.iloc[-1], f'30-day avg: {pr_30_day_avg.iloc[-1]:.2f}', color='red', fontsize=12)
plt.text(data['Date'].iloc[-1], pr_60_day_avg.iloc[-1], f'60-day avg: {pr_60_day_avg.iloc[-1]:.2f}', color='green', fontsize=12)

plt.title('PR vs Date with 30-Day Moving Average and Budget line', fontsize=14,pad=20)
plt.xlabel('Date', fontsize=14,labelpad=10)
plt.ylabel('PR', fontsize=14,labelpad=10)
plt.legend(loc='upper left',fontsize=12)

plt.xticks(rotation=45)
plt.subplots_adjust(right=0.8)
plt.tight_layout()
plt.savefig(r'C:\Users\Aniket Roy\Desktop\PV Doctor Pte.ltd Project\data\your_graph.jpg')
plt.show()