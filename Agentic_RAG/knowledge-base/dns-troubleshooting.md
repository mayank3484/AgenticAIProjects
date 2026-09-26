# DNS Troubleshooting Guide

## Common DNS Problems

### 1. Slow DNS Resolution
- **Symptoms**: Web pages take more than 10 seconds to load
- **Solution**:
  - Flush DNS cache: `ipconfig /flushdns` (Windows) or `sudo dscacheutil -flushcache` (Mac)
  - Check DNS server settings in network configuration
  - Try using public DNS servers: 8.8.8.8 or 1.1.1.1

### 2. Name Resolution Failure
- **Symptoms**: "Host not found" or "DNS server not responding"
- **Solution**:
  - Test with nslookup or dig command
  - Verify DNS server addresses are correct
  - Check if firewall is blocking DNS traffic (port 53)

### 3. Internal vs External Resolution
- **Symptoms**: Can access external sites but not internal resources
- **Solution**:
  - Ensure internal DNS servers are configured
  - Check split-horizon DNS setup
  - Verify DNS forwarding rules

## DNS Configuration Steps

1. Open network settings
2. Navigate to DNS configuration
3. Set primary DNS server: 10.10.1.10 (company internal)
4. Set secondary DNS server: 8.8.8.8 (public fallback)
5. Save and restart network services

## Troubleshooting Checklist

- [ ] Test DNS resolution with nslookup
- [ ] Check if other devices have same issue
- [ ] Verify DNS server addresses are correct
- [ ] Ensure firewall allows DNS traffic
