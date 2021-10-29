import os
import shutil
import time

excluded_files = ["airpi.sh", "airpi.py", "README.md", "LICENSE", "nohup.out"]

def unshare():
        os.system("sudo rmmod g_mass_storage")
        os.system("sudo chmod 777 /mnt/usb_share/")

def update_share():
        os.system("cd /mnt/usb_share/ && sync")
        os.system('sudo modprobe g_mass_storage file=/piusb.bin stall=0 removable=1 ro=1 iProduct="AirPi"  iSerialNumber=1234567890')

def main():
        files = os.listdir()
        for f in excluded_files:
                files.remove(f)

        if len(files) > 0 and len(files) % 2 == 0:
                print("received", files)
                for f in files:
                        if f.startswith("."):
                                os.remove(f)
                        else:
                                unshare()
                                shutil.move(f, '/mnt/usb_share/' + f)
                                update_share()

update_share()

while True:
        main()
        time.sleep(1)
