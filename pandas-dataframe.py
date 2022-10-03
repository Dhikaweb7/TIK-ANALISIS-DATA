import pandas

data = [10, 9, 7, 9, 10]
siswa = ["Ragil", "Andhika", "Dafa", "Habib", "Rendy"]

nilai = pandas.DataFrame({
"Nama": siswa,
"Nilai": data
})
nilai
