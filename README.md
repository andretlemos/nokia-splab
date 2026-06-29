# Nokia SROS SPLab

This repository contains a containerlab-based lab for exploring Nokia SROS networking concepts, automated configuration deployment, and multi-domain routing scenarios. The project is currently under development and is intended to evolve into a more complete automation and validation environment.

## Overview

The lab combines:
- Nokia SR-SIM routers running SROS
- Cisco IOS routers for external AS simulation
- Linux-based client nodes
- Automation tools such as Nornir, Ansible, and NetBox-related components

The goal is to build a realistic service-provider-style topology for testing routing, provisioning, and configuration workflows.

## Topology

The main topology is defined in [clab/lab.clab.yml](clab/lab.clab.yml).

[Topology](clab/nokia-splab.png)


### Devices included
- Core routers: p1, p2, p3, p4
- Provider edge routers: pe1, pe2, pe3, pe4
- Autonomous systems: as1, as2, as3, as4
- Client hosts: client1, client2

### Topology layout
- A core ring is built between p1, p2, p3, and p4
- Each PE router is connected to one core router
- Each PE router establishes eBGP peering with one AS router
- Client hosts are connected to pe3 and pe4

### For running this lab is required SR-SIM license file and adjust the file clab;lab.clab.yml

## Repository structure

- [clab](clab): containerlab topology files, licenses, and generated lab artifacts
- [src](src): configuration templates, inventory, and automation modules
- [backup-netbox](backup-netbox): scripts related to NetBox database backup and restore

## Project status

This project is still under development. Some automation flows, documentation, and deployment steps may change as the lab evolves.

## Getting started

Prerequisites:
- Docker or Podman
- containerlab
- Python 3.12+

Typical workflow:
1. Deploy the Netbox docker (netbox-docker) and after import the backup using the file netbox-database-import.sh on backup-netbox/ folder
2. Deploy the lab with containerlab using the topology file in [clab/lab.clab.yml](clab/lab.clab.yml)
3. Use the automation code under [src](src) to generate or deploy configurations
4. Extend the templates and inventory as needed for new scenarios

## Notes

The project currently focuses on lab topology definition and configuration automation scaffolding. More complete usage examples and operational documentation will be added over time.
