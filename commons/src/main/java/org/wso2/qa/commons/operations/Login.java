package org.wso2.qa.commons.operations;

import org.openqa.selenium.WebDriver;
import org.wso2.qa.commons.pageobjects.LoginPage;
import org.wso2.qa.commons.testbase.TestBase;

public class Login {

    private TestBase base = new TestBase();

    public void executeLogin(String username, String password, WebDriver driver) {
        driver.get(base.getMgtConsoleURL());
        LoginPage.txtBoxUsername(driver).sendKeys(username);
        LoginPage.txtBoxPassword(driver).sendKeys(password);
        LoginPage.btnSignIn(driver).click();
    }

    public void executeLogout(WebDriver driver) {
        driver.get(base.getMgtConsoleLogout());
    }
}
