import random
import string
import os
import requests
import time

characters = string.ascii_uppercase + string.digits

def generate_steam_code(length):
    return ''.join(random.choice(characters) for _ in range(length))

def generate_amazon_activation_codes(num_codes):
    code_length = 20
    codes = []
    for i in range(num_codes):
        code = ''.join(random.choice(characters) for _ in range(code_length))
        codes.append(f"https://www.amazon.com/activate/{code}")
    return codes

def generate_steam_activation_codes(num_codes):
    code_length = 15
    codes = []
    for i in range(num_codes):
        steam_code = generate_steam_code(code_length)
        codes.append(f"https://store.steampowered.com/account/registerkey?key={steam_code}")
    return codes

def generate_roblox_redemption_codes(num_codes):
    code_length = 10
    codes = []
    for i in range(num_codes):
        code = ''.join(random.choice(characters) for _ in range(code_length))
        codes.append(f"https://www.roblox.com/gamecard-redeem/{code}")
    return codes

def generate_google_play_redeem_codes(num_codes):
    code_length = 16
    codes = []
    for i in range(num_codes):
        code = ''.join(random.choice(characters) for _ in range(code_length))
        codes.append(f"https://play.google.com/store/redeem?code={code}")
    return codes

def generate_apple_activation_codes(num_codes):
    code_length = 16
    codes = []
    for i in range(num_codes):
        code = ''.join(random.choice(characters) for _ in range(code_length))
        codes.append(f"https://www.apple.com/activate/{code}")
    return codes

def send_codes_to_webhook(codes, webhook_url):
    if not webhook_url.startswith("https://discord.com/api/webhooks/"):
        print("Invalid webhook URL. Please ensure it starts with https://discord.com/api/webhooks/")
        return

    # Split the codes into chunks of 10 messages each
    chunks = [codes[i:i + 10] for i in range(0, len(codes), 10)]

    # Send each chunk as a separate message with a delay of 2 seconds between messages
    for chunk in chunks:
        data = {"content": "\n".join(chunk)}
        headers = {"Content-Type": "application/json"}
        response = requests.post(webhook_url, json=data, headers=headers)
        if response.status_code != 200:
            print("Error sending codes:", response.status_code)
        time.sleep(2)

def main():
    os.system('cls' if os.name == 'nt' else 'clear')  # Clear screen

    # ASCII art
    print(r'''

█████╗ ██╗     ███████╗██╗  ██╗██████╗  █████╗ ██████╗ ██████╗  ██████╗      ██████╗ ███████╗███╗   ██╗
██╔══██╗██║     ██╔════╝╚██╗██╔╝██╔══██╗██╔══██╗██╔══██╗██╔══██╗██╔═══██╗    ██╔════╝ ██╔════╝████╗  ██║
███████║██║     █████╗   ╚███╔╝ ██║  ██║███████║██████╔╝██████╔╝██║   ██║    ██║  ███╗█████╗  ██╔██╗ ██║
██╔══██║██║     ██╔══╝   ██╔██╗ ██║  ██║██╔══██║██╔═══╝ ██╔══██╗██║   ██║    ██║   ██║██╔══╝  ██║╚██╗██║
██║  ██║███████╗███████╗██╔╝ ██╗██████╔╝██║  ██║██║     ██║  ██║╚██████╔╝    ╚██████╔╝███████╗██║ ╚████║
╚═╝  ╚═╝╚══════╝╚══════╝╚═╝  ╚═╝╚═════╝ ╚═╝  ╚═╝╚═╝     ╚═╝  ╚═╝ ╚═════╝      ╚═════╝ ╚══════╝╚═╝  ╚═══╝

''')

    print("Made by Alex")

    # Get username and password
    while True:
        username = input("Enter your username: ")
        if username != "GeneratorTool":
            print("Invalid username")
        else:
            break

    while True:
        password = input("Enter your password: ")
        if password != "AlexGen354":
            print("Invalid password")
        else:
            break

    # Get webhook URL
    while True:
        webhook_url = input("Enter the webhook URL: ")
        if not webhook_url.startswith("https://discord.com/api/webhooks/"):
            print("Invalid webhook URL. Please ensure it starts with https://discord.com/api/webhooks/")
        else:
            break

    # Display menu options
    print("-" * 50)
    print("╔═════════════════════════════════════════════════════════════╗")
    print("║ ★ ★ ★ CODE GENERATOR ★ ★ ★ ║")
    print("╠═════════════════════════════════════════════════════════════╣")
    print("║ ╚ 1. 🔑 Amazon Activation Codes ╚═╝")
    print("║ ╚ 2. 🎮 Steam Activation Codes ╚═╝")
    print("║ ╚ 3. 🕹️ Roblox Redemption Codes ╚═╝")
    print("║ ╚ 4. 📱 Google Play Redeem Codes ╚═╝")
    print("║ ╚ 5. 🍏 Apple Activation Codes ╚═╝")
    print("║ ╚ 6,EXIT                        ╚═╝")
    print("╠═════════════════════════════════════════════════════════════╣")
    print("║ 🚀 Select an option and press Enter! ║")
    print("╚═════════════════════════════════════════════════════════════╝")

    while True:
        choice = input("Enter your choice (1-6): ")

        if choice == "1":
            num_codes = int(input("Enter the number of codes to generate: "))
            codes = generate_amazon_activation_codes(num_codes)
            send_codes_to_webhook(codes, webhook_url)
            print("CODES SUCCESSFULLY SENT!")
        elif choice == "2":
            num_codes = int(input("Enter the number of codes to generate: "))
            codes = generate_steam_activation_codes(num_codes)
            send_codes_to_webhook(codes, webhook_url)
            print("CODES SUCCESSFULLY SENT!")
        elif choice == "3":
            num_codes = int(input("Enter the number of codes to generate: "))
            codes = generate_roblox_redemption_codes(num_codes)
            send_codes_to_webhook(codes, webhook_url)
            print("CODES SUCCESSFULLY SENT!")
        elif choice == "4":
            num_codes = int(input("Enter the number of codes to generate: "))
            codes = generate_google_play_redeem_codes(num_codes)
            send_codes_to_webhook(codes, webhook_url)
            print("CODES SUCCESSFULLY SENT!")
        elif choice == "5":
            num_codes = int(input("Enter the number of codes to generate: "))
            codes = generate_apple_activation_codes(num_codes)
            send_codes_to_webhook(codes, webhook_url)
            print("CODES SUCCESSFULLY SENT!")
        elif choice == "6":
            print("Goodbye!")
            break
        else:
            print("Invalid choice")

if __name__ == "__main__":
    main()