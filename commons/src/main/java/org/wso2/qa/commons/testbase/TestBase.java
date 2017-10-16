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

package org.wso2.qa.commons.testbase;

import org.openqa.selenium.By;
import org.openqa.selenium.WebDriver;
import org.openqa.selenium.WebElement;
import org.slf4j.Logger;
import org.slf4j.LoggerFactory;
import org.wso2.qa.commons.util.ElementLocatorProperties;
import org.wso2.qa.commons.util.TestSuiteProperties;

import java.io.IOException;

public class TestBase {

    private static final Logger logger = LoggerFactory.getLogger(TestBase.class);
    DriverManager driverManager = new DriverManager();

    protected WebDriver driver;

    protected void init() {
        this.driver = driverManager.getWebDriver(TestSuiteProperties.getInstance().getElement("driver"));
    }

    public String getMgtConsoleURL() {
        logger.info("accessing Management Console LoginOperations page");
        return "https://is.dev.wso2.org/carbon/admin/index.jsp";
    }

    public String getMgtConsoleLogout() {
        logger.info("logging out of Management Console");
        return "https://is.dev.wso2.org/carbon/admin/logout_action.jsp";
    }

    protected WebElement getlLogout() throws IOException {
        return driver.findElement(By.xpath
                (ElementLocatorProperties.getInstance().getElement("link.logout")));
    }
}
