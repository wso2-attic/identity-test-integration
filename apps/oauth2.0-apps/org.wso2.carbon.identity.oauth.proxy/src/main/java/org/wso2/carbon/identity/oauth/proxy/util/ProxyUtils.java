package org.wso2.carbon.identity.oauth.proxy.util;

import java.io.File;
import java.io.FileInputStream;
import java.io.FileNotFoundException;
import java.io.IOException;
import java.io.UnsupportedEncodingException;
import java.net.URI;
import java.security.InvalidAlgorithmParameterException;
import java.security.InvalidKeyException;
import java.security.NoSuchAlgorithmException;
import java.util.Properties;

import javax.crypto.BadPaddingException;
import javax.crypto.Cipher;
import javax.crypto.IllegalBlockSizeException;
import javax.crypto.NoSuchPaddingException;
import javax.crypto.spec.IvParameterSpec;
import javax.crypto.spec.SecretKeySpec;
import javax.ws.rs.core.Response;

import org.apache.axiom.om.util.Base64;
import org.apache.commons.httpclient.HttpStatus;
import org.apache.commons.logging.Log;
import org.apache.commons.logging.LogFactory;
import org.wso2.carbon.identity.oauth.proxy.bean.ErrorResponse;

/**
 * 
 *
 */
public class ProxyUtils {

    private final static Log log = LogFactory.getLog(ProxyUtils.class);

    public static final String ID_TOKEN = "id_token";
    public static final String ACCESS_TOKEN = "access_token";
    public static final String REFRESH_TOKEN = "refresh_token";
    public static final String EXPIRATION = "expires_in";
    public static final String SPA_NAME = "spa_name";

    public static final String PROXY_API = "/";

    public static final String IS_AUTHORIZATION_EP = "/oauth2/authorize";
    public static final String IS_TOKEN_EP = "/oauth2/token";

    public static final String IS_SERVER_EP = "is_server_ep";

    public static final String SECRET_KEY = "secret_key";
    public static final String IV = "iv";

    public static final String CLIENT_ID = "client_id";
    public static final String CLIENT_SECRET = "client_secret";

    public static final String OAUTH_GRANT_TYPE_CODE = "code";
    public static final String SCOPE = "scope.";
    public static final String OPENID_SCOPE = "openid";

    private static final String PROXY_ROPERTIES_FILE = "oauth_proxy.properties";
    private static final String OAUTH_PROXY_CONFIG_PATH = "oauth.proxy.property.file.path";
    private static final String SP_CALLBACK_URL_MAPPING = "sp_callback_url_mapping.";
    private static final String SP_CLOGOUT_URL_MAPPING = "sp_logout_url_mapping.";

    private static final String PROXY_CALLBACK_URL = "proxy_callback_url";

    private static Properties properties = new Properties();

    static {

        FileInputStream fileInputStream = null;
        String configPath = System.getProperty(OAUTH_PROXY_CONFIG_PATH,
                System.getProperty("carbon.home") + File.separator + "repository" + File.separator + "conf");

        try {
            configPath = configPath + File.separator + PROXY_ROPERTIES_FILE;
            fileInputStream = new FileInputStream(new File(configPath));
            properties.load(fileInputStream);
        } catch (FileNotFoundException e) {
            log.error(e);
            throw new RuntimeException(PROXY_ROPERTIES_FILE + " property file not found in " + configPath, e);
        } catch (IOException e) {
            log.error(e);
            throw new RuntimeException(PROXY_ROPERTIES_FILE + " property file reading error from " + configPath, e);
        } finally {
            if (fileInputStream != null) {
                try {
                    fileInputStream.close();
                } catch (Exception exx) {
                    log.error("Error occured while closing the file stream :" + exx);
                }
            }
        }
    }

    /**
     * status of the operation.
     */
    public enum OperationStatus {
        SUCCESS, BAD_REQUEST, NOT_FOUND, FORBIDDEN, CREATED, INTERNAL_SERVER_ERROR
    }

    /**
     * 
     * @return
     */
    public static String getAuthzEp() {
        return getProperty(IS_SERVER_EP, null) + IS_AUTHORIZATION_EP;
    }

    /**
     * 
     * @return
     */
    public static String getTokenEp() {
        return getProperty(IS_SERVER_EP, null) + IS_TOKEN_EP;
    }

    /**
     * 
     * @param spaName
     * @return
     */
    public static String getConsumerKey(String spaName) {
        return getProperty(CLIENT_ID + "." + spaName, getProperty(CLIENT_ID, null));
    }

    /**
     * 
     * @param spaName
     * @return
     */
    public static String getConsumerSecret(String spaName) {
        return getProperty(CLIENT_SECRET + "." + spaName, getProperty(CLIENT_SECRET, null));

    }

    /**
     * 
     * @return
     */
    public static String getAuthzGrantType() {
        return OAUTH_GRANT_TYPE_CODE;
    }

    /**
     * 
     * @param spaName
     * @return
     */
    public static String getScope(String spaName) {
        return getProperty(SCOPE + spaName.toLowerCase(), OPENID_SCOPE);

    }

    /**
     * 
     * @param spName
     * @return
     */
    public static String getSpaCallbackUrl(String spaName) {
        return getProperty(SP_CALLBACK_URL_MAPPING + spaName.toLowerCase(), null);
    }

    /**
     * 
     * @param spName
     * @return
     */
    public static String getSpaLogoutUrl(String spaName) {
        return getProperty(SP_CLOGOUT_URL_MAPPING + spaName.toLowerCase(), null);
    }

    /**
     * 
     * @return
     */
    public static String getCallbackUrl() {
        return getProperty(PROXY_CALLBACK_URL, null);
    }

    /**
     * creates the response to be sent to the calling application, by the API.
     * 
     * @param responseStatus
     * @param code
     * @param name
     * @param detail
     * @return
     */
    public static Response handleResponse(ProxyUtils.OperationStatus responseStatus, String code, String name,
            String detail) {
        Response response;

        String message = name;
        ErrorResponse resp = new ErrorResponse(code, name, detail);

        switch (responseStatus) {
        case CREATED:
            response = Response.created(URI.create(message)).build();
            break;
        case SUCCESS:
            response = Response.ok().entity(resp).build();
            break;
        case BAD_REQUEST:
            response = Response.status(HttpStatus.SC_BAD_REQUEST).entity(resp).build();
            break;
        case NOT_FOUND:
            response = Response.status(HttpStatus.SC_NOT_FOUND).entity(resp).build();
            break;
        case FORBIDDEN:
            response = Response.status(HttpStatus.SC_UNAUTHORIZED).entity(resp).build();
            break;
        case INTERNAL_SERVER_ERROR:
            response = Response.status(HttpStatus.SC_INTERNAL_SERVER_ERROR).entity(resp).build();
            break;
        default:
            response = Response.noContent().build();
        }
        if (log.isDebugEnabled()) {
            log.debug(resp.toString());
        }
        return response;
    }

    /**
     * 
     * @param key
     * @param defaultValue
     * @return
     */
    private static String getProperty(String key, String defaultValue) {
        String propValue = (String) properties.get(key);
        return propValue != null && !propValue.trim().isEmpty() ? propValue.trim() : defaultValue;
    }

    /**
     * 
     * @param plaintext
     * @return
     * @throws NoSuchAlgorithmException
     * @throws NoSuchPaddingException
     * @throws IllegalBlockSizeException
     * @throws BadPaddingException
     * @throws UnsupportedEncodingException
     * @throws InvalidKeyException
     * @throws InvalidAlgorithmParameterException
     */
    public static String encrypt(String plaintext)
            throws NoSuchAlgorithmException, NoSuchPaddingException, IllegalBlockSizeException, BadPaddingException,
            UnsupportedEncodingException, InvalidKeyException, InvalidAlgorithmParameterException {

        String key = properties.getProperty(SECRET_KEY);

        if (key == null) {
            throw new InvalidKeyException("No secret key is defined in the configuration file.");
        }

        String initVector = properties.getProperty(IV);

        if (initVector == null) {
            throw new InvalidKeyException("No initialization vector is defined in the configuration file.");
        }

        IvParameterSpec iv = new IvParameterSpec(initVector.getBytes("UTF-8"));
        SecretKeySpec skeySpec = new SecretKeySpec(key.getBytes("UTF-8"), "AES");
        Cipher cipher = Cipher.getInstance("AES/CBC/PKCS5PADDING");
        cipher.init(Cipher.ENCRYPT_MODE, skeySpec, iv);
        byte[] encrypted = cipher.doFinal(plaintext.getBytes());
        return Base64.encode(encrypted);

    }

    /**
     * 
     * @param encrypted
     * @return
     * @throws UnsupportedEncodingException
     * @throws NoSuchAlgorithmException
     * @throws NoSuchPaddingException
     * @throws IllegalBlockSizeException
     * @throws BadPaddingException
     * @throws InvalidKeyException
     * @throws InvalidAlgorithmParameterException
     */
    public static String decrypt(String encrypted)
            throws UnsupportedEncodingException, NoSuchAlgorithmException, NoSuchPaddingException,
            IllegalBlockSizeException, BadPaddingException, InvalidKeyException, InvalidAlgorithmParameterException {

        String key = properties.getProperty(SECRET_KEY);

        if (key == null) {
            throw new InvalidKeyException("No secret key is defined in the configuration file.");
        }

        String initVector = properties.getProperty(IV);

        if (initVector == null) {
            throw new InvalidKeyException("No initialization vector is defined in the configuration file.");
        }

        IvParameterSpec iv = new IvParameterSpec(initVector.getBytes("UTF-8"));
        SecretKeySpec skeySpec = new SecretKeySpec(key.getBytes("UTF-8"), "AES");

        Cipher cipher = Cipher.getInstance("AES/CBC/PKCS5PADDING");
        cipher.init(Cipher.DECRYPT_MODE, skeySpec, iv);
        byte[] original = cipher.doFinal(Base64.decode(encrypted));
        return new String(original);
    }

}
