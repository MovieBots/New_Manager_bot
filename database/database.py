# database.py

import json
import os

DATABASE_FILE = "premium_users.json"
ADMINS_FILE = "admins.txt"

def load_premium_users():
    if os.path.exists(DATABASE_FILE):
        with open(DATABASE_FILE, "r") as f:
            return json.load(f)
    return {}

def save_premium_users(premium_users):
    with open(DATABASE_FILE, "w") as f:
        json.dump(premium_users, f)

def load_admin_ids():
    if os.path.exists(ADMINS_FILE):
        with open(ADMINS_FILE, "r") as f:
            return set(int(line.strip()) for line in f.readlines())
    return set()

def save_admin_ids(admin_ids):
    with open(ADMINS_FILE, "w") as f:
        for admin_id in admin_ids:
            f.write(str(admin_id) + "\n")
