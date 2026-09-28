import unittest
from unittest.mock import patch
import sys
from pathlib import Path

sys.path.insert(0, str(Path(__file__).resolve().parents[1]))
import inventory


class InventoryTests(unittest.TestCase):
    def test_collect_and_count_session_hosts(self):
        resource = "/subscriptions/test-sub/resourceGroups/rg-avd/providers/Microsoft.DesktopVirtualization/"
        responses = [
            {},
            {"id": "test-sub"},
            [{"id": resource + "hostPools/pool-a", "name": "pool-a", "location": "canadacentral"}],
            [{"id": resource + "workspaces/workspace-a", "name": "workspace-a"}],
            [{"id": resource + "applicationGroups/apps-a", "name": "apps-a"}],
            {"value": [{"name": "host-1"}, {"name": "host-2"}]},
        ]
        with patch.object(inventory, "az_json", side_effect=responses) as cli:
            report = inventory.collect("test-sub")
        self.assertEqual(report["host_pools"][0]["session_host_count"], 2)
        self.assertEqual(report["workspaces"][0]["resource_group"], "rg-avd")
        self.assertIn("sessionHosts?api-version=2024-04-03", cli.call_args.args[-1])
        self.assertEqual(cli.call_args.args[:3], ("rest", "--method", "get"))

    def test_refuses_wrong_subscription(self):
        with patch.object(inventory, "az_json", side_effect=[{}, {"id": "another-sub"}]) as cli:
            with self.assertRaises(RuntimeError):
                inventory.collect("test-sub")
        self.assertEqual(cli.call_count, 2)

    def test_rejects_unexpected_pagination_host(self):
        pool = {
            "id": "/subscriptions/test-sub/resourceGroups/rg-avd/providers/Microsoft.DesktopVirtualization/hostPools/p",
            "name": "p",
        }
        with patch.object(inventory, "az_json", return_value={"value": [], "nextLink": "https://example.com/" }):
            with self.assertRaises(RuntimeError):
                inventory.session_hosts("test-sub", pool)


if __name__ == "__main__":
    unittest.main()
