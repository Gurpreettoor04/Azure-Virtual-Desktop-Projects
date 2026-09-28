# RHEL administration and Ansible automation

**Environment:** Multiple Red Hat Enterprise Linux virtual machines in a training lab, with an Ansible controller and managed hosts.

## Goal
Administer Linux hosts consistently and automate repeatable changes.

## Linux administration
- Installed and registered RHEL; managed packages, repositories, updates, systemd services, cron, and logs.
- Configured users, groups, sudo, ACLs, passwords, and SSH key access.
- Worked with partitions, filesystems, swap, LVM, Stratis, and persistent mounts.
- Practiced networking, DNS, NTP, firewalld, and SELinux troubleshooting.

## Ansible work
- Built inventories and configured controller-to-host SSH access.
- Used ad hoc commands and playbooks with variables, facts, loops, conditionals, handlers, blocks, error handling, and reusable roles.
- Applied Jinja2 templates, lineinfile and blockinfile; used Ansible Vault for sensitive configuration data.

## Validation and evidence
My notes describe multi-host automation and troubleshooting, but do not include the original playbook files or run output. This page documents the completed lab at a summary level; future examples will be clearly identified as recreated samples.

## Interview discussion
I can explain idempotency, inventory grouping, privilege escalation, handling secrets with Vault, and diagnosing a host that fails a playbook.

**Next evidence to add:** A sanitized inventory, one tested playbook, and redacted before/after output.
