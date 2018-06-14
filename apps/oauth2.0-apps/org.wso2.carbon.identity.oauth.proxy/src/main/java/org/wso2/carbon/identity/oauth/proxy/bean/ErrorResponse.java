package org.wso2.carbon.identity.oauth.proxy.bean;

import javax.xml.bind.annotation.XmlAccessType;
import javax.xml.bind.annotation.XmlAccessorType;
import javax.xml.bind.annotation.XmlAttribute;
import javax.xml.bind.annotation.XmlRootElement;
import javax.xml.bind.annotation.XmlType;

import com.google.gson.Gson;
import com.google.gson.annotations.SerializedName;

@XmlAccessorType(XmlAccessType.FIELD)
@XmlType(propOrder = { "error_code", "error_type", "error_message" })
@XmlRootElement(name = "error_response")
public class ErrorResponse {

    @XmlAttribute(name = "error_code")
    @SerializedName("error_code")
    private String code;
    @SerializedName("error_type")
    @XmlAttribute(name = "error_type")
    private String type;
    @SerializedName("error_message")
    @XmlAttribute(name = "error_message")
    private String message;

    private static final Gson gson = new Gson();

    public ErrorResponse() {
    }

    /**
     * 
     * @param code
     * @param type
     * @param message
     */
    public ErrorResponse(String code, String type, String message) {
        this.code = code;
        this.type = type;
        this.message = message;
    }

    /**
     * 
     * @return
     */
    public String getCode() {
        return code;
    }

    /**
     * 
     * @param code
     */
    public void setCode(String code) {
        this.code = code;
    }

    /**
     * 
     * @return
     */
    public String getType() {
        return type;
    }

    /**
     * 
     * @param type
     */
    public void setType(String type) {
        this.type = type;
    }

    /**
     * 
     * @return
     */
    public String getMessage() {
        return message;
    }

    /**
     * 
     * @param message
     */
    public void setMessage(String message) {
        this.message = message;
    }

    /**
     * 
     * @param json
     * @return
     */
    public static ErrorResponse buildFromJson(String json) {
        return gson.fromJson(json, ErrorResponse.class);
    }

}