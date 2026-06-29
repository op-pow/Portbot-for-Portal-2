import time
import socket
import mss
import mss.tools
from google import genai
from PIL import Image

# 1. Setting up the Gemini Brain
API_KEY = "AQ.Ab8RN6LsMfFifppGIwwTyWeRwBIyWeXYBJoH722zZuvgCVmFZQ"
client = genai.Client(api_key=API_KEY)

def send_command(command_text):
    try:
        wire = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        wire.connect(('127.0.0.1', 2121))
        wire.sendall((command_text + '\n').encode('utf-8'))
        wire.close()
    except Exception as e:
        pass

def take_screen_picture():
    with mss.MSS() as sct:
        monitor = sct.monitors[1] 
        sct_img = sct.grab(monitor)
        img = Image.frombytes("RGB", sct_img.size, sct_img.bgra, "raw", "BGRX")
        return img

def ask_gemini(image_of_game):
    prompt = "You are playing Portal 2 co-op. Look at this screen. Reply with ONLY ONE WORD from this list: 'walk', 'jump', 'shoot_blue', 'shoot_orange', or 'wait'."
    try:
        response = client.models.generate_content(
            model='gemini-2.0-flash', 
            contents=[prompt, image_of_game]
        )
        return response.text.strip().lower() 
    except Exception as e:
        print("Brain crash error:", e) 
        return "wait"

print("Portbot AI Brain has launched!")
print("Starting 15-second countdown...")
time.sleep(15)

print("AI Activated! Portbot is now looking at the screen and thinking for itself...")

# The Invincible [Forever] Loop
while True: 
    try:
        # Take a picture of the room
        current_view = take_screen_picture()
        
        # Ask Gemini for the next move
        ai_choice = ask_gemini(current_view)
        
        # Tell you what it decided in the game chat
        send_command('cmd2 say "I see the room. Deciding to: ' + ai_choice + '"')
        time.sleep(0.5) 
        
        # The [If / Then] Logic
        if "walk" in ai_choice:
            send_command('cmd2 +forward') 
            time.sleep(1)
            send_command('cmd2 -forward') 
            
        elif "jump" in ai_choice:
            send_command('cmd2 +jump')
            time.sleep(0.5)
            send_command('cmd2 -jump')
            
        elif "shoot_blue" in ai_choice:
            send_command('cmd2 +attack')
            
        elif "shoot_orange" in ai_choice:
            send_command('cmd2 +attack2') 
            
        # THE FIX: Increased wait time to 15 seconds to respect the API speed limit
        time.sleep(15)

    except Exception as fatal_error:
        print("CRITICAL ERROR CAUGHT:", fatal_error)
        print("Portbot stumbled! Rebooting thought process in 2 seconds...")
        time.sleep(2)