package org.wso2.qa.commons.testbase;

import org.slf4j.Logger;
import org.slf4j.LoggerFactory;

public class TestBase {

    private static final Logger logger = LoggerFactory.getLogger(TestBase.class);

    public String getMgtConsoleURL() {
        return "https://localhost:9443/carbon/admin/login.jsp";
    }
}
