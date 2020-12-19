#!/usr/bin/env python3
# This Source Code Form is subject to the terms of the GNU
# General Public License, v.3.0. If a copy of the GPL was not distributed with this
# file, You can obtain one at https://www.gnu.org/licenses/gpl-3.0.en.html.

print("Online Session String Generator For Ionxix")


print("Telethon (docs.telethon.dev)")
print("Ionxix - https://github.com/Ion-cell/Ionix")

print("Select your required option: ")
s_l = input("Enter y / n ? ?? ")

if s_l == "y":

  from telethon.sync import TelegramClient
  from telethon.sessions import StringSession
  APP_ID = int(input("Enter APP ID here: "))
  API_HASH = input("Enter API HASH here: ")
  with TelegramClient(
    StringSession(), 
    APP_ID, 
    API_HASH
  ) as client:
    session_str = client.session.save()
    s_m = client.send_message("me", session_str)
    s_m.reply("⬆️ The above one is your SESSION_STRING. Go back to the deploy page and paste this there. Get help From @xark047  if needed.")
    print("Please check your Telegram Saved Messages for the SESSION_STRING ")

elif s_l == "n":
  print ("Okay, your choice, see you... ")
else:
  print("Please select y / n only. ")
