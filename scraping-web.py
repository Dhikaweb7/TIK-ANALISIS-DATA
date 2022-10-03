import requests
import pandas as pd
from bs4 import BeautifulSoup

th = "https://www.jobs.id/lowongan-kerja?kata-kunci=part time"
halaman = requests.get(th)
hasil = BeautifulSoup(halaman.content, 'html.parser')
print(hasil)
