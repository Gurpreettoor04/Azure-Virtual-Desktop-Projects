#!/usr/bin/env python3
"""Read-only Azure Virtual Desktop resource inventory."""

import argparse
import json
import re
import subprocess
import sys
from urllib.parse import quote


def az_json(*args):
    """Execute Azure CLI and parse its JSON output."""
    command = ["az", *args, "--output", "json"]
    result = subprocess.run(command, capture_output=True, text=True, check=False)
    if result.returncode:
        raise RuntimeError(result.stderr.strip() or f"Azure CLI failed: {command[1]}")
    if not result.stdout.strip():
        return {}
    try:
        return json.loads(result.stdout)
    except json.JSONDecodeError as error:
        raise RuntimeError("Azure CLI returned invalid JSON") from error


def resource_group(resource_id):
    match = re.search(r"/resourceGroups/([^/]+)/", resource_id, re.IGNORECASE)
    if not match:
        raise ValueError(f"Host pool has no resource group: {resource_id}")
    return match.group(1)


def session_hosts(subscription, pool):
    group = resource_group(pool["id"])
    url = (
        "https://management.azure.com/subscriptions/"
        + quote(subscription, safe="")
        + "/resourceGroups/"
        + quote(group, safe="")
        + "/providers/Microsoft.DesktopVirtualization/hostPools/"
        + quote(pool["name"], safe="")
        + "/sessionHosts?api-version=2024-04-03"
    )
    count = 0
    while url:
        page = az_json("rest", "--method", "get", "--url", url)
        count += len(page.get("value", []))
        url = page.get("nextLink")
        if url and not url.startswith("https://management.azure.com/"):
            raise RuntimeError("Unexpected pagination URL from Azure")
    return count


def collect(subscription):
    az_json("account", "set", "--subscription", subscription)
    account = az_json("account", "show")
    if account.get("id", "").lower() != subscription.lower():
        raise RuntimeError("The selected subscription does not match the requested ID")

    pools = az_json("desktopvirtualization", "hostpool", "list")
    workspaces = az_json("desktopvirtualization", "workspace", "list")
    groups = az_json("desktopvirtualization", "applicationgroup", "list")
    return {
        "subscription": subscription,
        "host_pools": [
            {
                "name": pool["name"],
                "resource_group": resource_group(pool["id"]),
                "location": pool.get("location", ""),
                "session_host_count": session_hosts(subscription, pool),
            }
            for pool in pools
        ],
        "workspaces": [
            {"name": item["name"], "resource_group": resource_group(item["id"])}
            for item in workspaces
        ],
        "application_groups": [
            {"name": item["name"], "resource_group": resource_group(item["id"])}
            for item in groups
        ],
    }


def main():
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("--subscription", required=True, help="Azure subscription ID")
    parser.add_argument("--json", action="store_true", help="Print structured JSON")
    args = parser.parse_args()
    try:
        report = collect(args.subscription)
    except (RuntimeError, ValueError, KeyError) as error:
        print(f"Inventory failed: {error}", file=sys.stderr)
        return 1
    if args.json:
        print(json.dumps(report, indent=2))
    else:
        print(f"Subscription: {report['subscription']}")
        print(f"Host pools: {len(report['host_pools'])}")
        for pool in report["host_pools"]:
            print(
                f"  {pool['name']} ({pool['resource_group']}, {pool['location']}): "
                f"{pool['session_host_count']} session host(s)"
            )
        print(f"Workspaces: {len(report['workspaces'])}")
        print(f"Application groups: {len(report['application_groups'])}")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
