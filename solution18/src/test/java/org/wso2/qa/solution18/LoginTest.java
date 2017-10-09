package org.wso2.qa.solution18;

import org.openqa.selenium.WebDriver;
import org.testng.annotations.Test;
import org.wso2.qa.commons.pageobjects.LoginPage;
import org.wso2.qa.commons.testbase.TestBase;

public class LoginTest {

    private TestBase base = new TestBase();
    org.wso2.qa.commons.testbase.DriverManager driverManager = new org.wso2.qa.commons.testbase.DriverManager();

    WebDriver driver;

    @Test
    public void loginTest() {
        String username = "admin";
        String password = "admin";
        driver = driverManager.getWebDriver("chrome");
        driver.get(base.getMgtConsoleURL());
        LoginPage.txtBoxUsername(driver).sendKeys(username);
        LoginPage.txtBoxPassword(driver).sendKeys(password);
        LoginPage.btnSignIn(driver).click();
    }
}
