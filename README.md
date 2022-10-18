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
