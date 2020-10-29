import tkinter as tk


class Central(tk.Frame):

    def __init__(self, reference):
        super(Central, self).__init__()
        # Saving reference to gui
        self.reference = reference

        # Setting up widgets
        self.grid_columnconfigure(0, weight=1)
        w = reference.width
        h = reference.height
        self.devices = tk.StringVar(self)
        self.b1t = tk.StringVar(self)
        self.b1t.set("Connect")
        self.b2t = tk.StringVar(self)
        self.b2t.set("Upload")
        self.mode = tk.StringVar(self)
        self.mode.set("AOO")
        self.l8t = tk.StringVar(self)
        self.l8t.set("Atrium")

        # Pacemaker device menu
        self.f1 = tk.Frame(self, height=reference.height, width=250, bg="grey").place(x=0, y=0)
        self.l1 = tk.Label(self, text="Pacemaker Menu").place(x=75, y=10)
        self.l2 = tk.Label(self, text="Devices").place(x=15, y=44)
        self.o1 = tk.OptionMenu(self, self.devices, "one", "two", "three").place(anchor=tk.NE, x=235, y=40)
        self.b1 = tk.Button(self, textvariable=self.b1t, command=self.device_button, state=tk.DISABLED, width=30)
        self.b1.place(x=15, y=80)
        self.devices.trace('w', self.device_select)
        self.l3 = tk.Label(self, text="Connection Status").place(x=15, y=120)
        self.l4 = tk.Label(self, text="Active").place(anchor=tk.NE, x=235, y=120)
        self.l5 = tk.Label(self, text="Signal Strength").place(x=15, y=150)
        self.l6 = tk.Label(self, text="Strong").place(anchor=tk.NE, x=235, y=150)
        self.b2 = tk.Button(self, textvariable=self.b2t, command=self.device_button, state=tk.DISABLED, width=30)
        self.b2.place(x=15, y=180)

        # Pacemaker parameters
        self.t1 = tk.Label(self, text="Pacemaker Parameter").place(x=w/2+60, y=0)
        self.o2 = tk.OptionMenu(self, self.mode, "AOO", "VOO", "AAI", "VVI").place(x=265, y=40)
        self.l7 = tk.Label(self, text="Affected Chamber: ").place(x=355, y=46)
        self.l8 = tk.Label(self, textvariable=self.l8t).place(x=460, y=46)
        self.mode.trace('w', self.mode_select)

        rx = 265
        ry = 76
        rinc = 170
        self.s1v = tk.DoubleVar()
        self.s1 = tk.Scale(self, orient=tk.HORIZONTAL, variable=self.s1v, length=150, from_=1, to=10, resolution=0.1, state=tk.DISABLED)
        self.s1.place(x=rx, y=ry)
        self.s1v.set(4.0)
        self.s1t = tk.Label(self, text="Pulse Width (ms)").place(x=rx+20, y=ry+40)
        rx += rinc

        self.s2v = tk.DoubleVar()
        self.s2 = tk.Scale(self, orient=tk.HORIZONTAL, variable=self.s2v, length=150, from_=500, to=7500, resolution=150, state=tk.DISABLED)
        self.s2.place(x=rx, y=ry)
        self.s2v.set(3750)
        self.s2t = tk.Label(self, text="Pulse Amplitude (mV)").place(x=rx+20, y=ry+40)
        rx += rinc
        self.s3v = tk.DoubleVar()
        self.s3 = tk.Scale(self, orient=tk.HORIZONTAL, variable=self.s3v, length=150, from_=20, to=120, resolution=1, state=tk.DISABLED)
        self.s3.place(x=rx, y=ry)
        self.s3v.set(60)
        self.s3t = tk.Label(self, text="Lower Limit (ppm)").place(x=rx+20, y=ry+40)

        self.s5v = tk.DoubleVar()
        self.s5 = tk.Scale(self, orient=tk.HORIZONTAL, variable=self.s5v, length=150, from_=80, to=180, resolution=1, state=tk.DISABLED)
        self.s5.place(x=rx, y=ry+70)
        self.s5v.set(120)
        self.s5t = tk.Label(self, text="Upper Limit (ppm)").place(x=rx+20, y=ry+110)
        rx += rinc
        self.s4v = tk.DoubleVar()
        self.s4 = tk.Scale(self, orient=tk.HORIZONTAL, variable=self.s4v, length=150, from_=100, to=500, resolution=5,state=tk.DISABLED)
        self.s4.place(x=rx, y=ry)
        self.s4v.set(250)
        self.s4t = tk.Label(self, text="Rate Delay (ms)").place(x=rx+20, y=ry+40)

        self.pack(expand=1, fill=tk.BOTH)

    def device_button(self):
        print("connect")

    def device_select(self, *args):
        self.b1.config(state="normal")

    def mode_select(self, *args):
        mode = self.mode.get()
        if mode == "AOO":
            self.l8t.set("Atrium")
            self.s4v.set(250)
            self.s2v.set(3750)
            self.s2.config(state="disabled")
        elif mode == "AAI":
            self.l8t.set("Atrium")
            self.s4v.set(250)
            self.s2v.set(3500)
            self.s2.config(state="normal")
        elif mode == "VOO":
            self.l8t.set("Ventricle")
            self.s4v.set(320)
            self.s2v.set(3750)
            self.s2.config(state="disabled")
        elif mode == "VVI":
            self.l8t.set("Ventricle")
            self.s4v.set(320)
            self.s2v.set(3500)
            self.s2.config(state="normal")


