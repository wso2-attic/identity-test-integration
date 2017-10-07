package org.wso2.qa.commons.operations;

import org.openqa.selenium.WebDriver;
import org.wso2.qa.commons.pageobjects.LoginPage;
import org.wso2.qa.commons.testbase.DriverManager;
import org.wso2.qa.commons.testbase.TestBase;

public class Login {

    TestBase base = new TestBase();
    DriverManager driverManager = new DriverManager();

    WebDriver driver;

    public void executeLogin(String username, String password) {
        driver = driverManager.getWebDriver("chrome");
        driver.get(base.getMgtConsoleURL());
        LoginPage.txtBoxUsername(driver).sendKeys(username);
        LoginPage.txtBoxPassword(driver).sendKeys(password);
        LoginPage.btnSignIn(driver).click();
    }
}
