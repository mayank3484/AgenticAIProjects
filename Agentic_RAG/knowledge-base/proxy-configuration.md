# Proxy Configuration Guide

## Corporate Proxy Setup

### 1. Browser Proxy Settings
- **Chrome/Edge**: Settings > Advanced > System > Open proxy settings
- **Firefox**: Preferences > Network Settings > Settings > Manual proxy configuration
- **Proxy Address**: proxy.company.com:8080
- **Authentication**: Username and password required for company network

### 2. Command Line Proxy
- **Git**:
  ```
  git config --global http.proxy http://user:pass@proxy.company.com:8080
  git config --global https.proxy https://user:pass@proxy.company.com:8080
  ```

- **Wget**:
  ```
  wget --proxy=on --http-proxy=http://user:pass@proxy.company.com:8080
  ```

### 3. System-wide Proxy
- **Linux**: 
  - Set environment variables:
    ```
    export http_proxy=http://user:pass@proxy.company.com:8080
    export https_proxy=https://user:pass@proxy.company.com:8080
    ```

## Common Proxy Issues

### 1. Authentication Failure
- **Symptoms**: "407 Proxy Authentication Required"
- **Solution**:
  - Verify proxy credentials are correct
  - Check if authentication is required for specific URLs
  - Clear cached credentials in browser

### 2. SSL/TLS Errors
- **Symptoms**: "SSL certificate verification failed"
- **Solution**:
  - Update system certificates
  - Configure application to accept self-signed certificates
  - Add company CA certificate to trust store

### 3. Connection Timeout
- **Symptoms**: Slow or no response from proxy
- **Solution**:
  - Test proxy connectivity with telnet
  - Check if proxy is configured correctly
  - Try bypassing proxy for direct connection

## Proxy Troubleshooting Checklist

- [ ] Verify proxy address and port are correct
- [ ] Confirm authentication credentials work
- [ ] Test proxy connectivity before application use
- [ ] Ensure system certificates are up to date