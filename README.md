# Portbot: AI-Powered Portal 2 Co-op Partner 🤖🍰

Portbot is a Python bot that plays Portal 2's co-op mode with you. Instead of using preset paths, Portbot uses the **Google Gemini 2.0 Flash Vision API** to actually look at your game screen, figure out the puzzle room, and decide what to do next.

Created by ErrorGamer.

## ✨ Features
* **True AI Vision:** Takes pictures of your game and uses Gemini 2.0 Flash to understand the room.
* **Invisible Controls:** Sends commands directly to the game's engine. It will not mess up your keyboard or pop open the developer console.
* **Auto-Launcher:** A script that automatically finds the game, sets up the lobby, and spawns the bot.
* **Invincible Loop:** Built-in safety nets that stop the bot from crashing if the screen glitches or the AI gets too busy.

## 🛠️ What You Need
* **OS:** Windows 11
* **Game:** Portal 2 (Installed via Steam)
* **Python:** Version 3.8 or higher
* **API Key:** A free Google Gemini API Key (get one at [Google AI Studio](https://aistudio.google.com/))

## 📦 How to Install

1. Download this code to your computer. Open your Command Prompt and run:
   ```
   git clone https://github.com/op-pow/Portbot-for-Portal-2.git
   ```

2. Install the required Python tools by running:
   ```
   pip install psutil keyboard pyperclip pydirectinput mss pillow google-genai
   ```

3. Open `brain.py` in a text editor like Notepad. You must get your own free API key from Google and paste it into the `API_KEY` variable at the top of the file!

## ⚙️ Game Setup (CRITICAL)
Portbot will not work unless you change two specific settings in Portal 2 and Steam.

### Open the Engine Backdoor:

1. Open Steam → Right-click Portal 2 → Properties.
2. In the General tab, find **Launch Options** at the bottom.
3. Type exactly this: `-netconport 2121`

This allows the Python script to send invisible commands directly to the game.

### Set Borderless Windowed Mode:

1. Launch Portal 2 → Options → Video.
2. Change Display Mode to **Windowed (No Border)** or **Borderless**.

True fullscreen will block Python from taking screenshots.

## 🚀 How to Run

1. Launch Portal 2 and stay on the Main Menu.
2. Open a Command Prompt as Administrator (required for the launcher's initial setup keys).
3. Go to your Portbot folder and run the launcher:
   ```
   python launcher.py
   ```
4. Click your mouse inside the Portal 2 window so the game is selected.
5. Press **CTRL** on your keyboard.
6. Do not touch your keyboard or mouse. The launcher will automatically load the map and spawn the bot.
7. Once spawned, wait exactly 15 seconds. You will see a second black window open—this is Portbot's Brain booting up.
8. Portbot will announce in the game chat when it is online and will begin analyzing the room!

## 🐛 Troubleshooting

**The bot only types half its commands into the console initially:**
- Make sure you clicked inside the Portal 2 window before pressing CTRL.

**The Brain window crashes immediately with a 404 or 429 error:**
- **404:** Make sure your `google-genai` tool is up to date.
- **429:** You hit the free Gemini API speed limit. The bot has a built-in 15-second delay to prevent this, but if you get locked out, wait 3 minutes and try again.

**The script says "Connection failed":**
- You forgot to add `-netconport 2121` to your Steam Launch Options, or another app is blocking it.
