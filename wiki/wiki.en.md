# OFlake Poster

OFlake Poster is a tool for automating posting in Telegram. It allows you to send messages to Telegram channels based on templates using placeholders.

## Installation

### Installation

1. Ensure you have Python 3.6 or higher installed.
2. Install the necessary dependencies:

   ```bash
   pip install python-telegram-bot
   ```

3. Download the OFlake Poster repository and unzip it. Or clone it:

   ```bash
   git clone https://github.com/SerbOFlake/OFlake-Poster.git
   ```

## Configuration

### OOBE (Out-Of-Box Experience)

For the lazy, an OOBE tool has been assembled. Run it using:

```bash
python oobe.py
```

First, you will be prompted to enter the bot token:

![image](https://github.com/user-attachments/assets/3ffb6c05-c2c9-4a9d-aa2d-25311a87d16e)

Next, you need to enter the channel name:

> [!WARNING]
> Not the ID (will be prompted later)
> Here, enter the channel name to add to the configuration, i.e., simple names without spaces are preferable.

![image](https://github.com/user-attachments/assets/0dac05e5-28f0-42a6-b54f-893e19227178)

Now, you need to get the channel ID. You can use:

1. Modded Telegram clients on Android (e.g., AyuGram initially displays the channel IDs).
2. Using the web version:
   - The web version URL contains the channel ID. Go to the channel and find this value (It is different for everyone).
   - ![Untitled](https://github.com/user-attachments/assets/af928d72-c6ad-4c82-8d76-9430413661c0)
   - The value should be negative for input.

Then enter the value here:

![image](https://github.com/user-attachments/assets/86e8a690-a76e-4a28-9398-10a093ae9ae6)

Done! You will see this again:

![image](https://github.com/user-attachments/assets/0cf44f38-3c69-49d9-919b-8ed4cdee01fa)

If you need to add more channels, enter them. If not, leave the line empty and press Enter:

![image](https://github.com/user-attachments/assets/510fb08f-70c1-424c-bef0-e6eda0f4a541)

> [!TIP]
> OOBE is completed, well done!

### Manual Configuration

Create a `config.ini` file in the application's root folder and insert the following content:

```ini
[secure]
token = Here you tokenff
oobe = false

[channels]
test = -1002271321808
```

- `token` — replace with your bot token.
- `oobe` — set to `true` if you want to run OOBE again.
- In `[channels]`, add your channels.

## Creating Templates (sample)

Go to the `samples` folder and create a file `test.txt`. Add the following content:

```
Example
Dynamic text: {$dyntext}

👻 By : https://github.com/SerbOFlake/OFlake-Poster
```

Everything in `{$}` is a placeholder (also known as a filler). Save the file.

## Using the Poster

### Automation

Imagine a situation: you are a very sociable person and want a message in your group of like-minded people every time you use the `make` command.

Create a `makefile`:

```makefile
# Variables
CHANNEL = test
PLACEHOLDER = "I compiled something"
TEMPLATE = test.txt

# Target for sending a message
post:
	@echo "Sending a message to channel $(CHANNEL)..."
	@python cli.poster.py --channel $(CHANNEL) --sample $(TEMPLATE) \
		+dyntext "$(PLACEHOLDER)" \
	@echo "Message sent!"

# Target for cleaning (if necessary)
clean:
	@echo "Cleaning..."

# Default target
.PHONY: post clean
```

Now, when you run `make post`, a message will be sent to your channel about something being compiled.

### Manual Input

Run the poster:

```bash
python poster.py
```

You will see:

![image](https://github.com/user-attachments/assets/07f34d76-f04f-4a50-acf2-b69e05277a0a)

Here, enter your channel name (Name, not ID):

> [!NOTE]
> The name we set in the configuration.

Now, we need to specify the template (sample):

![image](https://github.com/user-attachments/assets/9435c72e-4ad0-41a0-b9a4-a6a6c46dc58b)

In our case, `test.txt`.

You will see the following lines:

![image](https://github.com/user-attachments/assets/748f7a15-f656-4752-a6fa-d91294d73a76)

Up to `🪵 Available placeholders: dyntext` is the template content for understanding where everything is. In `🪵 Available placeholders: dyntext`, you will see the placeholders available.

In:

```
🪵 Enter placeholder: dyntext
🪵 Enter content:
```

You will be prompted to enter content for each placeholder. For line breaks, use `\n`.

Enter something like:

![image](https://github.com/user-attachments/assets/1fd1864f-329b-4ea7-acb1-422b6e92f78e)

The console output will be:

![sss](https://github.com/user-attachments/assets/81f2ccfe-ecf5-4d9e-8255-4e7199fafcb6)

And in the channel, it will be:

![image](https://github.com/user-attachments/assets/3a64cfb4-6235-400d-8986-c539b6477f15)

## Conclusion

OFlake Poster is a powerful tool for automating posting in Telegram. With it, you can easily send messages to channels using templates and placeholders. If you have any questions or suggestions, feel free to contact the developer.
