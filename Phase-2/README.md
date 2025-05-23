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

