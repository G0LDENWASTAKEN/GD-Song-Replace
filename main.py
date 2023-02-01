#imports
import time
import os

#show the title screen
print('''


░██████╗░█████╗░███╗░░██╗░██████╗░  ██████╗░███████╗██████╗░██╗░░░░░░█████╗░░█████╗░███████╗
██╔════╝██╔══██╗████╗░██║██╔════╝░  ██╔══██╗██╔════╝██╔══██╗██║░░░░░██╔══██╗██╔══██╗██╔════╝
╚█████╗░██║░░██║██╔██╗██║██║░░██╗░  ██████╔╝█████╗░░██████╔╝██║░░░░░███████║██║░░╚═╝█████╗░░
░╚═══██╗██║░░██║██║╚████║██║░░╚██╗  ██╔══██╗██╔══╝░░██╔═══╝░██║░░░░░██╔══██║██║░░██╗██╔══╝░░
██████╔╝╚█████╔╝██║░╚███║╚██████╔╝  ██║░░██║███████╗██║░░░░░███████╗██║░░██║╚█████╔╝███████╗
╚═════╝░░╚════╝░╚═╝░░╚══╝░╚═════╝░  ╚═╝░░╚═╝╚══════╝╚═╝░░░░░╚══════╝╚═╝░░╚═╝░╚════╝░╚══════╝

''')

#formatting
print('''
''')

#tell user to rename file before continuing
print("Make sure to rename the custom song to the song ID you want to replace!")
time.sleep(1)

#formatting
print('''
''')

#asks user to input the file name to move
file_name = input("Enter the song ID of the song you want to replace. Make sure to include the '.mp3':  ")

#defines the folder to move to
destination = os.path.join(os.path.join(os.environ['USERPROFILE']), 'AppData/Local/GeometryDash/')

#defines the original song file to delete, so it can be replaced without error.
og_file = os.path.join(os.path.join(os.environ['USERPROFILE']), f'AppData/Local/GeometryDash/{file_name}')


#deletes original song file
if os.path.exists(og_file):
    os.remove(og_file)

#tries to move the custom song into the game files
try:
    os.rename(file_name, os.path.join(destination, file_name))
    print("File moved successfully! You can now open Geometry Dash.")
    time.sleep(5)

#If the file is not found, tell the user instead of crashing.
except FileNotFoundError:
    print("Error: File not found")
    time.sleep(3)
except Exception as e:
    print("Error:", e)
    time.sleep(3)
    


