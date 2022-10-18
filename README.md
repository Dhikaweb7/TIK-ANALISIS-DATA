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
