from win32com.client import Dispatch
import PhysxCal

FSO = Dispatch('Scripting.FileSystemObject')
listDrives = FSO.Drives

for entry in listDrives:
    try:
       if entry.DriveLetter == 'C':
           HD_SerialNumber = entry.SerialNumber
    except:
        print("Problem!")

try:
    with open("PhysxInit.txt","r") as file:
        file_info = file.readline()
        if str(file_info[:10]) == str(HD_SerialNumber):
            PhysxCal.Main.mainFrame(0)
except:
    f = open("PhysxInit.txt", "w")
    f.write(str(HD_SerialNumber))
    f.close()
    try:
        with open("PhysxInit.txt", "r") as file:
            file_info = file.readline()
            if str(file_info[:10]) == str(HD_SerialNumber):
                PhysxCal.Main.mainFrame(0)
    except:
        pass

