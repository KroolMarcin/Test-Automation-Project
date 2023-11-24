import org.openqa.selenium.WebDriver;
import org.openqa.selenium.WebElement;
import org.openqa.selenium.chrome.ChromeDriver;
import org.openqa.selenium.By;
import org.testng.Assert;
import org.testng.annotations.AfterMethod;
import org.testng.annotations.BeforeMethod;
import org.testng.annotations.Test;

import io.qameta.allure.Allure;
import io.qameta.allure.Step;

import javax.imageio.ImageIO;
import java.io.ByteArrayInputStream;
import java.io.ByteArrayOutputStream;

public class Test_herokuapp {
    private WebDriver driver;

    @BeforeMethod
    public void setUp() {
        driver = new ChromeDriver();
        driver.manage().window().maximize();
    }

    @AfterMethod
    public void tearDown() {
        driver.quit();
    }

    @Test
    public void testAddRemoveElements() {
        openAddRemovePage();
        addElement();
        assertNumberOfButtons(2);
        removeElement();
        assertNumberOfButtons(1);
    }

    @Step("Open the main page.")
    private void openAddRemovePage() {
        driver.get("https://the-internet.herokuapp.com/add_remove_elements/");
        takeScreenshot();
    }

    @Step("Add an element.")
    private void addElement() {
        driver.findElement(By.xpath("//button[text()='Add Element']")).click();
        takeScreenshot();
    }

    @Step("Assert number of 'Delete' buttons is {0}.")
    private void assertNumberOfButtons(int expectedCount) {
        int deleteButtonsCount = driver.findElements(By.xpath("//button[text()='Delete']")).size();
        Assert.assertEquals(deleteButtonsCount, expectedCount);
        takeScreenshot();
    }

    @Step("Remove an element.")
    private void removeElement() {
        driver.findElement(By.xpath("//button[text()='Delete']")).click();
        takeScreenshot();
    }

    @Test
    public void testcheckbox() {
        openCheckboxesPage();
        checkSelection();
        takeScreenshot();
    }

    @Step("Open Checkboxes page")
    private void openCheckboxesPage() {
        driver.get("https://the-internet.herokuapp.com/checkboxes");
        takeScreenshot();
    }
    @Step("Checking selection of element and checking its status.")
    private void checkSelection(){
        WebElement checkbox1 = driver.findElement(By.cssSelector("input[type=checkbox]:nth-child(1)"));
        Assert.assertFalse(checkbox1.isSelected());
        checkbox1.click();
        Assert.assertTrue(checkbox1.isSelected());
    }


    private void takeScreenshot() {
        try {
            ByteArrayOutputStream baos = new ByteArrayOutputStream();
            ImageIO.write(ScreenshotUtils.takeScreenshot(driver), "png", baos);
            Allure.addAttachment("Screenshot", new ByteArrayInputStream(baos.toByteArray()));
        } catch (Exception e) {
            e.printStackTrace();
        }
    }
}