import os
from time import sleep


a ='\033[92m'
b ='\033[91m'
c ='\033[0m'
d ='\033[34;1m'
e ='\033[35;1m'
f ='\033[36;1m'
os.system('clear')

print(a+'\____________________________________/')
os.system ('    figlet Tombol')
print(a+'\t\033[33;1mTombol Tambahan Termux >_')
print('\t\033[33;1mBy : R4M4DH4N1')
print(a+'\____________________________________/')
print('\nLoanjing...')
sleep(1)
print(b+'\n[●] Pencopotan File Lama.....')
sleep(1)
try:
      os.mkdir('/data/data/com.termux/files/home/.termux')
except:
      pass
print(a+'[●] Sukses...')
sleep(1)
print(b+'\n[●] Menambahkan File Baru.....')
sleep(1)

key = "extra-keys = [['ESC','/','-','HOME','UP','END','PGUP'],['TAB','CTRL','ALT','LEFT','DOWN','RIGHT','PGDN']]"
kontol = open('/data/data/com.termux/files/home/.termux/termux.properties','w')
kontol.write(key)
kontol.close()
sleep(1)
print(a+'[●] Sukses...')
sleep(1)
print(b+'\n[●] Pemasangan EXtra-Keys ')
sleep(2)
os.system('termux-reload-settings')
print(a+'[●] Proses Selesai !!\n '+f+'\n>_ Kata Atta Subscribe Itu Gratis.Jadi Anda Subrex   Dulu Chanel Yt Gw !\n>_ Bayar Pake Subscribe Ya !\n')
os.system ("figlet Loading..")
os.system ("xdg-open https://youtube.com/channel/UC_TtsAzujNHgM2TZzCMopkQ")