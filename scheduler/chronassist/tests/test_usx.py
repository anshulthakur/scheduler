from django.test import TestCase
import unittest
from selenium import webdriver

# Create your tests here.

class FunctionalTest(TestCase):
    
    def setUp(self):
        self.browser = webdriver.Chrome()
        self.browser.implicitly_wait(3) #seconds
    
    def tearDown(self):
        self.browser.quit()
        
        
    def test_USX(self):
#1. User visits page
#2. User sees form to make quick to-do list
#3. User enters to-do element and presses enter/submit
#4. Page reloads with his entry as to-do list item and form empty
#5. He enters another one and presses submit
#6. He sees this entry after the first entry
#7. He wants the second to be the first, so he drags second above first and drops
#8. He reloads page and the ordering is maintained.
#9. He notices a create job button next to the form
#10. He clicks on it and sees that the form folds out to a bigger form
#11. In this form, he can enter title, start date, start time, period, recurring/one time options and a check box of cancel on override (which means that if it is preempted, will it be postponed, or will it be canceled).
#He notices that if he doesn't enter date, today's date is taken
#12. If he doesn't enter time, 1 hour is taken and placed in the first empty slot.
#13. He needs to find an option for work hours to set the schedule duration (morning 9 to night 12)
#He notices that his job sheet has another view - view Day, in which the allocated chunks of jobs are shown in a table with empty spaces in between.
#14. He now tries to make an entry with timing which clashes with some other job.
#15. The UI prompts him about a clash with another job. It gives the option to: 
#a) Reschedule current job 
# b) Reschedule/Cancel other job (Only cancel option is displayed for jobs which cannot be rescheduled, 
# i.e. were marked as non-reschedulable. Hard Limit Jobs.)
        pass

if __name__== '__main__':
    unittest.main()    
