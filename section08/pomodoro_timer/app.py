from tkinter import ttk
import tkinter as tk
from components.components import Home, Settings, Timer
from collections import deque

COLOUR_PRIMARY = "#2e3f4f"
COLOUR_SECONDARY = "#293846"
COLOUR_LIGHT_TEXT = "#EEEEEE"
COLOUR_DARK_TEXT = "#8095a8"


class PomodoroTimer(tk.Tk):
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)

        style = ttk.Style()
        style.configure("Timer.TFrame", background="#FFF")
        style.configure("Background.TFrame", background=COLOUR_PRIMARY)
        style.configure(
            "TimerText.TLabel",
            background="#ffffff",
            foreground=COLOUR_DARK_TEXT,
            font="Courier 38"
        )
        style.configure(
            "LightText.TLabel",
            background=COLOUR_PRIMARY,
            foreground=COLOUR_LIGHT_TEXT,
        )
        style.configure(
            "PomodoroButton.TButton",
            background=COLOUR_SECONDARY,
            foreground=COLOUR_LIGHT_TEXT,
        )
        
        # Main app window is a tk widget, so background is set directly
        self["background"] = COLOUR_PRIMARY

        self.title("Pomodoro Timer")
        self.columnconfigure(0, weight=1)
        self.rowconfigure(1, weight=1)

        container = ttk.Frame(self)
        container.grid()
        container.columnconfigure(0, weight=1)

        self.pomodoro = tk.StringVar(value=25)
        self.long_break = tk.StringVar(value=15)
        self.short_break = tk.StringVar(value=5)
        self.timer_order = ["Pomodoro", "Short Break", "Pomodoro", "Short Break", "Pomodoro", "Long Break"]
        self.timer_schedule = deque(self.timer_order)
        
        self.current_time = tk.StringVar(value=f"{self.pomodoro.get()}:00")
        self.timer_running = False

        self.frames = {}

        for F in (Home, Settings, Timer):
            frame = F(container, self)
            self.frames[F] = frame
            frame.grid(row=0, column=0, sticky="NESW")

        self.show_frame(Home)

    def show_frame(self, container):
        frame = self.frames[container]
        frame.tkraise()


root = PomodoroTimer()
root.mainloop()


"""
activebackground − Background color for the widget when the widget is active.

activeforeground − Foreground color for the widget when the widget is active.

background − Background color for the widget. This can also be represented as bg.

disabledforeground − Foreground color for the widget when the widget is disabled.

foreground − Foreground color for the widget. This can also be represented as fg.

highlightbackground − Background color of the highlight region when the widget has focus.

highlightcolor − Foreground color of the highlight region when the widget has focus.

selectbackground − Background color for the selected items of the widget.

selectforeground − Foreground color for the selected items of the widget.
"""
