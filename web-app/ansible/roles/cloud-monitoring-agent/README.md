cloud-monitoring-agent
========

[![Build Status](https://drone-opsdev.rax.io/github.com/rack-roles/cloud-monitoring-agent/status.svg?branch=master)](https://drone-opsdev.rax.io/github.com/rack-roles/cloud-monitoring-agent)

This role installs and configures the Rackspace Cloud monitoring agent.

Requirements
------------

Requires a Rackspace Public Cloud server to run completely unattended. See [Issue 4](https://github.com/rack-roles/cloud-backup-agent/issues/4).

Role Variables
--------------

### General

* `rackspace_username`: Pass your Rackspace username to configure the agent.
* `rackspace_apikey`: Pass your Rackspace apikey to configure the agent.
* `cloud_monitoring_agent_force_setup`: Force the setup command to run even if the bootstrap file exists.
* `cloud_monitoring_default_checks`: A series of default checks applied to the agent.
* `cloud_monitoring_additional_checks`: A series of additional checks to be applied to the agent.

### Checks

Each check has a series of variables that can be modified.

* `cloud_monitoring_{{check_name}}_period`: The period of the check.
* `cloud_monitoring_{{check_name}}_timeout`: The timeout of the check.
* `cloud_monitoring_{{check_name}}_target`: Only applies to certain checks. Sets the target of the check. ("/" or "etho" as examples.)
* `cloud_monitoring_{{check_name}}_alarm`: Whether or not to enable the alarm section of the file. (Default: False)

### Network Alarms

* `cloud_monitoring_network_receive_critical`: Set this based on your expected max throughput. (Default: 76)
* `cloud_monitoring_network_receive_warning`: Set this based on your expected max throughput. (Default: 56)
* `cloud_monitoring_network_transmit_critical`: Set this based on your expected max throughput. (Default: 76)
* `cloud_monitoring_network_transmit_warning`: Set this based on your expected max throughput. (Default: 56)

Dependencies
------------

None

Example Playbook
-------------------------

Including an example of how to use your role (for instance, with variables passed in as parameters) is always nice for users too:

    - hosts: servers
      roles:
         - { role: Rackspace_Automation.cloud-monitoring-agent, x: 42 }

License
-------

BSD

Author Information
------------------

[Rackspace - the open cloud company](http://rackspace.com)

Ask about our DevOps Automation Service - [www.rackspace.com/devops](http://rackspace.com/devops)
