from tkinter import *
import time
import math
import os

class CalendarApp:
    def __init__(self, master):
        self.master = master #master
        self.init_data()
        self.init_ui()

    def init_data(self):
        self.curtime = time.strftime("%H:%M:%S")
        self.tdydate = time.strftime("%B %d %Y")
        self.curday = time.strftime("%d")
        self.curmonth = time.strftime("%B")
        self.curday = int(time.strftime("%d"))
        self.curyear = int(time.strftime("%Y"))
        self.epoch = time.ctime(0)

        self.year = self.curyear
        self.month = self.curmonth
        self.year_days = 365
        self.leapyear_days = 366

        self.months = [["January", 31],
                        ["February", 28],
                  ["March", 31],
                  ["April", 30],
                  ["May", 31],
                  ["June", 30],
                  ["July", 31],
                  ["August", 31],
                  ["September", 30],
                  ["October", 31],
                  ["November", 30],
                  ["December", 31]]

        self.week = ("Sunday", "Monday", "Tuesday", "Wednesday", "Thursday", "Friday", "Saturday")

    def init_ui(self):
        self.master.geometry("1920x1080")
        self.master.title("CalendarApp")

        self.frame3 = Frame(self.master)
        self.frame3.pack(fill=X)
        self.frame3.columnconfigure(0, weight=1)
        self.frame3.columnconfigure(1, weight=2)
        self.frame3.columnconfigure(2, weight=1)

        self.prev_month = Button(self.frame3, text="Previous", command=self.prev, height=3)
        self.prev_month.grid(row=0, column=0, sticky="ew")

        self.monthyear_label = StringVar()
        self.monthyear_text = str()

        self.nav_month = Label(self.frame3, textvariable=self.monthyear_label, height=3)
        self.nav_month.grid(row=0, column=1, sticky="ew")

        self.next_month = Button(self.frame3, text="Next", command=self.next, height=3)
        self.next_month.grid(row=0, column=2, sticky="ew")

        self.monthyear_text = str(self.month) + " " + str(self.year)
        self.monthyear_label.set(self.monthyear_text)

        self.frame2 = Frame(self.master)
        self.frame2.pack(fill=X)

        for day in self.week:
            self.day_label = Label(self.frame2, text=day, height=3)
            self.day_label.grid(row=0, column=self.week.index(day), sticky="ew")
            self.frame2.columnconfigure(self.week.index(day), weight=1)

        self.frame1 = Frame(self.master)
        self.frame1.pack(fill=BOTH, expand=True)

        self.button_gen()

    def month_length(self):
        for m in self.months:
                if m[0] == self.month:
                        return self.months[self.months.index(m)][1]

    def isleap(self, year):  # checks if the year is a leap year
            if year % 4 == 0 and (year % 100 != 0 or year % 400 == 0):
                return True
            return False

    def leapcount(self, year):  # counts the number of leap years from 1st jan 1AD according to gregorian calendar
        count = 0
        # julianleap=int(curyear)/4
        for y in range(1, year + 1):
            if self.isleap(y) == True:
                count += 1
        return count

    def leapchange(self):
        if self.isleap(self.year) == True:
            for m in self.months:
                if m[0] == "February":
                    m[1] = 29
                else:
                    pass
        else:
            for m in self.months:
                if m[0] == "February":
                    m[1] = 28
                else:
                    pass

    def pmdcount(self):  # counts days from the first day of the *year* to the end of the previous month
        count = 0
        for m in self.months:
            if m[0] == self.month:
                break
            else:
                count += m[1]
        return count

    def open_event_editor(self, date):
        pass
    # Open a new window for event editing
    # ...

    def save_event(self, date, event_details):
        pass
    # Save the event details to a file
    # ...

    def load_events(self):
        pass
    # Load events from files and update the calendar UI
    # ...

    def highlight_dates_with_events(self):
        pass
    # Highlight dates with events on the calendar UI
    # ...


    def prev(self):  # changes the label textvariable then sets it then page update.
        # global self.year, self.month, self.monthyear_text, self.monthyear_label
        for m in self.months:
            if m[0] == self.month:
                if self.months.index(m) == 0:
                    self.year -= 1
                    self.month = self.months[11][0]
                    self.monthyear_text = str(self.month) + " " + str(self.year)
                    self.monthyear_label.set(self.monthyear_text)
                else:
                    self.month = self.months[self.months.index(m) - 1][0]
                    self.monthyear_text = str(self.month) + " " + str(self.year)
                    self.monthyear_label.set(self.monthyear_text)
                break

        self.button_gen()

    def next(self):
        # global self.month, self.year
        for m in self.months:
            if m[0] == self.month:
                if self.months.index(m) == 11:
                    self.year += 1
                    self.month = self.months[0][0]
                    self.monthyear_text = str(self.month) + " " + str(self.year)
                    self.monthyear_label.set(self.monthyear_text)
                else:
                    self.month = self.months[self.months.index(m) + 1][0]
                    self.monthyear_text = str(self.month) + " " + str(self.year)
                    self.monthyear_label.set(self.monthyear_text)
                break

        self.button_gen()

    def button_gen(self):
        print(self.month)
        print(self.year)
        self.leapchange()
        self.epoch_prevmonth = ((self.year_days * (self.year - 1 - self.leapcount(self.year - 1))) + (
                    self.leapyear_days * self.leapcount(self.year - 1))) + self.pmdcount()
        print(self.leapcount(self.year - 1))
        print(self.pmdcount())
        print(self.epoch_prevmonth)
        self.prevmonth_end = (self.epoch_prevmonth - (math.floor(self.epoch_prevmonth / 7) * 7))
        print(self.prevmonth_end)
        print(self.isleap(self.year))
        print(self.months[1][1])
        print(self.month_length())

        for widget in self.frame1.winfo_children():
            widget.destroy()
        for row in range(6):
            for day in self.week:  # basically for col in range(7)
                count = row * 7 + self.week.index(day) - self.prevmonth_end  # prevmonth_end needs to be updated
                if row == 0 and self.week.index(day) <= self.prevmonth_end:
                    ghost_label = Label(self.frame1, text="")
                    ghost_label.grid(row=row, column=self.week.index(day), sticky="nsew")
                    self.frame1.columnconfigure(self.week.index(day), weight=1)
                    self.frame1.rowconfigure(row, weight=1)

                elif row * 7 + self.week.index(day) - self.prevmonth_end <= self.month_length():
                    day_button = Button(self.frame1, text=count)
                    day_button.grid(row=row, column=self.week.index(day), sticky="nsew")
                    self.frame1.columnconfigure(self.week.index(day), weight=1)
                    self.frame1.rowconfigure(row, weight=1)
                else:
                    ghost_label = Label(self.frame1, text="")
                    ghost_label.grid(row=row, column=self.week.index(day), sticky="nsew")
                    self.frame1.columnconfigure(self.week.index(day), weight=1)
                    self.frame1.rowconfigure(row, weight=1)





if __name__ == "__main__":
    win = Tk()
    run = CalendarApp(win)
    win.mainloop()
