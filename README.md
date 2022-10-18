# TIK-ANALISIS-DATA
Bab Analisis data

## Array

```python

data = [10, 9, 7, 8, 10, 8]
print(data[1])
data[2] = 10
print(data)
data.append(9)
print(data)

```

## Pandas DataFrame

```python

import pandas

data = [10, 9, 7, 9, 10]
siswa = ["Ragil", "Andhika", "Dafa", "Habib", "Rendy"]

nilai = pandas.DataFrame({
"Nama": siswa,
"Nilai": data
})
nilai

```

## Scraping Web

```python

import requests
import pandas as pd
from bs4 import BeautifulSoup

# link dalam th = bisa diubah sesuai ke inginan
th = "https://www.jobs.id/lowongan-kerja?kata-kunci=part time"
halaman = requests.get(th)
hasil = BeautifulSoup(halaman.content, 'html.parser')
print(hasil)

```

## Proses data scrapping menjadi diagram

```python

import requests
import pandas as pd
from bs4 import BeautifulSoup


# Mata Pelajaran TIK | ANALISIS DATA
# X TKJ 1
# SMK RADEN PAKU
# 2022

th = "https://www.jobs.id/lowongan-kerja?kata-kunci=part time"
halaman = requests.get(th)
hasil = BeautifulSoup(halaman.content, 'html.parser')
lowkers = hasil.find_all(class_="single-job-ads")

posisi = []
instansi = []
gaji = []

for p in lowkers:
 t1 = p.select("h3")
 t2 = t1[0].select("a")
 posisi.append(t2[0].get_text())

 t1 = p.select("p")
 t2 = t1[0].select("a")
 try:
   instansi.append(t2[0].get_text())
 except:
  instansi.append("-")

 t2 = t1[1].select("span")
 try:
   xgaji = t2[1].get_text()
 except:
   xgaji = t2[0].get_text()
 xgaji = xgaji.replace(".","")
 if (xgaji=="Gaji Dirahasiakan") :
  xgaji = 0
 gaji.append(xgaji);

import plotly.express as px

lowker = pd.DataFrame({
  "Posisi": posisi,
  "Instansi": instansi,
  "Gaji":gaji
})

fig = px.bar(lowker, x='Instansi', y='Gaji')
fig.show()

```
