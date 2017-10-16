/*
 *  Copyright (c) 2017, WSO2 Inc. (http://www.wso2.org) All Rights Reserved.
 *
 *  WSO2 Inc. licenses this file to you under the Apache License,
 *  Version 2.0 (the "License"); you may not use this file except
 *  in compliance with the License.
 *  You may obtain a copy of the License at
 *
 *     http://www.apache.org/licenses/LICENSE-2.0
 *
 *  Unless required by applicable law or agreed to in writing,
 *  software distributed under the License is distributed on an
 *  "AS IS" BASIS, WITHOUT WARRANTIES OR CONDITIONS OF ANY
 *  KIND, either express or implied.  See the License for the
 *  specific language governing permissions and limitations
 *  under the License.
 */

package org.wso2.qa.commons.pageobjects.menus;

import org.openqa.selenium.By;
import org.openqa.selenium.WebDriver;
import org.openqa.selenium.WebElement;

/**
 * Menu Items locator class
 * <p>
 * TODO - move element values into the property file
 */
public class MenuItems {

    private WebElement element;
    private WebDriver driver;

    public MenuItems(WebDriver driver) {
        this.driver = driver;
    }

    // Main Tab in menu
    public WebElement tabMain() {
        element = driver.findElement(By.xpath("/html/body/table/tbody/tr[2]/td[1]/div[2]/span"));
        return element;
    }

    // Monitor Tab in menu
    public WebElement tabMonitor() {
        element = driver.findElement(By.xpath("/html/body/table/tbody/tr[2]/td[1]/div[3]/span"));
        return element;
    }

    // Configure Tab in menu
    public WebElement tabConfigure() {
        element = driver.findElement(By.xpath("/html/body/table/tbody/tr[2]/td[1]/div[4]/span"));
        return element;
    }

    // Tools Tab in menu
    public WebElement tabTools() {
        element = driver.findElement(By.xpath("/html/body/table/tbody/tr[2]/td[1]/div[5]/span"));
        return element;
    }

    // Main tab --> Identity tab
    public WebElement mainTabIdentity() {
        element = driver.findElement(By.xpath("//*[@id=\"region1_identity_menu\"]"));
        return element;
    }

    // Main --> Identity --> Users and Roles add
    public WebElement userNrolesAdd() {
        element = driver.findElement(By.xpath
                ("/html/body/table/tbody/tr[2]/td[2]/table/tbody/tr[1]/td/div/ul/li[3]/ul/li[2]/ul/li[1]/a"));
        return element;
    }

    // Main --> Identity --> Users and Roles list
    public WebElement userNrolesList() {
        element = driver.findElement(By.xpath
                ("/html/body/table/tbody/tr[2]/td[2]/table/tbody/tr[1]/td/div/ul/li[3]/ul/li[2]/ul/li[2]/a"));
        return element;
    }

    public WebElement userStoresAdd() {
        element = driver.findElement(By.xpath
                ("/html/body/table/tbody/tr[2]/td[2]/table/tbody/tr[1]/td/div/ul/li[3]/ul/li[4]/ul/li[1]/a"));
        return element;
    }

    public WebElement userStoresList() {
        element = driver.findElement(By.xpath
                ("/html/body/table/tbody/tr[2]/td[2]/table/tbody/tr[1]/td/div/ul/li[3]/ul/li[4]/ul/li[2]/a"));
        return element;
    }

    public WebElement claimsAdd() {
        element = driver.findElement(By.xpath
                ("/html/body/table/tbody/tr[2]/td[2]/table/tbody/tr[1]/td/div/ul/li[3]/ul/li[6]/ul/li[1]/a"));
        return element;
    }

    public WebElement claimsList() {
        element = driver.findElement(By.xpath
                ("/html/body/table/tbody/tr[2]/td[2]/table/tbody/tr[1]/td/div/ul/li[3]/ul/li[6]/ul/li[2]/a"));
        return element;
    }

    public WebElement spAdd() {
        element = driver.findElement(By.xpath
                ("/html/body/table/tbody/tr[2]/td[2]/table/tbody/tr[1]/td/div/ul/li[3]/ul/li[8]/ul/li[1]/a"));
        return element;
    }

    public WebElement spList() {
        element = driver.findElement(By.xpath
                ("/html/body/table/tbody/tr[2]/td[2]/table/tbody/tr[1]/td/div/ul/li[3]/ul/li[8]/ul/li[2]/a"));
        return element;
    }

    public WebElement spResident() {
        element = driver.findElement(By.xpath
                ("/html/body/table/tbody/tr[2]/td[2]/table/tbody/tr[1]/td/div/ul/li[3]/ul/li[10]/ul/li[3]/a"));
        return element;
    }

    public WebElement idpAdd() {
        element = driver.findElement(By.xpath
                ("/html/body/table/tbody/tr[2]/td[2]/table/tbody/tr[1]/td/div/ul/li[3]/ul/li[8]/ul/li[1]/a"));
        return element;
    }

    public WebElement idpList() {
        element = driver.findElement(By.xpath
                ("/html/body/table/tbody/tr[2]/td[2]/table/tbody/tr[1]/td/div/ul/li[3]/ul/li[10]/ul/li[2]/a"));
        return element;
    }

    public WebElement idpResident() {
        element = driver.findElement(By.xpath
                ("/html/body/table/tbody/tr[2]/td[2]/table/tbody/tr[1]/td/div/ul/li[3]/ul/li[10]/ul/li[3]/a"));
        return element;
    }

}
