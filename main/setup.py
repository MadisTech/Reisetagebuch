'''
Dieses Pogramm erzeugt eine GUI, in dem Daten zu Ereignissen eingegeben, auf eine .csv Datei
gespeichert, aus der selben .csv Datei gelesen und gelöscht werden.

Copyright (C) 2020  MADI'S Tech

This program is free software: you can redistribute it and/or modify
it under the terms of the GNU General Public License as published by
the Free Software Foundation, either version 3 of the License, or any later version.

This program is distributed in the hope that it will be useful,
but WITHOUT ANY WARRANTY; without even the implied warranty of
MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.  See the
GNU General Public License for more details.

You should have received a copy of the GNU General Public License
along with this program.  If not, see https://www.gnu.org/licenses/.

'''
import tkinter as tk
import os
from tkinter import messagebox
from PIL import Image, ImageTk

#Front-End
root = tk.Tk()
root.configure(bg='#242254')
root.title('Reisetagebuch')
root.iconbitmap('Icon 40x40 px.ico')

logo = tk.Frame(root)
logo.grid(row=0, column=0, rowspan=2, columnspan=6)

Eingabefeld = tk.Frame(root)
Eingabefeld.grid(row=2, column=0, rowspan=5, columnspan=6)

Ausgabefeld = tk.Frame(root)
Ausgabefeld.grid(row=8, column=0, rowspan=4, columnspan=6)

#Graphische Felder
socialmedia = Image.open('GUI Header 970x250 px.png')
socialmedia.thumbnail((698.4,180))
mainSM = ImageTk.PhotoImage(socialmedia)

socialmediaL=tk.Label(logo, borderwidth=0, highlightthickness=0, image=mainSM)
socialmediaL.pack()

Eingabe = Image.open('Eingabefeld 970 x 360 px.png')
Eingabe.thumbnail((698.4,259))
mainEingabe = ImageTk.PhotoImage(Eingabe)

Eingabeframe=tk.Label(Eingabefeld, borderwidth=0, highlightthickness=0, image=mainEingabe)
Eingabeframe.pack()

Ausgabe = Image.open('Eingabefeld 970 x 360 px.png')
Ausgabe.thumbnail((698.4,259))
mainAusgabe = ImageTk.PhotoImage(Ausgabe)

Ausgabeframe=tk.Label(Ausgabefeld, borderwidth=0, highlightthickness=0, image=mainAusgabe)
Ausgabeframe.pack()

#Variablen der Eingabefelder
eindatum = tk.StringVar()
einort = tk.StringVar()
einbild = tk.StringVar()

#Variablen der Ausgabefelder
ausdatum = tk.StringVar()
ausort = tk.StringVar()
ausbild = tk.StringVar()

#GUI Funktionen
def EintragSpeichern():
    
    #Leere Einträge werden hier abgefangen
    if eindatum.get() == '':
        messagebox.showinfo('Fehler', 'Gebe bitte ein Datum ein', parent=root)

    else:
        #Information aus den Feldern Datum,Ort, Notizen und Bild werden entnommen
        a = eindatum.get()
        b = einort.get()
        c = einNotizenE.get('1.0','end')
        d = einbild.get()
            
        if os.path.isfile('Ereignisse.csv'):

            #Informationen aus Feldern werden der Speicherdatei hinzugefügt
            Ereignis = open('Ereignisse.csv', 'a')
            Ereignis.write(a + ";" + b + ";" + d + ";" + c) # c nach d, weil in c schon ein \n ist - weiß nicht genau warum.
            Ereignis.close()
            messagebox.showinfo('Eintrag', 'Eintrag wurde gespeichert', parent=root)
            
        else:
                
            Ereignis = open('Ereignisse.csv', 'w')
            Ereignis.write(a + ";" + b + ";" + d + ";" + c)
            Ereignis.close()
            messagebox.showinfo('Eintrag', 'Eintrag wurde gespeichert', parent=root)
            

def abrufen():
    global Arbeitsliste
    datei = open("Ereignisse.csv", "r")
    Arbeitsliste = datei.readlines()
    datei.close()
    
    for i in range(len(Arbeitsliste)):
        Arbeitsliste[i] = Arbeitsliste[i].split(";")
        Arbeitsliste[i][3] = Arbeitsliste[i][3].replace("\n","")
    
    #Erster Eintrag im Speicher wird in Die jeweiligen GUI Felder ausgegeben
    ausdatum.set(Arbeitsliste[0][0])
    ausort.set(Arbeitsliste[0][1])
    ausbild.set(Arbeitsliste[0][2])
    ausNotizE.delete('1.0','end')
    ausNotizE.insert('1.0', Arbeitsliste[0][3])

def EintragLöschen():
       
    a = ausdatum.get()
    b = ausort.get()
    d = ausbild.get()
    c = ausNotizE.get('1.0','end')
    vergleich1=[a, b, d]
    
    for i in range(len(Arbeitsliste)):        
        vergleich2=[Arbeitsliste[i][0], Arbeitsliste[i][1], Arbeitsliste[i][2]]    

        if vergleich1 == vergleich2:
            
            gelöscht = Arbeitsliste.pop(i)

            try:
                datei = open("Ereignisse.csv", "w")
                for i in range(len(Arbeitsliste)):
                    datei.write(Arbeitsliste[i][0] + ";" + Arbeitsliste[i][1] + ";" + Arbeitsliste[i][2] + ";" + Arbeitsliste[i][3] + "\n")
                datei.close()
                messagebox.showinfo('Löschen', 'Eintrag wurde gelöscht', parent=root)
            except:
                messagebox.showinfo('Error', 'Eintrag konnte nicht gelöscht werden', parent=root)

            try:    
                ausdatum.set(Arbeitsliste[0][0])
                ausort.set(Arbeitsliste[0][1])
                ausbild.set(Arbeitsliste[0][2])
                ausNotizE.delete('1.0','end')
                ausNotizE.insert('1.0', Arbeitsliste[0][3])
                break
            except IndexError:
                messagebox.showinfo('Fertig', 'Alle Ereignisse wurden bearbeitet', parent=root)
                ausdatum.set('')
                ausort.set('')
                ausbild.set('')
                ausNotizE.delete('1.0','end')
        else:
            continue

#GUI Widgets
#Ereigniseingabe
einEreignisL = tk.Label(root, text='Ereigniseingabe:', bg='#242254', fg='white', font=('Poppins', '18', 'bold'))
einEreignisL.grid(row=2, column=0, columnspan=2)
einEreignisB = tk.Button(root, text='Eintrag speichern', bd=0, bg='white', command=EintragSpeichern)
einEreignisB.grid(row=2, column=2, columnspan=4)

#Eingabefeld - Datum
einDatumL = tk.Label(root, text='Datum: ', bg='#242254', fg='white', font=('Poppins', '12', 'bold'))
einDatumL.grid(row=3, column=0)
einDatumE = tk.Entry(root, textvariable=eindatum, width= 40)
einDatumE.grid(row=3, column=1, columnspan=2, sticky=tk.W)

#Eingabefeld - Ort
einOrtL = tk.Label(root, text='Ort: ', bg='#242254', fg='white', font=('Poppins', '12', 'bold'))
einOrtL.grid(row=4, column=0)
einOrtE = tk.Entry(root, textvariable=einort, width= 40)
einOrtE.grid(row=4, column=1, columnspan=2, sticky=tk.W)

#Eingabefeld - Notizen
einNotizenL = tk.Label(root, text='Notizen: ', bg='#242254', fg='white', font=('Poppins', '12', 'bold'))
einNotizenL.grid(row=5, column=0, rowspan=2)
einNotizenE = tk.Text(root, height=4, width=61)
einNotizenE.grid(row=5, column=1, rowspan=2, columnspan=5, sticky=tk.W)

#Eingabefeld - Foto
einFotoL = tk.Label(root, text='Datenpfad zum Foto/Fotos: ', bg='#242254', fg='white', font=('Poppins', '12', 'bold'))
einFotoL.grid(row=3, column=3, columnspan= 3, sticky=tk.S)
einFotoE = tk.Entry(root, textvariable=einbild, width= 45)
einFotoE.grid(row=4, column=3,  columnspan=3)
    
#Ereignisausgabe
ausEreignisL = tk.Label(root, text='Ereignisausgabe:', bg='#242254', fg='white', font=('Poppins', '18', 'bold'))
ausEreignisL.grid(row=8, column=0, columnspan=2)
ausEreignisB = tk.Button(root, text='Ausgabe starten', bd=0, bg='white', command=abrufen)
ausEreignisB.grid(row=8, column=2, columnspan=4)

#Ereignisausgabe - Datum
ausDatumE = tk.Entry(root, textvariable=ausdatum, width=33)
ausDatumE.grid(row=9, column=0, columnspan=2)

#Ereignisausgabe - Ort
ausOrtE = tk.Entry(root, textvariable=ausort, width=33)
ausOrtE.grid(row=10, column=0, columnspan=2)

#Ereignisausgabe - Bild
ausBildE = tk.Entry(root, width=67, textvariable=ausbild)
ausBildE.grid(row=9, column=2, columnspan=4, sticky=tk.W)

#Ereignisausgabe - Notiz
ausNotizE = tk.Text(root, height=4, width=50)
ausNotizE.grid(row=10, column=2, columnspan=4, sticky=tk.W)

#Ereignisausgabe - Bearbeitung abschließen
ausBearbeitungL = tk.Label(root, text='Diesen Eintrag fertig bearbeitet?: ', bg='#242254', fg='white', font=('Poppins', '13', 'bold'))
ausBearbeitungL.grid(row=11, column=2, columnspan=3)
ausBearbeitungB = tk.Button(root, text='Eintrag löschen', bd=0, command=EintragLöschen)
ausBearbeitungB.grid(row=11, column=5)

root.mainloop()