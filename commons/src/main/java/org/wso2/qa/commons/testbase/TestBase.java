package org.wso2.qa.commons.testbase;

import org.slf4j.Logger;
import org.slf4j.LoggerFactory;

public class TestBase {

    private static final Logger logger = LoggerFactory.getLogger(TestBase.class);

    public String getMgtConsoleURL() {
        logger.info("accessing Management Console LoginOperations page");
        return "https://localhost:9443/carbon/admin/index.jsp";
    }

    public String getMgtConsoleLogout() {
        logger.info("logging out of Management Console");
        return "https://localhost:9443/carbon/admin/logout_action.jsp";
    }
}
