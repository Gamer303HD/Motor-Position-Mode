import os
import sys
import tkinter
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
        terminal()
    else:
        pass

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



    check = int(canbyid) + int(speedid) + int(acceralitionid) + int(positionid) + 245
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
