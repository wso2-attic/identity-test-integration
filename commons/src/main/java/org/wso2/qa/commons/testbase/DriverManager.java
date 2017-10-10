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

import org.openqa.selenium.WebDriver;
import org.openqa.selenium.chrome.ChromeDriver;
import org.openqa.selenium.firefox.FirefoxDriver;
import org.openqa.selenium.ie.InternetExplorerDriver;
import org.openqa.selenium.remote.DesiredCapabilities;
import org.openqa.selenium.remote.RemoteWebDriver;

public class DriverManager {

    private WebDriver driver;

    public WebDriver getWebDriver(String driverSelection) {

        if (driverSelection.equalsIgnoreCase("firefox")) {
            System.setProperty("webdriver.gecko.driver", "../drivers/gecko/geckodriver");
            driver = new FirefoxDriver();

        } else if (driverSelection.equalsIgnoreCase("chrome")) {
            System.setProperty("webdriver.chrome.driver", "../drivers/chrome/chromedriver");
            driver = new ChromeDriver();

        } else if (driverSelection.equalsIgnoreCase("remotefirefox")) {
            System.setProperty("webdriver.gecko.driver", "../drivers/gecko/geckodriver");
            DesiredCapabilities capabilities = DesiredCapabilities.firefox();
            capabilities.setCapability("marionette", true);
            WebDriver driver = new RemoteWebDriver(capabilities);


        } else if (driverSelection.equalsIgnoreCase("remotechrome")) {
            System.setProperty("webdriver.chrome.driver", "../drivers/chrome/chromedriver");
            DesiredCapabilities desiredCapabilities = DesiredCapabilities.chrome();


        } else if (driverSelection.equalsIgnoreCase("ie")) {
            driver = new InternetExplorerDriver();

        }
        return driver;
    }
}
