from selenium import webdriver
import unittest

class NewVisitorTest(unittest.TestCase):

    def setUp(self):
        self.browser = webdriver.Firefox()
        self.browser.implicitly_wait(3)

    def tearDown(self):
        self.browser.quit()

    def test_can_start_a_list_and_retrieve_it_later(self):
        # Billy Bob has heard about a new online to-do app that is all over HN and Reddit.
        # He goes to check it out.
        self.browser.get('http://localhost:8000')

        # He notices the page title and header mention to-do lists.
        self.assertIn( 'To-Do',  self.browser.title)
        self.fail('Finish the test!')

        # He is asked to enter a to-do on load.

        # He types in "Buy peacock feathers" into the text box.

        # Submitting updates the page and it now lists the entered to-do item.

        # There is another input Billy Bob can enter another to-do immediately.
        # He enters "Use peacock feathers to make a fly.

        # Submitting updates the page and shows both items.

        # Billy Bob notices the page has a unique URL and he realizes he can
        # visit the site later to see the items he has entered.

        # Ole Billy Bob returns to the unique URL and sees his expected list of to-dos.

if __name__ == '__main__':
    unittest.main(warnings='ignore')
