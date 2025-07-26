import tkinter as tk
from tkinter import messagebox
import pygame

# Initialize pygame for sound
pygame.init()
pygame.mixer.init()

# Function to play buzzer sound
def play_buzzer():
    try:
        pygame.mixer.music.load("oxygen_alert.wav.wav")  # Make sure this file is in the same folder
        pygame.mixer.music.play()
    except:
        messagebox.showerror("Error", "oxygen_alert.wav.wav not found!")

# Main window
root = tk.Tk()
root.title("Smart Oxygen Supply System")
root.geometry("500x400")
root.configure(bg="#E8F6F3")

# Sensor status variables
occupant_detected = tk.BooleanVar()
air_quality_poor = tk.BooleanVar()

# Emergency check function
def check_emergency():
    if occupant_detected.get() and air_quality_poor.get():
        status_label.config(text="🚨 Emergency Detected!\nOxygen & Ventilation Activated", fg="red")
        play_buzzer()
    elif occupant_detected.get():
        status_label.config(text="Occupant Detected\nAir Quality Normal", fg="blue")
    elif air_quality_poor.get():
        status_label.config(text="Poor Air Quality\nNo Occupant", fg="orange")
    else:
        status_label.config(text="System Normal", fg="green")

# GUI elements
tk.Label(root, text="Smart Oxygen Supply System", font=("Arial", 16, "bold"), bg="#E8F6F3").pack(pady=10)

tk.Checkbutton(root, text="Occupant Detected", variable=occupant_detected,
               bg="#E8F6F3", font=("Arial", 12)).pack(pady=10)

tk.Checkbutton(root, text="Poor Air Quality", variable=air_quality_poor,
               bg="#E8F6F3", font=("Arial", 12)).pack(pady=10)

tk.Button(root, text="Run System Check", command=check_emergency,
          bg="#2ECC71", fg="white", font=("Arial", 12), width=20).pack(pady=20)

status_label = tk.Label(root, text="System Idle", font=("Arial", 14), bg="#E8F6F3")
status_label.pack(pady=20)

# Run the GUI
root.mainloop()
