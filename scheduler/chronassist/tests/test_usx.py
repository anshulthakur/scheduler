from django.test import TestCase
import unittest
from selenium import webdriver
from selenium.webdriver.common.keys import Keys

# Create your tests here.

class FunctionalTest(TestCase):
    
    def setUp(self):
        self.browser = webdriver.Chrome()
        self.browser.implicitly_wait(3) #seconds
    
    def tearDown(self):
        self.browser.quit()
        
    def create_item_in_list(self, item_text=None):
        form_input = self.browser.find_element_by_id('id_new_item')
        self.assertEqual(  
                form_input.get_attribute('placeholder'),
                'Enter a To-Do Item'
                )
        
        #3. User enters to-do element and presses enter/submit
        form_input.send_keys(item_text)
        
        #4. Page reloads with his entry as to-do list item and form empty
        form_input.send_keys(Keys.ENTER)

        
    def test_USX(self):
        #1. User visits page
        self.browser.get("http://localhost:8000")
        #2. User sees form to make quick to-do list titled 'Your To-Do List'
        self.assertIn('To-Do', self.browser.title)
        form_title = self.browser.find_element_by_tag_name('h1').text
        self.assertIn('Your To-Do List', form_title)
        
        #Create an entry in table
        self.create_item_in_list('Make a scheduler project test case')
                
        #He notes that the entry has been created.
        table = self.browser.find_element_by_id('id_list_table')
        rows = table.find_elements_by_tag_name('tr')
        self.assertIn('Make a scheduler project test case', [row.text for row in rows])
        
        #5. He enters another one and presses submit
        self.create_item_in_list('Make a scheduler project model too')
        #6. He sees this entry after the first entry
        table = self.browser.find_element_by_id('id_list_table')
        rows = table.find_elements_by_tag_name('tr')
        self.assertIn('Make a scheduler project test case', [row.text for row in rows])
        self.assertIn('Make a scheduler project model too', [row.text for row in rows])
        self.fail('Finish the test!')
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
