Dante
=========

Dante socks proxy server https://www.inet.no/dante/

Installation
--------------

```yaml
- src: git@github.com:alexey1607/ansible-dante.git
  scm: git
  version: master
  name: dante
```

Role Variables
--------------
### dante_user
- Dante user
- Default value: *dante*

### dante_group
- Dante group
- Default value: *dante*

### dante_config
- Dante config path
- Default value: */etc/danted.conf*

### dante_logs
- Dante logs path
- Default value: */var/log/sockd.log*

### dante_interface
- Dante interface
- Default value: *0.0.0.0*

### dante_port
- Dante port
- Default value: *1080*

Requirements
------------
* Debian
  - 9 (stretch)
  - 10 (buster)
  - 11 (bullseye)

Example Playbook
----------------
```
- name: Install dante-server
  hosts: helsinki
  roles:
    - dante
```

License
-------

BSD

Author Information
------------------

Alexey1607
