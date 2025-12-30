import os
import psutil
import subprocess
from pynput import mouse

# Ignored processes
GAMES = ["GenshinImpact.exe", "javaw.exe", "TslGame.exe", "Minecraft.exe", "RobloxPlayerBeta.exe", "GTA5.exe", "gta_sa.exe", "GTAIV.exe", "Asphalt8.exe", "Asphalt9.exe", "Cemu.exe", "yuzu.exe", "Ryujinx.exe", "Dota2.exe", "csgo.exe", "cs2.exe"]


def is_game_running():
    # Checking
    for proc in psutil.process_iter(['name']):
        try:
            if proc.info['name'] in GAMES:
                return True
        except (psutil.NoSuchProcess, psutil.AccessDenied):
            continue
    return False

def restart_explorer():
   print("restarting explorer...")
    # restarting explorer.exe
   os.system("taskkill /F /IM explorer.exe")
    # reopening explorer via Popen
   subprocess.Popen("explorer.exe")

def on_click(x, y, button, pressed):
    # The logic of checking the mouse wheel click
    if button == mouse.Button.middle and pressed:
        if not is_game_running():
            restart_explorer()
        else:
            print("Игра запущена, перезапуск отменен. :)")

# Starting listening
print("Script running!")
with mouse.Listener(on_click=on_click) as listener:
    listener.join()
