# Intune and Entra ID: endpoint lifecycle and access

**Environment:** Hands-on endpoint management lab at NetSoft College of Technology. This is a project summary based on my notes, not an export of live policies.

## Goal
Enroll and manage devices, deploy applications and updates, and apply identity and endpoint security controls.

## Work completed
- Configured Windows Autopilot deployment profiles, hardware hash import, Microsoft Entra Join, and Company Portal enrollment.
- Created configuration, compliance, device restriction, and Windows Update for Business policies.
- Deployed Microsoft 365 Apps, Win32 packages, and line-of-business applications.
- Configured MFA, self-service password reset, Conditional Access, Identity Protection, and authentication policies.
- Applied BitLocker, Microsoft Defender for Endpoint onboarding, EDR, Firewall policies, Windows LAPS, and security baselines.
- Practiced device lifecycle management across Windows and other endpoint types in the lab.

## Validation to show during an interview
Enrollment status, assignment scope, policy and app deployment status, compliance state, BitLocker recovery key escrow, and sign-in results. My notes describe configuration but do not preserve per-device screenshots or policy exports.

## Design decisions
Start with a test group, check assignment filters and policy conflicts, and verify access before broad deployment. Keep privileged account recovery and Conditional Access exclusions under change control.

**Next evidence to add:** Redacted policy screenshots, an Autopilot enrollment timeline, sample app packaging notes, and a troubleshooting case.
