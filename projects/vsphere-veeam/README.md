# VMware vSphere and Veeam backup and recovery

**Environment:** ESXi 8, vCenter Server Appliance, Active Directory, iSCSI/NFS storage, and Veeam Backup & Replication Community Edition in a training environment.

## Goal
Build a virtual infrastructure with shared storage and tested VM recovery.

## Virtualization work
- Configured ESXi hosts, vCenter, datacenters, clusters, and AD-based role access.
- Created standard and distributed virtual switches, VLANs, NIC teaming, VMFS datastores, and iSCSI/NFS connections.
- Practiced HA, DRS, vMotion, EVC, Fault Tolerance, Storage DRS, snapshots, templates, replication, and Lifecycle Manager remediation.

## Backup work
- Connected VMware infrastructure to Veeam and configured repositories and VM backup jobs.
- Performed guest file restores and Instant VM Recovery tests.
- Used an NFS repository and repeated disaster recovery exercises according to my lab notes.

## Validation recorded in my notes
The notes report backup integrity and recovery testing, but do not include job logs, recovery time measurements, or configuration exports. I would add redacted evidence before quoting recovery objectives.

## Interview discussion
A backup is useful only when a restore works. I can describe which VM and application checks matter after guest file restore or Instant VM Recovery.

**Next evidence to add:** Redacted topology and job screenshots, restore checklist, and recovery test log.
