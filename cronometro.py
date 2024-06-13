import tkinter as tk

class Stopwatch:
    def __init__(self, master):
        self.master = master
        self.master.title("Cronômetro")

        self.running = False
        self.hours = 0
        self.minutes = 0
        self.seconds = 0

        self.time_label = tk.Label(master, text=self.format_time(), font=("Helvetica", 48))
        self.time_label.pack()

        self.start_button = tk.Button(master, text="Iniciar", command=self.start)
        self.start_button.pack(side=tk.LEFT)

        self.stop_button = tk.Button(master, text="Parar", command=self.stop)
        self.stop_button.pack(side=tk.LEFT)

        self.reset_button = tk.Button(master, text="Resetar", command=self.reset)
        self.reset_button.pack(side=tk.LEFT)

        self.update_time()

    def format_time(self):
        return f"{self.hours:02}:{self.minutes:02}:{self.seconds:02}"

    def update_time(self):
        if self.running:
            self.seconds += 1
            if self.seconds >= 60:
                self.seconds = 0
                self.minutes += 1
            if self.minutes >= 60:
                self.minutes = 0
                self.hours += 1

            self.time_label.config(text=self.format_time())
        self.master.after(1000, self.update_time)

    def start(self):
        if not self.running:
            self.running = True

    def stop(self):
        if self.running:
            self.running = False

    def reset(self):
        if not self.running:
            self.hours = 0
            self.minutes = 0
            self.seconds = 0
            self.time_label.config(text=self.format_time())

if __name__ == "__main__":
    root = tk.Tk()
    stopwatch = Stopwatch(root)
    root.mainloop()
