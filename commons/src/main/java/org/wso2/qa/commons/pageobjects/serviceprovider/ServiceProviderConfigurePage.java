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

/**
 * Service Provider Configuration Page locator class
 * <p>
 * TODO - move element values into the property file
 */
public class ServiceProviderConfigurePage {

    private static WebElement element = null;

    public static WebElement txtBoxServiceProviderName(WebDriver webDriver) {
        element = webDriver.findElement(By.xpath("//*[@id=\"spName\"]"));
        return element;
    }

    public static WebElement txtBoxServiceProviderDescription(WebDriver driver) {
        element = driver.findElement(By.xpath("//*[@id=\"sp-description\"]"));
        return element;
    }

    public static WebElement chkBoxSAAS(WebDriver driver) {
        element = driver.findElement(By.xpath("//*[@id=\"isSaasApp\"]"));
        return element;
    }

    /*
     * Configuration tabs
     */

    public static WebElement tabClaimConfiguration(WebDriver driver) {
        element = driver.findElement(By.xpath
                ("//*[@id=\"claims_head\"]"));
        return element;
    }

    public static WebElement tabRolePermissionConfiguration(WebDriver driver) {
        element = driver.findElement(By.xpath
                ("//*[@id=\"authorization_permission_head\"]"));
        return element;
    }

    public static WebElement tabInboundAuthenticationConfiguration(WebDriver driver) {
        element = driver.findElement(By.xpath
                ("//*[@id=\"app_authentication_head\"]"));
        return element;
    }

    public static WebElement tabLocalOutboundAuthenticationConfiguration(WebDriver driver) {
        element = driver.findElement(By.xpath
                ("//*[@id=\"app_authentication_advance_head\"]"));
        return element;
    }

    public static WebElement tabInboundProvisioningConfiguration(WebDriver driver) {
        element = driver.findElement(By.xpath
                ("//*[@id=\"inbound_provisioning_head\"]"));
        return element;
    }

    public static WebElement tabOutboundProvisioningConfiguration(WebDriver driver) {
        element = driver.findElement(By.xpath
                ("//*[@id=\"outbound_provisioning_head\"]"));
        return element;
    }
}

