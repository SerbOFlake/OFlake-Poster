# poster.py
import os
import subprocess
from oobe import oobe

def read_template(template_path):
    with open(template_path, 'r', encoding='utf-8') as file:
        return file.read()

def replace_placeholders(template, placeholders):
    for key, value in placeholders.items():
        # Заменяем \n на фактические переносы строк
        value = value.replace('\\n', '\n')
        template = template.replace(f'{{${key}}}', value)
    return template

def main():
    oobe()

    while True:
        channel = input("📧 Enter channel name (or 'exit' to quit): ")
        if channel == 'exit':
            break

        template_file = input("🛡️ Select a sample: ")
        template_path = os.path.join('samples', template_file)
        if not os.path.exists(template_path):
            print(f"🛡️ Template file not found: {template_path}")
            continue

        template = read_template(template_path)
        print(f"\n🗂️ {template_file} | Content\n{template}\n")

        placeholders = {}
        for line in template.splitlines():
            if '{$' in line:
                placeholder = line.split('{$')[1].split('}')[0]
                placeholders[placeholder] = None

        print(f"🪵 Available placeholders: {', '.join(placeholders.keys())}\n")

        for placeholder in placeholders:
            value = input(f"🪵 Enter placeholder: {placeholder}\n🪵 Enter content: ")
            placeholders[placeholder] = value

        message = replace_placeholders(template, placeholders)
        print(f"\nMessage:\n{message}\n")

        args = [
            'python', 'cli.poster.py',
            '--channel', channel,
            '--sample', template_file,
        ]

        for placeholder, value in placeholders.items():
            # Заменяем \n на фактические переносы строк перед передачей в cli.poster.py
            value = value.replace('\\n', '\n')
            args.append(f'+{placeholder}')
            args.append(value)

        subprocess.run(args)
        print("📤 Message sent successfully!\n")

if __name__ == '__main__':
    main()