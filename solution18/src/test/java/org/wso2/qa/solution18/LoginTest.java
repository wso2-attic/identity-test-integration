package org.wso2.qa.solution18;

import org.openqa.selenium.WebDriver;
import org.testng.annotations.Test;
import org.wso2.qa.commons.operations.LoginOperations;
import org.wso2.qa.commons.pageobjects.MenuItems;

public class LoginTest {

    private org.wso2.qa.commons.testbase.DriverManager driverManager = new org.wso2.qa.commons.testbase.DriverManager();
    private LoginOperations login = new LoginOperations();

    private WebDriver driver;

    @Test
    public void loginTest() throws InterruptedException {
        String username = "admin";
        String password = "admin";
        driver = driverManager.getWebDriver("chrome");
        login.executeLogin(username, password, driver);

        // check menu items
        MenuItems.tabMain(driver).click();
        MenuItems.tabMonitor(driver).click();
        MenuItems.tabConfigure(driver).click();
        MenuItems.tabTools(driver).click();

        // check main menu items
        MenuItems.tabMain(driver).click();
        MenuItems.userNrolesAdd(driver).click();
        MenuItems.userNrolesList(driver).click();
        MenuItems.userStoresAdd(driver).click();
        MenuItems.userStoresList(driver).click();
        MenuItems.claimsAdd(driver).click();
        MenuItems.claimsList(driver).click();
        MenuItems.spAdd(driver).click();
        MenuItems.spList(driver).click();
        MenuItems.spResident(driver).click();
        MenuItems.idpAdd(driver).click();
        MenuItems.idpList(driver).click();
        MenuItems.idpResident(driver).click();

        login.executeLogout(driver);
        driver.close();
    }
}
