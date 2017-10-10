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

import org.openqa.selenium.WebDriver;
import org.wso2.qa.commons.pageobjects.LoginPage;
import org.wso2.qa.commons.testbase.TestBase;

public class LoginOperations {

    private TestBase base = new TestBase();

    public void executeLogin(String username, String password, WebDriver driver) {
        driver.get(base.getMgtConsoleURL());
        LoginPage.txtBoxUsername(driver).sendKeys(username);
        LoginPage.txtBoxPassword(driver).sendKeys(password);
        LoginPage.btnSignIn(driver).click();
    }

    public void executeLogout(WebDriver driver) {
        driver.get(base.getMgtConsoleLogout());
    }
}
