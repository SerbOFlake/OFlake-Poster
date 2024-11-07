# cli.poster.py
import configparser
import sys
import os
import asyncio
from telegram import Bot

def read_template(template_path):
    with open(template_path, 'r', encoding='utf-8') as file:
        return file.read()

def replace_placeholders(template, placeholders):
    for key, value in placeholders.items():
        template = template.replace(f'{{${key}}}', value)
    return template

async def send_message(token, channel_id, message):
    bot = Bot(token=token)
    await bot.send_message(chat_id=channel_id, text=message)

def main():
    if len(sys.argv) < 4:
        print("Usage: python cli.poster.py --channel <channel> --sample <template_file> [+<placeholder> <value>]...")
        sys.exit(1)

    channel = None
    template_file = None
    placeholders = {}

    i = 1
    while i < len(sys.argv):
        if sys.argv[i] == '--channel':
            channel = sys.argv[i + 1]
            i += 2
        elif sys.argv[i] == '--sample':
            template_file = sys.argv[i + 1]
            i += 2
        elif sys.argv[i].startswith('+'):
            placeholder = sys.argv[i][1:]
            value = sys.argv[i + 1]
            placeholders[placeholder] = value
            i += 2
        else:
            print(f"Unknown argument: {sys.argv[i]}")
            sys.exit(1)

    if not channel or not template_file:
        print("Channel and template file are required.")
        sys.exit(1)

    config = configparser.ConfigParser()
    config.read('config.ini')

    if 'secure' not in config:
        print("Section [secure] not found in config.ini")
        sys.exit(1)

    if 'token' not in config['secure']:
        print("Token not found in [secure] section of config.ini")
        sys.exit(1)

    token = config['secure']['token']
    channel_id = config['channels'][channel]

    print(f"Token: {token}")
    print(f"Channel ID: {channel_id}")

    template_path = os.path.join('samples', template_file)
    if not os.path.exists(template_path):
        print(f"Template file not found: {template_path}")
        sys.exit(1)

    template = read_template(template_path)
    message = replace_placeholders(template, placeholders)

    print(f"Message: {message}")

    asyncio.run(send_message(token, channel_id, message))

if __name__ == '__main__':
    main()
