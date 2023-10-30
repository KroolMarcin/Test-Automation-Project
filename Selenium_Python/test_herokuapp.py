import time
import unittest

from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC


class TestHerokuApp(unittest.TestCase):
    def setUp(self):
        #Method that runs in the beggining of each test
        self.driver = webdriver.Chrome()
        self.driver.maximize_window()
 
    def tearDown(self):
        #Method that runs in the end of each test
        self.driver.close()

    def test_add_remove_page(self):
        #Test which adds and removes delete button
        self.driver.get("https://the-internet.herokuapp.com/")
        addRemoveElement = WebDriverWait(self.driver, 10).until(EC.presence_of_element_located((By.XPATH, "//ul//li//a[text()='Add/Remove Elements']")))
        addRemovePage = self.driver.find_element(By.XPATH, "//ul//li//a[text()='Add/Remove Elements']")
        addRemovePage.click()
        addButton = self.driver.find_element(By.XPATH, "//button[text()='Add Element']")
        addButton.click()
        addButton.click()

        # Check that two buttons are visible
        deleteButton = self.driver.find_elements(By.XPATH, "//button[text()='Delete']")
        self.assertEqual(len(deleteButton), 2)

        # Check that one button is visible
        deleteButton[0].click()
        deleteButton = self.driver.find_elements(By.XPATH, "//button[text()='Delete']")
        self.assertEqual(len(deleteButton),1)

    def test_checkbox(self):
        #Test which gives information about status of checkbox
        self.driver.get("https://the-internet.herokuapp.com/checkboxes")
        checkbox = self.driver.find_elements(By.XPATH, '//input[@type="checkbox"]')
        # Checking if first checkbox is already selected
        self.assertFalse(checkbox[0].is_selected())

        # Select first checkbox if it is not selected
        if not checkbox[0].is_selected():
            checkbox[0].click()
        
        # Checking if second checkbox is already selected
        self.assertTrue(checkbox[1].is_selected())

        # Unselect second checkbox if it is selected
        if checkbox[1].is_selected():
            checkbox[1].click()

        self.assertTrue(checkbox[0].is_selected())
        self.assertFalse(checkbox[1].is_selected())
    
    def test_dropdown(self):
        #Test which asserts chosen element of dropdown
        self.driver.get('https://the-internet.herokuapp.com/dropdown')
        dropdown = self.driver.find_element(By.XPATH, "//select[@id='dropdown']")
        dropdown.click()
        dropdownElements = self.driver.find_elements(By.XPATH, '//select[@id="dropdown"]//option')
        dropdownElements[2].click()

        self.assertTrue(dropdownElements[2].is_selected())
    
    def test_drag_and_drop(self):
        #Test which drags one element and drops on another element
        from selenium.webdriver import ActionChains
        self.driver.get("https://the-internet.herokuapp.com/drag_and_drop")
        columnA = self.driver.find_element(By.XPATH, "//div[@id='column-a']")
        columnB = self.driver.find_element(By.XPATH, "//div[@id='column-b']")

        #Making element move with the use of ActionChains
        actionChains = ActionChains(self.driver)
        actionChains.drag_and_drop(source=columnA, target=columnB).perform()

        #Making sure that elements place was changed
        self.assertEqual(columnA.text, 'B')
        self.assertEqual(columnB.text, 'A')