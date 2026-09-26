# Git Access Troubleshooting

## Common Git Access Problems

### 1. Permission Denied
- **Symptoms**: "Permission denied (publickey)" or "fatal: unable to access"
- **Solution**:
  - Verify SSH key is added to ssh-agent: `ssh-add -l`
  - Check if key is in correct location: `~/.ssh/id_rsa` or `~/.ssh/id_ed25519`
  - Ensure proper repository permissions in GitLab/GitHub
  - Generate new SSH keys if necessary

### 2. Network Connectivity Issues
- **Symptoms**: Timeout errors, connection refused
- **Solution**:
  - Test connectivity: `ping git.company.com`
  - Check proxy settings if behind corporate firewall
  - Verify VPN is connected when accessing internal repositories
  - Try using HTTPS instead of SSH

### 3. Authentication Failure
- **Symptoms**: "Authentication failed" or "Invalid username or password"
- **Solution**:
  - Regenerate personal access tokens in GitLab
  - Update credential helper: `git config --global credential.helper store`
  - Clear cached credentials: `git credential-cache exit`

## Git Configuration Steps

1. Configure Git user:
   ```
   git config --global user.name "John Doe"
   git config --global user.email "john.doe@company.com"
   ```

2. Set up SSH keys:
   ```
   ssh-keygen -t ed25519 -C "john.doe@company.com"
   ssh-add ~/.ssh/id_ed25519
   ```

3. Add key to GitLab:
   - Copy public key: `cat ~/.ssh/id_ed25519.pub`
   - Paste into GitLab Settings > SSH Keys

## Troubleshooting Checklist

- [ ] Verify VPN is connected for internal repositories
- [ ] Check SSH agent has keys loaded
- [ ] Test git clone with HTTPS as fallback
- [ ] Ensure correct repository URL format