# network-automation-labs
Hands-on network automation labs using Python, Ansible, NAPALM, NETCONF/RESTCONF, and GNS3/VIRL, from fundamentals to advanced workflows for real-world infrastructure.
# Network Automation Labs

This repository contains hands-on **network** automation labs built around real-world scenarios using Python, Ansible, NAPALM, NETCONF/RESTCONF, and GNS3/VIRL/Containerlab. The goal is to practice end‑to‑end workflows: from device onboarding and configuration management to validation and troubleshooting.

## Goals

- Build a solid foundation in modern network automation concepts and tooling.
- Practice automating multivendor network devices using Python and Ansible.
- Learn to use APIs and data models (NETCONF/RESTCONF/YANG) for network programmability.
- Develop repeatable lab environments using GNS3, VIRL, or container-based topologies.
- Apply DevOps/DevSecOps practices (Git, CI, testing) to network changes.

## Lab structure

Each lab lives in its own directory with configs, automation code, and documentation:

```text
labs/
  01-basic-cli-automation/
  02-ansible-inventory-and-playbooks/
  03-templates-and-jinja2/
  04-netconf-restconf-yang/
  05-validation-and-testing/
  06-git-ci-for-network-changes/
  07-gns3-topologies/
  08-cloud-networking-labs/
