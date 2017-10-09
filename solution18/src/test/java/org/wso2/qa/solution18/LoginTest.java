package org.wso2.qa.solution18;

import org.openqa.selenium.WebDriver;
import org.testng.annotations.Test;
import org.wso2.qa.commons.operations.Login;
import org.wso2.qa.commons.pageobjects.MenuItems;
import org.wso2.qa.commons.testbase.TestBase;

public class LoginTest {

    private org.wso2.qa.commons.testbase.DriverManager driverManager = new org.wso2.qa.commons.testbase.DriverManager();
    private Login login = new Login();

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

        login.executeLogout(driver);
        driver.close();
    }
}
