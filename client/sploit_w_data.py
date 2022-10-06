#!/usr/bin/env python3

from time import sleep
from typing import List
import requests
import threading

DF_HOST = ""
DF_PORT = 0

SPLOIT_NAME = ""
SERVICE_NAME = ""

# Make sure fields are set
assert DF_HOST and SPLOIT_NAME and SERVICE_NAME
assert DF_PORT > 0

resp = requests.get(f"http://{DF_HOST}:{DF_PORT}/api/get_config")
assert resp.status_code == 200

config = resp.json()


def send_flags(team_name: str, flags: List[str]):

    sending = [
        {"flag": flag, "sploit": SPLOIT_NAME, "team": team_name} for flag in flags
    ]

    print(f"[{threading.current_thread().name}] Sending {len(sending)} flags...")

    requests.post(
        f"http://{DF_HOST}:{DF_PORT}/api/post_flags",
        headers={"Content-type": "application/json"},
        json=sending,
    )
    print(f"[{threading.current_thread().name}] OK.")

#CHANGEME
def get_flag_ids():
    #try:
    #    return requests.get("http://PATH/TO/FLAG_IDS/").json()
    #except:
    #    return []
    pass


def loop(team_name: str, ip: str, flag_ids: List[str]):
    flags = []

    ############# WRITE SCRIPT HERE #############

    #################### END ####################

    send_flags(team_name, flags)


while True:
    flag_ids = get_flag_ids()

    for team_name, ip in config["TEAMS"].items():
        try:
            threading.Thread(
                target=loop,
                args=(team_name, ip, flag_ids[SERVICE_NAME][ip]),
                name=team_name,
            ).start()
        except:
            print(f"Could not start thread.")

    sleep(config["SUBMIT_PERIOD"])
