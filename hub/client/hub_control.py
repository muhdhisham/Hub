import json
import os
import time
from hub import config
from hub.client.base import HubHttpClient
from hub.client.auth import AuthClient
from pathlib import Path

from hub.exceptions import NotFoundException


class HubControlClient(HubHttpClient):
    """
    Controlling Hub through rest api
    """

    def __init__(self):
        super(HubControlClient, self).__init__()
        self.details = self.get_config()

    def get_dataset_path(self, tag):
        try:
            dataset = self.request(
                "GET",
                config.GET_DATASET_PATH_SUFFIX,
                params={"tag": tag},
                endpoint=config.HUB_REST_ENDPOINT,
            ).json()
        except NotFoundException:
            dataset = None

        return dataset

    def get_credentials(self):

        if self.auth_header is None:
            token = AuthClient().get_access_token(username="public", password="")
            self.auth_header = f"Bearer {token}"

        r = self.request(
            "GET", config.GET_CREDENTIALS_SUFFIX, endpoint=config.HUB_REST_ENDPOINT,
        ).json()

        details = {
            "_id": r["_id"],
            "region": r["region"],
            "session_token": r["session_token"],
            "access_key": r["access_key"],
            "secret_key": r["secret_key"],
            "endpoint": r["endpoint"],
            "expiration": r["expiration"],
            "bucket": r["bucket"],
        }

        self.save_config(details)
        return details

    def get_config(self, reset=False):

        if not os.path.isfile(config.STORE_CONFIG_PATH) or self.auth_header is None:
            self.get_credentials()

        with open(config.STORE_CONFIG_PATH, "r") as file:
            details = file.readlines()
            details = json.loads("".join(details))

        if float(details["expiration"]) < time.time() - 36000 or reset:
            details = self.get_credentials()
        return details

    def save_config(self, details):
        path = Path(config.STORE_CONFIG_PATH)
        os.makedirs(path.parent, exist_ok=True)
        with open(config.STORE_CONFIG_PATH, "w") as file:
            file.writelines(json.dumps(details))

    def create_dataset_entry(self, username, dataset_name, meta, public=True):
        try:
            tag = f"{username}/{dataset_name}"
            repo = f"public/{username}" if public else f"private/{username}"
            print(tag, repo, public)
            self.request(
                "POST",
                config.CREATE_DATASET_SUFFIX,
                json={
                    "tag": tag,
                    "repository": repo,
                    "public": public,
                    "rewrite": True
                },
                endpoint=config.HUB_REST_ENDPOINT,
            ).json()
        except Exception as e:
            print("Unable to create Dataset entry")
            print(e)

    def update_dataset_state(self, username, dataset_name, state, progress=0):
        try:
            tag = f"{username}/{dataset_name}"
            self.request(
                "POST",
                config.UPDATE_STATE_SUFFIX,
                json={
                    "tag": tag,
                    "state": state,
                    "progress": progress,
                },
                endpoint=config.HUB_REST_ENDPOINT,
            ).json()
        except Exception as e:
            print("Unable to update Dataset entry state")
            print(e)

    def delete_dataset_entry(self, username, dataset_name):
        try:
            tag = f"{username}/{dataset_name}"
            suffix = f"{config.DATASET_SUFFIX}/{tag}"
            self.request(
                "DELETE",
                suffix,
                endpoint=config.HUB_REST_ENDPOINT,
            ).json()
        except Exception as e:
            print("Unable to delete Dataset entry")
            print(e)
