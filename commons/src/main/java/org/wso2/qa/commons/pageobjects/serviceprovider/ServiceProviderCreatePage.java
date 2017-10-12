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

package org.wso2.qa.commons.pageobjects.serviceprovider;

import org.openqa.selenium.By;
import org.openqa.selenium.WebDriver;
import org.openqa.selenium.WebElement;
import org.wso2.qa.commons.util.ElementLocatorProperties;

/**
 * Service Provider creator page locator class
 * <p>
 */
public class ServiceProviderCreatePage {

    private WebElement element;
    private WebDriver driver;

    public ServiceProviderCreatePage(WebDriver driver) {
        this.driver = driver;
    }

    public WebElement txtBoxServiceProviderName() {
        element = driver.findElement(By.xpath
                (ElementLocatorProperties.getInstance().getElement("page.spcreate.txtbox.spname")));
        return element;
    }

    public WebElement txtBoxServiceProvierDescription() {
        element = driver.findElement(By.xpath
                (ElementLocatorProperties.getInstance().getElement("page.spcreate.txtbox.spdescription")));
        return element;
    }

    public WebElement btnRegister() {
        element = driver.findElement(By.xpath
                (ElementLocatorProperties.getInstance().getElement("page.spcreate.btn.register")));
        return element;
    }

    public WebElement btnCancel() {
        element = driver.findElement(By.xpath
                (ElementLocatorProperties.getInstance().getElement("page.spcreate.btn.cancel")));
        return element;
    }
}
