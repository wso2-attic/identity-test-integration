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

package org.wso2.qa.commons.operations;

import org.openqa.selenium.By;
import org.openqa.selenium.WebDriver;
import org.openqa.selenium.WebElement;
import org.slf4j.Logger;
import org.slf4j.LoggerFactory;
import org.wso2.qa.commons.pageobjects.login.LoginPage;
import org.wso2.qa.commons.util.ElementLocatorProperties;

import java.io.IOException;
import java.util.List;

public class ServiceProviderOperations {

    private static final Logger logger = LoggerFactory.getLogger(LoginPage.class);
    private WebDriver driver;

    // Initialize and verify page
    public ServiceProviderOperations(WebDriver driver) throws IOException {
        this.driver = driver;
        if (!(driver.getCurrentUrl().contains("list-service-providers.jsp"))) {
            throw new IllegalStateException("This is not the service provider page");
        }
    }

    // Get record count from SP List
    public Integer getRecordCount() {
        List<WebElement> rows = driver.findElements
                (By.xpath(ElementLocatorProperties.getInstance().getElement("page.splist.table.count")));
        return rows.size();
    }

    // Click Edit element for SP
    public void clickServiceProviderEditElement(String spName) {
        for (int i = 1; i <= getRecordCount(); i++) {
            String temp = driver.findElement(By.xpath
                    ("/html/body/table/tbody/tr[2]/td[3]/table/tbody/tr[2]/td/div/div/table[1]/tbody/tr/td/table/" +
                            "tbody/tr[" + i + "]/td[1]")).getText();
            if (temp.equals(spName)) {
                driver.findElement(By.xpath
                        ("/html/body/table/tbody/tr[2]/td[3]/table/tbody/tr[2]/td/div/div/" +
                                "table[1]/tbody/tr/td/table/tbody/tr[" + i + "]/td[3]/a[1]")).click();
            }
        }
    }


    // Click Edit element for SP
    public void clickServiceProviderDeleteElement(String spName) {
        for (int i = 1; i <= getRecordCount(); i++) {
            String temp = driver.findElement(By.xpath
                    ("/html/body/table/tbody/tr[2]/td[3]/table/tbody/tr[2]/td/div/div/table[1]/tbody/tr/td/table/" +
                            "tbody/tr[" + i + "]/td[1]")).getText();
            if (temp.equals(spName)) {
                driver.findElement(By.xpath
                        ("/html/body/table/tbody/tr[2]/td[3]/table/tbody/tr[2]/td/div/div/" +
                                "table[1]/tbody/tr/td/table/tbody/tr[" + i + "]/td[3]/a[2]")).click();
            }
        }
        driver.findElement(By.xpath("/html/body/div[3]/div[2]/button[1]")).click();
    }
}
