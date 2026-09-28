# Azure Virtual Desktop: host pools, identity, and profiles

**Environment:** Hands-on training project at NetSoft College of Technology. This page is based on my lab notes; production tenant details and credentials are omitted.

## Goal
Deliver managed Windows desktops and applications from Azure with secure access and persistent user profiles.

## Architecture
- Microsoft Entra ID and Active Directory identity for user access and domain join.
- Azure virtual network, storage accounts, and file shares supporting session hosts.
- Azure Virtual Desktop host pools, workspaces, session hosts, and published applications.
- FSLogix profiles for user state across sessions.

## Work completed
1. Built host pools, workspaces, and virtual desktops with Windows 10/11 multisession and Windows Server 2025 images.
2. Configured session hosts, remote applications, scaling plans, and a reference image for repeatable provisioning.
3. Implemented FSLogix profile disks and tested application persistence between sessions.
4. Worked with MSIX App Attach and application images for delivery tests.
5. Applied MFA, Conditional Access, user risk and session controls in the identity environment.
6. Used Azure Portal and PowerShell for deployment and administration.

## Validation recorded in my notes
Connectivity and RDP access, licensing, user sign-in, profiles, and hybrid identity integration were tested. The lab notes do not include a reproducible export of the tenant or measurements of session performance.

## Interview discussion
The design connects identity, network, storage, and session hosts. I can explain where a sign-in failure, unavailable desktop, or missing FSLogix profile would be investigated, and how scaling affects cost and user experience.

**Next evidence to add:** Redacted host pool and workspace screenshots, a topology diagram, a sample PowerShell deployment with placeholders, and a sign-in/profile test log.
