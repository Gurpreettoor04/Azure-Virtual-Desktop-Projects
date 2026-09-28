# Azure Virtual Desktop inventory

Read-only Python tool for checking Azure Virtual Desktop resources in one subscription. It lists host pools, workspaces, application groups, and the number of session hosts in each host pool. It makes no changes to Azure.

## Requirements

- Python 3.9 or later
- Azure CLI 2.55 or later with the `desktopvirtualization` extension
- Reader access to the AVD resources in the selected subscription

## Run

```bash
az login
az extension add --name desktopvirtualization
az account list -o table
python3 inventory.py --subscription "<subscription-id>"
```

Use `--json` to print structured output. If you have no AVD resources, the summary shows zero resources. The script selects the requested subscription and verifies that selection before reading resources. It never retrieves registration tokens or user sessions.

## Test without Azure

```bash
python3 -m unittest discover -s tests -v
```

The tests use a fake Azure CLI and sample response data. They verify the report logic and command selection. A live Azure run remains to be performed in your account.

The project is inspired by my Azure Virtual Desktop training lab, where I configured host pools, workspaces, session hosts, applications, identity, and FSLogix. It is newly authored portfolio code and should not be mistaken for an export from that lab.

Microsoft reference: [Azure CLI Desktop Virtualization commands](https://learn.microsoft.com/en-us/cli/azure/desktopvirtualization) and [Session Hosts REST list](https://learn.microsoft.com/en-us/rest/api/desktopvirtualization/session-hosts/list?view=rest-desktopvirtualization-2024-04-03).
