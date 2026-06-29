import psutil
import time
import pydirectinput
import keyboard
import subprocess 
import pyperclip
import os # NEW: The tool to find exact file locations

def is_portal2_running():
    for process in psutil.process_iter(['name']):
        if process.info['name'] and process.info['name'].lower() == 'portal2.exe':
            return True
    return False

def paste_to_console(command_text):
    pyperclip.copy(command_text)
    time.sleep(0.1)
    pydirectinput.keyDown('ctrl')
    pydirectinput.press('v')
    pydirectinput.keyUp('ctrl')
    time.sleep(0.1)
    pydirectinput.press('enter')

print("Portbot Launcher Started!")
print("Waiting for portal2.exe...")

while not is_portal2_running():
    time.sleep(2)

print("Portal 2 found! Portbot is standing by.")
print("1. Ensure game is in Borderless Window mode.")
print("2. Click inside the game menu.")
print("3. Press 'CTRL' to spawn Portbot.")

keyboard.wait('ctrl')
print("Spawning Portbot...")

time.sleep(1)

# Open console
pydirectinput.press('`')
time.sleep(0.5)

# Paste the map command perfectly
paste_to_console('ss_map mp_coop_lobby_3')

print("Waiting for the map to load...")
time.sleep(10) 

# Open console again
pydirectinput.press('`')
time.sleep(0.5)

# Paste the chat command perfectly
paste_to_console('cmd2 say "Portbot is online!"')

# Close console
pydirectinput.press('`')

print("Portbot has joined! Waking up the Brain...")

# NEW FIX: Find the exact folder this launcher is sitting in
current_folder = os.path.dirname(os.path.abspath(__file__))
brain_exact_path = os.path.join(current_folder, "brain.py")

# Run the brain using its exact address, wrapped in quotes for safety
subprocess.Popen(f'start cmd /k python "{brain_exact_path}"', shell=True)