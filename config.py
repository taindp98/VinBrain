#!/usr/bin/env python3
# Copyright (c) Microsoft Corporation. All rights reserved.
# Licensed under the MIT License.

import os

class DefaultConfig:
    """ Bot Configuration """

    PORT = 3978
    APP_ID = os.environ.get("MicrosoftAppId", "")
    APP_PASSWORD = os.environ.get("MicrosoftAppPassword", "")
    BLOB_ACCOUNT_NAME = "audio"
    BLOB_KEY = "5v311ra3pIDPVIuqGOmWhojvwUA3D8ULOx7GiXMKFlCSeWlWO/1bYlv9UIftdcP4ljAxxb7LOv9pkMLOEVBsMA=="
    BLOB_CONTAINER = "storage1011"
