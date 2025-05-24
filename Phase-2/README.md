<<<<<<< HEAD
HumHub - Putting People and Pieces together
===========================

[![Test Status](https://github.com/humhub/humhub/workflows/PHP%20Codeception%20Tests/badge.svg)](https://github.com/humhub/humhub/actions)
[![Yii2](https://img.shields.io/badge/Powered_by-Yii_Framework-green.svg?style=flat)](http://www.yiiframework.com/)
[![CLA assistant](https://cla-assistant.io/readme/badge/humhub/humhub)](https://cla-assistant.io/humhub/humhub)

#### **HumHub is an intuitive to use and modular designed open-source software**, used primarily as social network, knowledge database, intranet or information and communication platform.

**The software is written in PHP** and is best described by dividing into 4 main parts: **User, Spaces, Content and Modules.**

- **User:** All users have their own customisable profile (including name, profile picture, cover photo and personal information) and can follow and interact with each other. If wished and enabled, users can create own content, comment posts and join Spaces. Profile fields, permissions and all settings can be defined individually by the network operator (administrator).

- **Spaces:** Rooms or groups for any projects, departments, events or other needs. Network operators can create as many Spaces as needed and automatically map users into the desired Spaces. HumHub comes with an advanced permission and notification system (including email summaries).

- **Content:** Users can create content of all kinds (posts, wiki pages, photo/video, schedule appointments, create events or tasks) depending on their permission and share it with other members in their Space. There is a multi-level comment function, versatile collaboration options and also features to report inappropriate posts and content. All Content, Spaces and Members can be easily found through various and individually definable filter and search functions, Content can be edited, deleted and archived.

- **Modules:** The main software is designed in a modular way and can be extended by approximately 80 modules. These can easily be added to by installation and activation. This gives operators the possibility to set up and configure the network according to their needs and individual wishes. Among the modules are Advanced LDAP, RESTful API, Mass User Import, Calendar, Wiki, OnlyOffice, JWT SSO, Legal Tools, Translation Manager, Custom Themes and Custom Pages, Tasks, Gallery, News, Polls and Mail for Direct Messages.

#### With HumHub, we help people around the world to connect, stay informed, display and share content of various kinds, exchange files and communicate and collaborate with each other.

The software is responsive designed and works great on different devices, including smartphones and tablets. **HumHub is available in over 30 languages and is used in over 4,500 organizations worldwide.**

More information about HumHub can be found here:

-	[Homepage & Demo](http://www.humhub.org/)
-	[Documentation & Class Reference](http://docs.humhub.org/)
-	[Community](http://community.humhub.com/)
-	[Licence](https://www.humhub.com/licences)
=======
# 🔐 Security Evaluation of HumHub Deployment

This repository contains our setup and security evaluation of the **HumHub** open-source social network. We analyzed the local deployment using **OWASP ZAP** to identify potential vulnerabilities.

---

## ✅ Selected Platform

- **Chosen platform:** [HumHub](https://www.humhub.com/)
- **Version used:** PHP-based, Apache server, local installation
- **Purpose:** Evaluate security risks and address key issues

---

## ⚠️ Key Security Findings

We identified three main vulnerabilities in our local deployment using OWASP ZAP:

---

### 1. ❌ Missing Content-Security-Policy (CSP) Header

- **Description:** The application does not set a `Content-Security-Policy` (CSP) header in HTTP responses.
- **Risk:** Medium
- **Impact:** Absence of CSP allows for a broader attack surface, increasing the risk of XSS (Cross-Site Scripting) and code injection.
- **Fix:**
  - Add the following header to your Apache or PHP configuration:
    ```http
    Content-Security-Policy: default-src 'self'; script-src 'self'; object-src 'none'; frame-ancestors 'none';
    ```

---

### 2. ❌ Apache Server Status Page Exposed

- **URL:** `http://localhost/server-status`
- **Risk:** Medium
- **Impact:** The Apache `server-status` endpoint reveals sensitive information about active connections, software versions, and server uptime.
- **Fix:**
  - Restrict access to local requests only:
    ```apache
    <Location /server-status>
        SetHandler server-status
        Require local
    </Location>
    ```

---

### 3. ❌ Directory Browsing Enabled

- **Path:** `/humhub/assets/`
- **Risk:** Medium
- **Impact:** Public users can list files in this directory, potentially exposing sensitive files or scripts.
- **Fix:**
  - Disable directory listing in `.htaccess` or Apache config:
    ```apache
    Options -Indexes
    ```

---

## ✅ Post-Fix Validation

After applying the above fixes, we re-ran the OWASP ZAP scan and verified that the issues no longer appear in the results.

---
>>>>>>> 8b9fddc17ac8d3dc8bdd26121e4d44833008005b

