import tkinter as tk
from datetime import datetime
import pytz

class TimeZoneClockApp:
    def __init__(self, root):
        self.root = root
        self.root.title("Clock for All Time Zones")

        # Create a canvas to hold the time zones
        self.canvas = tk.Canvas(self.root, width=600, height=800, scrollregion=(0, 0, 600, 1600))
        self.scrollbar = tk.Scrollbar(self.root, orient="vertical", command=self.canvas.yview)
        self.scrollbar.pack(side="right", fill="y")
        self.canvas.pack(side="left", fill="both", expand=True)
        self.canvas.configure(yscrollcommand=self.scrollbar.set)

        # Create a frame inside the canvas
        self.frame = tk.Frame(self.canvas)
        self.canvas.create_window((0, 0), window=self.frame, anchor="nw")

        # Get all time zones
        self.timezones = pytz.all_timezones
        self.labels = {}

        # Create labels for each time zone
        for i, timezone in enumerate(self.timezones):
            label = tk.Label(self.frame, text=f"{timezone}: ", font=("Helvetica", 14), anchor="w")
            label.grid(row=i, column=0, sticky="w", padx=10, pady=5)
            self.labels[timezone] = label

        self.update_clock()

    def update_clock(self):
        # Update the time for each time zone
        for timezone in self.timezones:
            now = datetime.now(pytz.timezone(timezone))
            formatted_time = now.strftime("%Y-%m-%d %H:%M:%S")
            self.labels[timezone].config(text=f"{timezone}: {formatted_time}")

        # Refresh every second
        self.root.after(1000, self.update_clock)

if __name__ == "__main__":
    root = tk.Tk()
    app = TimeZoneClockApp(root)
    root.mainloop()
    git clone https://github.com/Hussain78605/Time-Zone-Clock.git
cd Time-Zone-Clock
