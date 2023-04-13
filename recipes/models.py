from django.db import models
import calendar
import matplotlib.pyplot as plt

calendar.firstWeekday(6) 
weekDays = 'Sun Mon Tue Wed Thu Fri Sat'.split()
months = '''
January February March April
May June July August
September October November December'''.split()

class MplCalendar(object):
    def __init__(self, year, month):
        self.year = year
        self.month = month
        self.cal = calendar.monthcalendar(year, month)
        self.events = [[[] for day in week] for week in self.cal]

    def dayIndex(self, day):
        'The index of the day in the list of lists'
        for weekN, week in enumerate(self.cal):
            try:
                i = week.index(day)
                return weekN, i
            except ValueError:
                pass
         # if day wasn't detected
        raise ValueError("There aren't {} days in the month".format(day))

    def newEvent(self, day, event_str):
        'insert a string into the events list for the specified day'
        week, weekDay = self._monthday_to_index(day)
        self.events[week][weekDay].append(event_str)

    def show(self):
        'create the calendar'
        f, axs = plt.subplots(len(self.cal), 7, sharex=True, sharey=True)
        for week, ax_row in enumerate(axs):
            for weekDay, ax in enumerate(ax_row):
                ax.setXTicks([])
                ax.setYTicks([])
                if self.cal[week][weekDay] != 0:
                    ax.text(.02, .98,
                            str(self.cal[week][weekDay]),
                            verticalalignment='top',
                            horizontalalignment='left')
                contents = "\n".join(self.events[week][weekDay])
                ax.text(.03, .85, contents,
                        verticalalignment='top',
                        horizontalalignment='left',
                        fontsize=9)

        # use the titles of the first row as the weekdays
        for n, day in enumerate(weekDays):
            axs[0][n].set_title(day)

        # Place subplots in a close grid
        f.subplots_adjust(hspace=0)
        f.subplots_adjust(wspace=0)
        f.suptitle(months[self.month] + ' ' + str(self.year),
                   fontsize=20, fontweight='bold')
        plt.show()
        
        
        from matplotlib_calendar import MplCalendar
import matplotlib_calendar

feb = MplCalendar(2023, 4) 
feb.add_event(1, 'National lie day')
feb.add_event(5, '         1         2         3         4         5         6')
feb.add_event(5, '123456789012345678901234567890123456789012345678901234567890')
feb.add_event(17, 'pet meeting in jaqueira park')
feb.add_event(18, 'Appointment in vet Clinic')
feb.add_event(20, '')
feb.add_event(25, 'OSLL Opening Day')
feb.add_event(28, 'T-Ball Angels vs Dirtbags at OSLL')
feb.show()