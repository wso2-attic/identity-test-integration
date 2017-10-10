package org.wso2.qa.commons.pageobjects;

import org.openqa.selenium.By;
import org.openqa.selenium.WebDriver;
import org.openqa.selenium.WebElement;

public class ServiceProviderCreatePage {

    private static WebElement element = null;

    public static WebElement txtBoxServiceProviderName(WebDriver webDriver) {
        element = webDriver.findElement(By.xpath("//*[@id=\"spName\"]"));
        return element;
    }

    public static WebElement txtBoxServiceProvierDescription(WebDriver webDriver) {
        element = webDriver.findElement(By.xpath("//*[@id=\"sp-description\"]"));
        return element;
    }

    public static WebElement btnRegister(WebDriver webDriver) {
        element = webDriver.findElement(By.xpath
                ("/html/body/table/tbody/tr[2]/td[3]/table/tbody/tr[2]/td/div/div/form/div[3]/input[1]"));
        return element;
    }

    public static WebElement btnCancel(WebDriver webDriver) {
        element = webDriver.findElement
                (By.xpath("/html/body/table/tbody/tr[2]/td[3]/table/tbody/tr[2]/td/div/div/form/div[3]/input[2]"));
        return element;
    }
}
