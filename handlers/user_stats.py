# handlers/user_stats.py

from pyrogram import Client, filters

def user_details_callback(client: Client, callback_query):
    user_id = int(callback_query.data.split("_")[2])
    user = client.get_users(user_id)
    details = (f"Name: {user.first_name} {user.last_name or ''}\n"
               f"Username: @{user.username or 'N/A'}\n"
               f"ID: {user.id}\n"
               f"Expiration Date: {premium_users[user_id].strftime('%Y-%m-%d')}")
    client.send_message(callback_query.message.chat.id, details)
