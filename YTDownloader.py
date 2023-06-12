# YouTube to MP3 Downloader

# Packages
from pytube import YouTube
import os
import customtkinter as ctk

# Variables
# Get URL from user / This was used pre-ctk
# link = YouTube("https://www.youtube.com/watch?v=u39QcvgF4FQ")
# link = YouTube(input("Enter YouTube URL: \n>>"))

# Set Save Destination
def save_location():
    print(os.getcwd())
    destination = str(ctk.filedialog.askdirectory())
    print(destination)


# DEBUG SAVE LOCATIONS
destination = "E:\Switch Mods\SmashUlt Mods\DownloadedMusic"


# ========== Functions ==========
# Download YouTube audio as MP3
def download_audio():
    link = YouTube(entry.get())
    # Get Audio ONLY
    video_audio = link.streams.filter(only_audio=True).first()

    # Download video/audio
    out_file = video_audio.download(output_path=os.getcwd())

    # Save File
    base, ext = os.path.splitext(out_file)
    new_file = base + '.mp3'
    os.rename(out_file, new_file)    
    
    # Download Success Message
    # print(link.title +" Downloaded Successfully!")

    # Clear entry URL
    entry.delete(0, ctk.END)
    open_popup()

# Success Pop-Up
def open_popup():
    top = ctk.CTkToplevel()
    top.geometry("340x129")
    top.title("Download Complete")
    top.attributes('-topmost', 'true')
    messagebox = ctk.CTkLabel(top, text="Success! :D", font=ctk.CTkFont(size=30, weight="bold"))
    messagebox.pack(pady=50)


# tkinter GUI
root = ctk.CTk()
root.geometry("750x350")
root.title("YouTube to MP3")

# Title
title_label = ctk.CTkLabel(root, text="YouTube to MP3", font=ctk.CTkFont(size=40, weight="bold"))
title_label.pack(padx=12, pady=(30, 20))

# User YouTube URL Input
entry = ctk.CTkEntry(root, placeholder_text="Enter YouTube URL >>")
entry.pack(fill="x", padx=18)

# Download Button
add_button = ctk.CTkButton(root, text="Download", width=500, command=download_audio)
add_button.pack(pady=20)

# Save Destination Text
savedest_label = ctk.CTkLabel(root, text=os.getcwd(), font=ctk.CTkFont(size=15))
savedest_label.pack(padx=12, pady=(9, 5))

# Save Destination Button
savedest_button = ctk.CTkButton(root, text="Choose Save Destination (WIP: Not working atm )", width=300, command=save_location)
savedest_button.pack(padx=10, pady=10)

root.mainloop()