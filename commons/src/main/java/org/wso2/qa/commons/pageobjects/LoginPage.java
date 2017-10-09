package org.wso2.qa.commons.pageobjects;

import org.openqa.selenium.By;
import org.openqa.selenium.WebDriver;
import org.openqa.selenium.WebElement;

/**
 * Page Object Model for login page
 */
public class LoginPage {

    private static WebElement element = null;

    public static WebElement txtBoxUsername(WebDriver webDriver) {
        element = webDriver.findElement(By.id("txtUserName"));
        return element;
    }

    public static WebElement txtBoxPassword(WebDriver webDriver) {
        element = webDriver.findElement(By.id("txtPassword"));
        return element;
    }

    public static WebElement btnSignIn(WebDriver webDriver) {
        element = webDriver.findElement(By.className("button"));
        return element;
    }
}
