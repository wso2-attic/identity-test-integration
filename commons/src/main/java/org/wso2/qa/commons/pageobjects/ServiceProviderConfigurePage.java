package org.wso2.qa.commons.pageobjects;

import org.openqa.selenium.By;
import org.openqa.selenium.WebDriver;
import org.openqa.selenium.WebElement;

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
