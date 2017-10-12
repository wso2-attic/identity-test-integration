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

package org.wso2.qa.commons.pageobjects.login;

import org.openqa.selenium.By;
import org.openqa.selenium.WebDriver;
import org.openqa.selenium.WebElement;
import org.wso2.qa.commons.util.ElementLocatorProperties;

/**
 * Page Object Model for login page
 */
public class LoginPage {

    private WebElement element;
    private WebDriver driver;

    public LoginPage(WebDriver driver) {
        this.driver = driver;
    }

    public WebElement txtBoxUsername() {
        element = driver.findElement(By.xpath
                (ElementLocatorProperties.getInstance().getElement("page.login.txtbox.username")));
        return element;
    }

    public WebElement txtBoxPassword() {
        element = driver.findElement(By.xpath
                (ElementLocatorProperties.getInstance().getElement("page.login.txtbox.password")));
        return element;
    }

    public WebElement btnSignIn() {
        element = driver.findElement(By.xpath
                (ElementLocatorProperties.getInstance().getElement("page.login.btn.signin")));
        return element;
    }
}
