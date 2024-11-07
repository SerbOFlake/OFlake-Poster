# oobe.py
import configparser

def oobe():
    config = configparser.ConfigParser()
    config.read('config.ini')

    if 'secure' not in config or 'token' not in config['secure'] or 'oobe' not in config['secure'] or config['secure']['oobe'] == 'true':
        print("OFlake Poster")
        print("Maded by Serb O Flake\n")

        token = input("🛡️ Enter your Telegram bot token: ")
        config['secure'] = {
            'token': token,
            'oobe': 'false'
        }

        channels = {}
        while True:
            channel_name = input("📧 Enter a channel (Not ID, or leave empty to finish): ")
            if not channel_name:
                break
            channel_id = input(f"🛡️ Enter ID for channel '{channel_name}': ")
            channels[channel_name] = channel_id

        config['channels'] = channels

        with open('config.ini', 'w', encoding='utf-8') as configfile:
            config.write(configfile)

        print("\nOOBE completed. You can now use the poster.")
        print("To add more channels, please refer to the wiki: https://github.com/SerbOFlake/OFlakePoster/wiki.en.md")

if __name__ == '__main__':
    oobe()