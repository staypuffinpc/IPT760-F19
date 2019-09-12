### PURPOSE: To create an class object that can be used for assignments ###
from datetime import date
from dateutil.relativedelta import relativedelta

class Assignment:

    def __init__(self):
        self.title = ''
        self.due = date.today() + relativedelta(months = +2) #choose a date 2 months from when you create this.  You'll likely have to change it
        self.description = ''
        self.value = 50

    def grade(self,earned=0):
        self.grade = earned/self.value
