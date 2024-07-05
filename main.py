import os
import sys
import tkinter as tk
from tkinter import ttk
from colorama import Fore, Back, Style
import subprocess

def clear():
    os.system("cls")
    #os.system("clear")
def skip():
    for x in range(6):
        print(" ")
def skipnumber(number):
    for x in range(number):
        print(" ")
def caps():
    skipnumber(2)
    print(Fore.RED +"███╗░░░███╗░█████╗░████████╗░█████╗░██████╗░  ██████╗░░█████╗░░██████╗██╗████████╗██╗░█████╗░███╗░░██╗")
    print("████╗░████║██╔══██╗╚══██╔══╝██╔══██╗██╔══██╗  ██╔══██╗██╔══██╗██╔════╝██║╚══██╔══╝██║██╔══██╗████╗░██║")
    print("██╔████╔██║██║░░██║░░░██║░░░██║░░██║██████╔╝  ██████╔╝██║░░██║╚█████╗░██║░░░██║░░░██║██║░░██║██╔██╗██║")
    print("██║╚██╔╝██║██║░░██║░░░██║░░░██║░░██║██╔══██╗  ██╔═══╝░██║░░██║░╚═══██╗██║░░░██║░░░██║██║░░██║██║╚████║")
    print("██║░╚═╝░██║╚█████╔╝░░░██║░░░╚█████╔╝██║░░██║  ██║░░░░░╚█████╔╝██████╔╝██║░░░██║░░░██║╚█████╔╝██║░╚███║")
    print("╚═╝░░░░░╚═╝░╚════╝░░░░╚═╝░░░░╚════╝░╚═╝░░╚═╝  ╚═╝░░░░░░╚════╝░╚═════╝░╚═╝░░░╚═╝░░░╚═╝░╚════╝░╚═╝░░╚══╝" + Style.RESET_ALL + Fore.BLUE)
    for x in range(6):
        print("")
def selectlogo():
        print(Style.RESET_ALL + Fore.RED +"░██████╗███████╗██╗░░░░░███████╗░█████╗░████████╗")
        print("██╔════╝██╔════╝██║░░░░░██╔════╝██╔══██╗╚══██╔══╝")
        print("╚█████╗░█████╗░░██║░░░░░█████╗░░██║░░╚═╝░░░██║░░░")
        print("░╚═══██╗██╔══╝░░██║░░░░░██╔══╝░░██║░░██╗░░░██║░░░")
        print("██████╔╝███████╗███████╗███████╗╚█████╔╝░░░██║░░░")
        print("╚═════╝░╚══════╝╚══════╝╚══════╝░╚════╝░░░░╚═╝░░░")
        for x in range(2):
            print("")

def selectinterface():
    clear()
    skipnumber(2)
    selectlogo()
    print(Style.RESET_ALL +  Fore.RED +"1 = Terminal  2 = GUI Interface" + Style.RESET_ALL + Fore.GREEN)
    skipnumber(10)
    print("Select: ")
    while True:
        try:
            selectednummber = int(input())
            if 1 <= selectednummber <= 2:
                break
            else:
                clear()
                selectlogo()
                print("Der Wert muss zwischen 1 und 2 liegen. Bitte erneut versuchen.")
        except ValueError:
            clear()
            selectlogo()
            print("Ungültige Eingabe. Bitte eine Zahl zwischen 1 und 2 eingeben.")
    if(selectednummber == 1):
        terminal()
    elif(selectednummber == 2):
        gui()
    else:
        pass
def gui():

    # Hauptfenster erstellen
    root = tk.Tk()
    root.title("Motor Position")
    root.geometry("500x400")
    root.configure(bg="#cdc0af")

    # Titel Label
    title_label = tk.Label(root, text="Motor Position", font=("Arial", 18, "bold"), bg="#cdc0af", fg="#333")
    title_label.pack(pady=20)

    # Funktion zum Aktualisieren des Labels mit dem Wert des Sliders
    def update_label(val, label, entry):
        val = int(float(val))  # Nur ganze Zahlenwerte
        
        entry.delete(0, tk.END)
        entry.insert(0, str(val))

    # Funktion zum Aktualisieren des Sliders mit dem Wert aus dem Entry
    def update_slider(entry, slider):
        try:
            val = int(entry.get())
            slider.set(val)
        except ValueError:
            pass  # Ungültiger Wert wird ignoriert

    # Stil für Entry-Widgets festlegen
    style = ttk.Style()
    style.configure("TEntry", padding=5)

    # Erster Slider und Entry
    frame1 = tk.Frame(root, bg="#c3b6a3")
    frame1.pack(pady=10)
    slider1 = tk.Scale(frame1, from_=1, to=9, orient="horizontal", command=lambda val: update_label(val, label1, entry1), length=200, bg="#c3b6a3", fg="#333")
    slider1.pack(side="left", padx=10)
    label1 = tk.Label(frame1, text="CAN ID       ", bg="#c3b6a3", fg="#333")
    label1.pack(side="left", padx=10)
    entry1 = ttk.Entry(frame1)
    entry1.pack(side="left", padx=10)
    entry1.bind("<Return>", lambda event: update_slider(entry1, slider1))
    
    # Zweiter Slider und Entry
    frame2 = tk.Frame(root, bg="#c3b6a3")
    frame2.pack(pady=10)
    slider2 = tk.Scale(frame2, from_=1, to=3000, orient="horizontal", command=lambda val: update_label(val, label2, entry2), length=200, bg="#c3b6a3", fg="#333")
    slider2.pack(side="left", padx=10)
    label2 = tk.Label(frame2, text="Speed         ", bg="#c3b6a3", fg="#333")
    label2.pack(side="left", padx=10)
    entry2 = ttk.Entry(frame2)
    entry2.pack(side="left", padx=10)
    entry2.bind("<Return>", lambda event: update_slider(entry2, slider2))

    # Dritter Slider und Entry
    frame3 = tk.Frame(root, bg="#c3b6a3")
    frame3.pack(pady=10)
    slider3 = tk.Scale(frame3, from_=1, to=255, orient="horizontal", command=lambda val: update_label(val, label3, entry3), length=200, bg="#c3b6a3", fg="#333")
    slider3.pack(side="left", padx=10)
    label3 = tk.Label(frame3, text="Acceralition", bg="#c3b6a3", fg="#333")
    label3.pack(side="left", padx=10)
    entry3 = ttk.Entry(frame3)
    entry3.pack(side="left", padx=10)
    entry3.bind("<Return>", lambda event: update_slider(entry3, slider3))

    # Vierter Slider und Entry
    frame4 = tk.Frame(root, bg="#c3b6a3")
    frame4.pack(pady=10)
    slider4 = tk.Scale(frame4, from_=1, to=16777215, orient="horizontal", command=lambda val: update_label(val, label4, entry4), length=200, bg="#c3b6a3", fg="#333")
    slider4.pack(side="left", padx=10)
    label4 = tk.Label(frame4, text="Position     ", bg="#c3b6a3", fg="#333")
    label4.pack(side="left", padx=10)
    entry4 = ttk.Entry(frame4)
    entry4.pack(side="left", padx=10)
    entry4.bind("<Return>", lambda event: update_slider(entry4, slider4))

    # Hauptschleife starten
    root.mainloop()

def terminal():
    clear()
    caps()
    print("Enter CAN ID 1 bis 9")

    while True:
        try:
            canbyid = int(input())
            if 1 <= canbyid <= 9:
                break
            else:
                clear()
                caps()
                print("Der Wert muss zwischen 1 und 9 liegen. Bitte erneut versuchen.")
        except ValueError:
            clear()
            caps()
            print("Ungültige Eingabe. Bitte eine Zahl zwischen 1 und 9 eingeben.")
    print("Select: " + str(canbyid))
    clear()
    caps()
    clear()
    caps()
    print("Enter Speed von 1 bis 3000")

    while True:
        try:
            speedid = int(input())
            if 1 <= speedid <= 3000:
                break
            else:
                clear()
                caps()
                print("Der Wert muss zwischen 1 bis 3000 liegen. Bitte erneut versuchen.")
        except ValueError:
            clear()
            caps()
            print("Ungültige Eingabe. Bitte eine Zahl zwischen 1 bis 3000 eingeben.")
    print("Select: " + str(speedid))
    clear()
    caps()
    print("Enter Acceralition 1 bis 255")

    while True:
        try:
            acceralitionid = int(input())
            if 1 <= acceralitionid <= 255:
                break
            else:
                clear()
                caps()
                print("Der Wert muss zwischen 1 und 255 liegen. Bitte erneut versuchen.")
        except ValueError:
            print("Ungültige Eingabe. Bitte eine Zahl zwischen 1 und 255 eingeben.")
    print("Select: " + str(acceralitionid))
    clear()
    caps()
    print("Enter Position 1 bis 16777215")

    while True:
        try:
            positionid = int(input())
            if 1 <= positionid <= 16777215:
                break
            else:
                clear()
                caps()
                print("Der Wert muss zwischen 1 und 16777215 liegen. Bitte erneut versuchen.")
        except ValueError:
            clear()
            caps()
            print("Ungültige Eingabe. Bitte eine Zahl zwischen 1 und 16777215 eingeben.")
    print("Select: " + str(positionid))
    clear()



    speedidhex = hex(int(speedid))[2:]
    speedidnumbers = len(str(speedidhex))
    if speedidnumbers == 1:
        speedidenter = "00 0" + speedidhex
    elif speedidnumbers == 2:
        speedidenter = "00 " + speedidhex
    elif speedidnumbers == 3:
        speedidenter = "0" + speedidhex[:1] + " " + speedidhex[1:]
    elif speedidnumbers == 4:
        speedidenter = speedidhex

    acceralitionidhex = hex(int(acceralitionid))[2:]
    acceralitionidnumbers = len(str(acceralitionidhex))
    if acceralitionidnumbers == 1:
        acceralitionidenter = "0" + acceralitionidhex
    else:
        acceralitionidenter = acceralitionidhex

    positionidhex = hex(int(positionid))[2:]
    positionidnumbers = len(str(positionidhex))
    if positionidnumbers == 1:
        positionidenter = "00000" + str(positionidhex)[:1]
        positionidenter1 = ' '.join(positionidenter[i:i+2] for i in range(0, len(positionidenter), 2))
    elif positionidnumbers == 2:
        positionidenter = "0000" + str(positionidhex)[:2]
        positionidenter1 = ' '.join(positionidenter[i:i+2] for i in range(0, len(positionidenter), 2))
    elif positionidnumbers == 3:
        positionidenter = "000" + str(positionidhex)[:3]
        positionidenter1 = ' '.join(positionidenter[i:i+2] for i in range(0, len(positionidenter), 2))
    elif positionidnumbers == 4:
        positionidenter = "00" + str(positionidhex)[:4]
        positionidenter1 = ' '.join(positionidenter[i:i+2] for i in range(0, len(positionidenter), 2))
    elif positionidnumbers == 5:
        positionidenter = "0" + str(positionidhex)[:5]
        positionidenter1 = ' '.join(positionidenter[i:i+2] for i in range(0, len(positionidenter), 2))
    elif positionidnumbers == 6:
        positionidenter = str(positionidhex)
        positionidenter1 = ' '.join(positionidenter[i:i+2] for i in range(0, len(positionidenter), 2))


    modeidhex = hex(245)[2:]
    canbyidhex = hex(int(canbyid))
    canbyidoutput = canbyidhex.replace('x', '')



    check = int(canbyid) + int(speedid) + int(acceralitionid) + int(positionid) + int(245)
    checkhex = hex(check)[2:]
    checkhexoutput = hex(check)

    checkidnumber = len(str(checkhex))
    if checkidnumber == 1:
        checkhex = "0" + checkhex
    elif checkidnumber == 3:
        checkhex = checkhex[-2:]  #
    elif checkidnumber == 4:
        checkhex = checkhex[-3:]
    elif checkidnumber == 5:
        checkhex = checkhex[-4:]
    elif checkidnumber == 6:
        checkhex = checkhex[-8:]  #
    elif checkidnumber == 7:
        checkhex = checkhex[-6:]
    elif checkidnumber == 8:
        checkhex = checkhex[-7:]   

    caps()
    #last 2 of result so example = 2B5 --> B5
    print("======================================================")
    print(Style.RESET_ALL + Fore.RED + canbyidoutput + " " + modeidhex + " " + speedidenter + " " + acceralitionidenter + " " + positionidenter1 + " " + checkhex +"                  CRC: " + checkhexoutput + Fore.BLUE)
    print("======================================================")


    def append_to_file_if_needed(text, file_name, line_length):
        # Versuchen, die Datei im Lesemodus zu öffnen, um den bestehenden Inhalt zu lesen
        try:
            with open(file_name, 'r', encoding='utf-8') as file:
                existing_content = file.read()
        except FileNotFoundError:
            existing_content = ""
        # Öffnen der Datei im Anhängemodus ('a') zum Hinzufügen von Text
        with open(file_name, 'a', encoding='utf-8') as file:
            # Überprüfen, ob die Datei bereits Text enthält
            if existing_content:
                file.write('\n')  # Neue Zeile hinzufügen, falls bereits Text vorhanden ist
            # Text in Teile der Länge line_length aufteilen und hinzufügen
            for i in range(0, len(text), line_length):
                file.write(text[i:i+line_length] + '')

    text = canbyidoutput + " " + modeidhex + " " + speedidenter + " " + acceralitionidenter + " " + positionidenter1 + " " + checkhex + "  CRC: " + checkhexoutput
    file_name = "log.txt"
    line_length = 50
    append_to_file_if_needed(text, file_name, line_length)
    print(f"Text wurde erfolgreich in die Datei " + Style.RESET_ALL + Fore.RED + "log.txt" + Style.RESET_ALL + Fore.BLUE + " geschrieben." + Style.RESET_ALL)
    print(Fore.BLUE +f"Text wurde erfolgreich in die Datei " + Style.RESET_ALL + Fore.RED +"cangenerate.txt" + Style.RESET_ALL + Fore.BLUE +" geschrieben." + Style.RESET_ALL)
    text = canbyidoutput + " " + modeidhex + " " + speedidenter + " " + acceralitionidenter + " " + positionidenter1 + " " + checkhex
    file_name = "cangenerate.txt"
    append_to_file_if_needed(text, file_name, line_length)
    skip()
    print("1 = restart ENTER = Exit")

 
    enter = input()
    if(enter == 1):
        terminal()
    else:
        clear()


selectinterface()
