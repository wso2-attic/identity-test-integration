<%--
  ~ Copyright (c) 2016, WSO2 Inc. (http://www.wso2.org) All Rights Reserved.
  ~
  ~ WSO2 Inc. licenses this file to you under the Apache License,
  ~ Version 2.0 (the "License"); you may not use this file except
  ~ in compliance with the License.
  ~ You may obtain a copy of the License at
  ~
  ~ http://www.apache.org/licenses/LICENSE-2.0
  ~
  ~ Unless required by applicable law or agreed to in writing,
  ~ software distributed under the License is distributed on an
  ~ "AS IS" BASIS, WITHOUT WARRANTIES OR CONDITIONS OF ANY
  ~ KIND, either express or implied.  See the License for the
  ~ specific language governing permissions and limitations
  ~ under the License.
  --%>

<%@page import="java.util.ArrayList" %>
<%@page import="java.util.Arrays" %>
<%@ page import="java.util.List" %>
<%@ page import="java.util.Map" %>
<%@page import="org.wso2.carbon.identity.application.authentication.endpoint.util.Constants" %>
<%@ page language="java" contentType="text/html; charset=UTF-8" pageEncoding="UTF-8" %>
<%@ taglib prefix="fmt" uri="http://java.sun.com/jsp/jstl/fmt" %>
<%@ page import="org.wso2.carbon.identity.application.authentication.endpoint.util.TenantDataManager" %>

<fmt:bundle basename="org.wso2.carbon.identity.application.authentication.endpoint.i18n.Resources">

    <%
        request.getSession().invalidate();
        String queryString = request.getQueryString();
        Map<String, String> idpAuthenticatorMapping = null;
        if (request.getAttribute(Constants.IDP_AUTHENTICATOR_MAP) != null) {
            idpAuthenticatorMapping = (Map<String, String>) request.getAttribute(Constants.IDP_AUTHENTICATOR_MAP);
        }

        String errorMessage = "Authentication Failed! Please Retry";
        String authenticationFailed = "false";

        if (Boolean.parseBoolean(request.getParameter(Constants.AUTH_FAILURE))) {
            authenticationFailed = "true";

            if (request.getParameter(Constants.AUTH_FAILURE_MSG) != null) {
                errorMessage = request.getParameter(Constants.AUTH_FAILURE_MSG);

                 if (errorMessage.equalsIgnoreCase("authentication.fail.message")) {
                    errorMessage = "Authentication Failed! Please Retry";
                }
            }
        }
    %>

    <html>
    <head>
        <meta charset="utf-8">
        <meta name="viewport" content="width=device-width, initial-scale=1.0">
        <title>WSO2 Identity Server</title>

        <link rel="icon" href="images/favicon.png" type="image/x-icon"/>
        <link href="libs/bootstrap_3.3.5/css/bootstrap.min.css" rel="stylesheet">
        <link href="css/Roboto.css" rel="stylesheet">
        <link href="css/custom-common.css" rel="stylesheet">

        <script src="js/scripts.js"></script>
        <script src="assets/js/jquery-1.7.1.min.js"></script>
        <!--[if lt IE 9]>
        <script src="js/html5shiv.min.js"></script>
        <script src="js/respond.min.js"></script>
        <![endif]-->
    </head>

    <body onload="getLoginDiv()">

    <!-- header -->
    <header class="header header-default">
        <div class="container-fluid"><br></div>
        <div class="container-fluid">
            <div class="pull-left brand float-remove-xs text-center-xs">
                <a href="#">
                    <img src="images/logo-inverse.svg" alt="wso2" title="wso2" class="logo">

                    <h1><em>Identity Server</em></h1>
                </a>
            </div>
        </div>
    </header>

    <!-- page content -->
    <div class="container-fluid body-wrapper">

        <div class="row">
            <div class="col-md-12">

                <!-- content -->
                <div class="container col-xs-10 col-sm-6 col-md-6 col-lg-4 col-centered wr-content wr-login col-centered">
                    <div>
                        <h2 class="wr-title blue-bg padding-double white boarder-bottom-blue margin-none">
                            Change your password &nbsp;&nbsp;
                    </div>
                    <div class="boarder-all ">
                        <div class="clearfix"></div>
                        <div class="padding-double login-form">
         <div id="errorDiv"></div>
          <%
                if ("true".equals(authenticationFailed)) {
                %>
                    <div class="alert alert-danger" id="failed-msg">
                        <%=errorMessage%>
                    </div>
                <% }

                %>
          <form id="pin_form" name="pin_form" action="../../commonauth"  method="POST">
               <div id="loginTable1" class="identity-box">


            <%
                   String loginFailed = request.getParameter("authFailure");
                   if (loginFailed != null && "true".equals(loginFailed)) {
               String authFailureMsg = request.getParameter("authFailureMsg");
               if (authFailureMsg != null && "login.fail.message".equals(authFailureMsg)) {
               %>


      <% } }  %>

          <div class="row">
             <div class="span6">
                <!-- Token Pin -->
                <div class="control-group">

                </div>
                <input type="hidden" name="sessionDataKey"
                   value='<%=request.getParameter("sessionDataKey")%>'/>
                 <div class='col-md-12 form-group'>
                   <div class="col-xs-12 col-sm-12 col-md-12 col-lg-12 form-group">
                           <input id="currentPassword" name="CURRENT_PWD" type="password" class="form-control" tabindex="0"
                                  placeholder="Current Password">
                       </div>
                       <div class="col-xs-12 col-sm-12 col-md-12 col-lg-12 form-group">
                           <input id="newPassword" name="NEW_PWD" type="password" class="form-control"
                                  placeholder="New Password">
                          </div>
                            <div class="col-xs-12 col-sm-12 col-md-12 col-lg-12 form-group">
                           <input id="repeatPassword" name="NEW_PWD_CONFIRMATION" type="password" class="form-control"
                                  placeholder="Repeat Password">
                            </div>
                            <div class='form-row'>
                               <div class='col-md-12 form-group'>
                                 <button class='form-control btn btn-primary submit-button' type='submit' onclick="$('#loading').show();">Change password</button>
                               </div>
                        </div>

                 </div>
                 </div>
                 </div>
                 </form>

                    </div>
                </div>
                <!-- /content -->

            </div>
        </div>
        <!-- /content/body -->

        </div>
    </div>

    <!-- footer -->
    <footer class="footer">
        <div class="container-fluid">
            <p>WSO2 Identity Server | &copy;
                <script>document.write(new Date().getFullYear());</script>
                <a href="http://wso2.com/" target="_blank"><i class="icon fw fw-wso2"></i> Inc</a>. All Rights Reserved.
            </p>
        </div>
    </footer>
    <script src="libs/jquery_1.11.3/jquery-1.11.3.js"></script>
    <script src="libs/bootstrap_3.3.5/js/bootstrap.min.js"></script>
    </body>
    </html>
</fmt:bundle>