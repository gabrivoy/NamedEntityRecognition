# e2e = end-to-end
import unittest
from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from webdriver_manager.chrome import ChromeDriverManager

class E2ETest(unittest.TestCase):

    def setUp(self):
        self.driver = webdriver.Chrome(service=Service(ChromeDriverManager().install()))
        self.driver.get('http://localhost:5000/')

    def tearDown(self):
        self.driver.quit()

    def test_browser_title_contains_app_name(self):
        self.assertIn('Named Entity', self.driver.title)

    def test_page_heading_is_named_entity_finder(self):
        heading = self._find("heading").text
        self.assertEqual(heading, "Named Entity Finder")

    def test_page_has_input_for_text(self):
        input_element = self._find('input-text')
        self.assertIsNotNone(input_element)

    def test_page_hast_button_for_submitting_test(self):
        submit_button = self._find('find-button')
        self.assertIsNotNone(submit_button)

    def test_page_has_ner_table(self):
        input_element = self._find('input-text')
        submit_button = self._find('find-button')
        input_element.send_keys('France and Germany share a border in Europe')
        submit_button.click()
        table = self._find('ner-table')
        self.assertIsNotNone(table)

    def _find(self, val):
        return self.driver.find_element("css selector", f'[data-test-id="{val}"]')