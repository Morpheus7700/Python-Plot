import os
import pandas as pd

def merge_data(pr_folder,ghi_folder, output_file):
    data=[]

    for year_month in os.listdir(pr_folder):
        pr_folder_path = os.path.join(pr_folder,year_month)
        ghi_folder_path = os.path.join(ghi_folder,year_month)

        if os.path.isdir(pr_folder_path) and os.path.isdir(ghi_folder_path):

            for pr_file in os.listdir(pr_folder_path):
                if pr_file.endswith(".csv"):
                    pr_file_path = os.path.join(pr_folder_path,pr_file)
                    pr_data = pd.read_csv(pr_file_path)

                    pr_data['Date'] = pd.to_datetime(pr_data['Date'])
                    pr_data = pr_data[['Date', 'PR']]

                    ghi_file_path = os.path.join(ghi_folder_path,pr_file)

                    if os.path.exists(ghi_file_path):
                        ghi_data = pd.read_csv(ghi_file_path)

                        ghi_data['Date'] = pd.to_datetime(ghi_data['Date'])
                        ghi_data = ghi_data[['Date', 'GHI']]

                        merged_data = pd.merge(pr_data,ghi_data,on='Date',how = 'inner')

                        data.append(merged_data)

    final_data = pd.concat(data, ignore_index=True)
    final_data.to_csv(output_file,index=False)

pr_folder = r'C:\Users\Aniket Roy\Desktop\PV Doctor Pte.ltd Project\data\PR'
ghi_folder =  r'C:\Users\Aniket Roy\Desktop\PV Doctor Pte.ltd Project\data\GHI'
output_file = r'C:\Users\Aniket Roy\Desktop\PV Doctor Pte.ltd Project\data\merged_data.csv'

merge_data(pr_folder, ghi_folder, output_file)