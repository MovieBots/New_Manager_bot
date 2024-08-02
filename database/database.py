# database/database.py

import os

admins_file = "admins.txt"

def load_admin_ids():
    admin_ids = set()
    if os.path.exists(admins_file):
        with open(admins_file, "r") as f:
            admin_ids.update(int(line.strip()) for line in f.readlines())
    return admin_ids

def save_admin_ids(admin_ids):
    with open(admins_file, "w") as f:
        for admin_id in admin_ids:
            f.write(str(admin_id) + "\n")
