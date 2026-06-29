from dotenv import load_dotenv
import os
import pynetbox

#Load the variables
load_dotenv("../env")
#Connect To Netbox
NETBOX_URL = os.getenv("NETBOX_URL")
NETBOX_TOKEN = os.getenv("NETBOX_TOKEN")
nb = pynetbox.api(NETBOX_URL, token=NETBOX_TOKEN)
