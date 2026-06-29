import os
from dotenv import load_dotenv
from nornir import InitNornir

BASE_DIR = os.path.dirname(os.path.dirname(__file__))

load_dotenv(os.path.join(BASE_DIR, ".env"))

nr = InitNornir(
    config_file=os.path.join(BASE_DIR, "config.yaml"),
    inventory={
        "plugin": "NetBoxInventory2",
        "options": {
            "nb_url": os.getenv("NETBOX_URL"),
            "nb_token": os.getenv("NETBOX_TOKEN"),
            "defaults_file": os.path.join(BASE_DIR, "inventory", "defaults.yaml"),
        },
    },
    runner={
        "plugin": "threaded",
        "options": {"num_workers": 10},
    },
)
