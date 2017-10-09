package org.wso2.qa.commons.pageobjects;

import org.openqa.selenium.By;
import org.openqa.selenium.WebDriver;
import org.openqa.selenium.WebElement;

public class MenuItems {

    private static WebElement element = null;

    // Main Tab in menu
    public static WebElement tabMain(WebDriver webDriver) {
        element = webDriver.findElement(By.xpath("/html/body/table/tbody/tr[2]/td[1]/div[2]/span"));
        return element;
    }

    // Monitor Tab in menu
    public static WebElement tabMonitor(WebDriver webDriver) {
        element = webDriver.findElement(By.xpath("/html/body/table/tbody/tr[2]/td[1]/div[3]/span"));
        return element;
    }

    // Configure Tab in menu
    public static WebElement tabConfigure(WebDriver webDriver) {
        element = webDriver.findElement(By.xpath("/html/body/table/tbody/tr[2]/td[1]/div[4]/span"));
        return element;
    }

    // Tools Tab in menu
    public static WebElement tabTools(WebDriver webDriver) {
        element = webDriver.findElement(By.xpath("/html/body/table/tbody/tr[2]/td[1]/div[5]/span"));
        return element;
    }

    // Main tab --> Identity tab
    public static WebElement mainTabIdentity(WebDriver webDriver) {
        element = webDriver.findElement(By.xpath("//*[@id=\"region1_identity_menu\"]"));
        return element;
    }

    // Main --> Identity --> Users and Roles add
    public static WebElement userNrolesAdd(WebDriver webDriver) {
        element = webDriver.findElement(By.xpath
                ("/html/body/table/tbody/tr[2]/td[2]/table/tbody/tr[1]/td/div/ul/li[3]/ul/li[2]/ul/li[1]/a"));
        return element;
    }

    // Main --> Identity --> Users and Roles list
    public static WebElement userNrolesList(WebDriver webDriver) {
        element = webDriver.findElement(By.xpath
                ("/html/body/table/tbody/tr[2]/td[2]/table/tbody/tr[1]/td/div/ul/li[3]/ul/li[2]/ul/li[2]/a"));
        return element;
    }

    public static WebElement userStoresAdd(WebDriver webDriver) {
        element = webDriver.findElement(By.xpath
                ("/html/body/table/tbody/tr[2]/td[2]/table/tbody/tr[1]/td/div/ul/li[3]/ul/li[4]/ul/li[1]/a"));
        return element;
    }

    public static WebElement userStoresList(WebDriver webDriver) {
        element = webDriver.findElement(By.xpath
                ("/html/body/table/tbody/tr[2]/td[2]/table/tbody/tr[1]/td/div/ul/li[3]/ul/li[4]/ul/li[2]/a"));
        return element;
    }

    public static WebElement claimsAdd(WebDriver webDriver) {
        element = webDriver.findElement(By.xpath
                ("/html/body/table/tbody/tr[2]/td[2]/table/tbody/tr[1]/td/div/ul/li[3]/ul/li[6]/ul/li[1]/a"));
        return element;
    }

    public static WebElement claimsList(WebDriver webDriver) {
        element = webDriver.findElement(By.xpath
                ("/html/body/table/tbody/tr[2]/td[2]/table/tbody/tr[1]/td/div/ul/li[3]/ul/li[6]/ul/li[2]/a"));
        return element;
    }

    public static WebElement spAdd(WebDriver webDriver) {
        element = webDriver.findElement(By.xpath
                ("/html/body/table/tbody/tr[2]/td[2]/table/tbody/tr[1]/td/div/ul/li[3]/ul/li[8]/ul/li[1]/a"));
        return element;
    }

    public static WebElement spList(WebDriver webDriver) {
        element = webDriver.findElement(By.xpath
                ("/html/body/table/tbody/tr[2]/td[2]/table/tbody/tr[1]/td/div/ul/li[3]/ul/li[8]/ul/li[2]/a"));
        return element;
    }

    public static WebElement spResident(WebDriver webDriver) {
        element = webDriver.findElement(By.xpath
                ("/html/body/table/tbody/tr[2]/td[2]/table/tbody/tr[1]/td/div/ul/li[3]/ul/li[8]/ul/li[3]/a"));
        return element;
    }

    public static WebElement idpAdd(WebDriver webDriver) {
        element = webDriver.findElement(By.xpath
                ("/html/body/table/tbody/tr[2]/td[2]/table/tbody/tr[1]/td/div/ul/li[3]/ul/li[8]/ul/li[1]/a"));
        return element;
    }

    public static WebElement idpList(WebDriver webDriver) {
        element = webDriver.findElement(By.xpath
                ("/html/body/table/tbody/tr[2]/td[2]/table/tbody/tr[1]/td/div/ul/li[3]/ul/li[10]/ul/li[2]/a"));
        return element;
    }

    public static WebElement idpResident(WebDriver webDriver) {
        element = webDriver.findElement(By.xpath
                ("/html/body/table/tbody/tr[2]/td[2]/table/tbody/tr[1]/td/div/ul/li[3]/ul/li[10]/ul/li[3]/a"));
        return element;
    }

}
