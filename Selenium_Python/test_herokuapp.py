import allure
import datetime
import unittest

from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

def take_screenshot_and_attach(driver):
    timestamp = datetime.datetime.now().strftime("%Y-%m-%d_%H-%M-%S")
    filename = f"screenshot_{timestamp}.png"
    allure.attach(driver.get_screenshot_as_png(), name=filename, attachment_type=allure.attachment_type.PNG)

@allure.title("Test HerokuApp")
@allure.description("Testing various features of the HerokuApp website")
class TestHerokuApp(unittest.TestCase):

    def setUp(self):
        #Method that runs in the beggining of each test
        self.driver = webdriver.Chrome()
        self.driver.maximize_window()
 
    def tearDown(self):
        #Method that runs in the end of each test
        take_screenshot_and_attach(self.driver)
        self.driver.close()

    @allure.story("Testing of adding and removing elements.")
    def test_add_remove_page(self):

        # Open main page
        with allure.step("Open the main page."):
            self.driver.get("https://the-internet.herokuapp.com/")
        
        # Add two buttons
        with allure.step("Add two elements."):
            addRemoveElement = WebDriverWait(self.driver, 10).until(EC.presence_of_element_located((By.XPATH, "//ul//li//a[text()='Add/Remove Elements']")))
            addRemoveElement.click()
            addButton = self.driver.find_element(By.XPATH, "//button[text()='Add Element']")
            addButton.click()
            addButton.click()

        # Check that two buttons are visible
        with allure.step("Check that two buttons are visible."):
            deleteButton = self.driver.find_elements(By.XPATH, "//button[text()='Delete']")
            self.assertEqual(len(deleteButton), 2)

        # Check that one button is visible
        with allure.step("Check that one button is visible."):
            deleteButton[0].click()
            deleteButton = self.driver.find_elements(By.XPATH, "//button[text()='Delete']")
            self.assertEqual(len(deleteButton),1)

    @allure.story("Testing of selecting checkboxes.")
    def test_checkbox(self):
        #Test which gives information about status of checkbox
        with allure.step("Open page with checkboxes exercise."):
            self.driver.get("https://the-internet.herokuapp.com/checkboxes")
        
        # Checking if first checkbox is already selected
        with allure.step("Checking selection of checkbox."):
            checkbox = self.driver.find_elements(By.XPATH, '//input[@type="checkbox"]')
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
    
    @allure.story("Testing of dropdown list.")
    def test_dropdown(self):
        #Test which asserts chosen element of dropdown
        with allure.step("Open page with dropdown exercise."):
            self.driver.get('https://the-internet.herokuapp.com/dropdown')
        with allure.step("Find and click wanted option of dropdown list."):
            dropdown = self.driver.find_element(By.XPATH, "//select[@id='dropdown']")
            dropdown.click()
            dropdownElements = self.driver.find_elements(By.XPATH, '//select[@id="dropdown"]//option')
            dropdownElements[2].click()
            self.assertTrue(dropdownElements[2].is_selected())
    
    @allure.story("Testing of dragging and dropping elements.")
    def test_drag_and_drop(self):
        #Test which drags one element and drops on another element
        with allure.step("Open page with drag and drop exercise."):
            from selenium.webdriver import ActionChains
            self.driver.get("https://the-internet.herokuapp.com/drag_and_drop")

        columnA = self.driver.find_element(By.XPATH, "//div[@id='column-a']")
        columnB = self.driver.find_element(By.XPATH, "//div[@id='column-b']")

        with allure.step("Move element from column A to column B."):
        #Making element move with the use of ActionChains
            actionChains = ActionChains(self.driver)
            actionChains.drag_and_drop(source=columnA, target=columnB).perform()

        #Making sure that elements place was changed
        with allure.step("Make assertion about position of elements."):
            self.assertEqual(columnA.text, 'B')
            self.assertEqual(columnB.text, 'A')