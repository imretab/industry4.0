import requests
from bs4 import BeautifulSoup
from tkinter import *
from tkcalendar import Calendar
import pandas as pd
import matplotlib.pyplot as plt

root = Tk()
root.geometry("1024x768")
cal = Calendar(root,selectmode='day',date_pattern='y. mm. dd.')
cal.pack(pady = 20)
def showStats():
    with requests.Session() as connection:
        main_url = "https://bet.szerencsejatek.hu/jatekok/putto/sorsolasok/"
        r = connection.get(main_url)
        data ={
        "CSRF_9cd258d5":"ZTlMfnpiekRra3k2OWpENjU5RTJYak84TlNkQmNqQlXtDFKpNW-j1xFz7elUmYbF7vrgwDemX9L22i96JVExHA==",
        "date":cal.get_date(),
        "yt2": "Keresés"
        }
        connection.headers.update(
            {
                "cookie": "CSRF_9cd258d5=ZTlMfnpiekRra3k2OWpENjU5RTJYak84TlNkQmNqQlXtDFKpNW-j1xFz7elUmYbF7vrgwDemX9L22i96JVExHA%3D%3D; dtCookie=v_4_srv_1_sn_815ADF7E94366B7A2822B7208DC364FD_perc_100000_ol_0_mul_1_app-3A1226c3b62c34ec28_0_rcs-3Acss_0"
            }
        )
        r = connection.post(main_url,data=data)
        soup = BeautifulSoup(r.content,'html.parser')
        table = soup.find('table')
        headings = [th.get_text().strip() for th in table.find("tr").find_all("th")]
        tbody = soup.find('tbody')
        datasets = []
        for row in tbody.find_all("tr")[0:]: 
            dataset = list((td.get_text() for td in row.find_all("div")))
            datasets.append(dataset)
        dataFrame = pd.DataFrame(datasets)
        renameColums = dataFrame.rename(columns={0:headings[0],1:headings[1],2:headings[2],3:headings[3]})
        renameColums.to_csv('huzasok.csv',sep=';',encoding='utf-8')
        df = pd.read_csv('huzasok.csv',sep=';')
        a_field_count = {}
        for index, row in df.iterrows():
            list_str = str(row.iloc[3])
            list_data = [int(x.strip()) for x in list_str.split(',')]
            for item in list_data:
                a_field_count[item] = a_field_count.get(item,0)+1
        b_field_counts = df['"B" mező'].value_counts()
        a_sorted = dict(sorted(a_field_count.items()))
        b_sorted = dict(sorted(b_field_counts.items()))
        plt.subplot(1,2,1)
        plt.bar(range(len(a_sorted)),list(a_sorted.values()))
        plt.xticks(range(len(a_sorted)), list(a_sorted.keys()),size=7)
        plt.title('Draws in field "A"',size=10)
        plt.subplot(1,2,2)
        plt.title('Draws in field "B"',size=10)
        plt.bar(range(len(b_sorted)),list(b_sorted.values()))
        plt.xticks(range(len(b_sorted)), list(b_sorted.keys()),size=7)
        plt.show()
Button(root,text="Get statistics for selected date",command=showStats).pack(pady=20)
root.mainloop()