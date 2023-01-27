from tkinter import *
from tkinter import messagebox
import requests

pencere = Tk()
pencere.geometry('700x480')
pencere.resizable(False, False)
pencere.title('Son Depremler')


def filtre():
    try:
        istek = requests.get('http://127.0.0.1:3000/' + '?location=' + konumEntry.get() + '&size=' + buyuklukEntry.get())
        veri = istek.json()
        depremler = veri['earthquakes']
        depremSayisi = len(depremler)
        lbListe.delete(0, END)
        for i in depremler:
            deprem = (" " * 2 + str(i['date']) + " " * 15 + str(i['size']['ml']) + " " * 15) + i['location']
            lbListe.insert(END, deprem)

        lblKonum = Label(pencere, text='Deprem Sayısı: ' + str(depremSayisi), font=('Arial', 10))
        lblKonum.place(x=540, y=10, width=130, height=25)
    except:
        messagebox.showerror("Hata", "Hatalı filterleme yaptınız!")


lblBuyukluk = Label(pencere, text='Minimum Büyüklük', font=('Arial', 10))
lblBuyukluk.place(x=10, y=10, width=120, height=25)

buyuklukEntry = Entry(pencere, justify='center')
buyuklukEntry.insert(END, '0')
buyuklukEntry.place(x=130, y=10, width=70, height=25)

lblKonum = Label(pencere, text='Konum', font=('Arial', 10))
lblKonum.place(x=220, y=10, width=70, height=25)

konumEntry = Entry(pencere, justify='center')
konumEntry.place(x=280, y=10, width=130, height=25)

btnFiltre = Button(pencere, text='Filtrele', command=filtre, font=('Arial', 10))
btnFiltre.place(x=450, y=10, width=70, height=25)

lblListTarih = Label(pencere, text='Tarih', font=('Arial', 10))
lblListTarih.place(x=40, y=45, width=70, height=25)

lblListBuyukluk = Label(pencere, text='Büyüklük', font=('Arial', 10))
lblListBuyukluk.place(x=172, y=45, width=70, height=25)

lblListYer = Label(pencere, text='Konum', font=('Arial', 10))
lblListYer.place(x=350, y=45, width=70, height=25)

scrollbar = Scrollbar(pencere, orient="vertical")
scrollbar.pack(side="right", fill="y")

lbListe = Listbox(pencere, font=('Arial', 10), yscrollcommand=scrollbar.set)
lbListe.place(x=10, y=70, width=668, height=396)

scrollbar.config(command=lbListe.yview)

filtre()

pencere.mainloop()
