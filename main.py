def main():
    print("Grabbing all required packages...")
    import subprocess
    import sys
    try:
        from json import dumps
    except:
        print("Your PC does not have json installed, which should be a standard python library. Attempting to fix...")
        subprocess.check_call([sys.executable, '-m', 'pip', 'install', 'json', '--quiet'])
        from json import dumps
        print("Isssue fixed!")
    try:
        from colorama import Fore
    except:
        print("Your PC does not have colorama installed, which should be a standard python library. Attempting to fix...")
        subprocess.check_call([sys.executable, '-m', 'pip', 'install', 'colorama', '--quiet'])
        from colorama import Fore
        print("Isssue fixed!")
    try:
        import random
    except:
        print("Your PC does not have random installed, which should be a standard python library. Attempting to fix...")
        subprocess.check_call([sys.executable, '-m', 'pip', 'install', 'random', '--quiet'])
        import random
        print("Isssue fixed!")
    try:
        from httplib2 import Http
    except:
        print("Your PC does not have httplib2 installed, getting now...")
        subprocess.check_call([sys.executable, '-m', 'pip', 'install', 'httplib2', '--quiet'])
        from httplib2 import Http
        print("Installed successfully!")
    try:
        from discord_webhook import DiscordWebhook
    except:
        print("Your PC does not have discord-webhook installed, getting now...")
        subprocess.check_call([sys.executable, '-m', 'pip', 'install', 'discord-webhook', '--quiet'])
        from discord_webhook import DiscordWebhook
        print("Installed successfully!")
    randint = random.randint(1,3)
    if randint == 1:
        print(Fore.GREEN + """     /$$      /$$ /$$   /$$ /$$    /$$$$$$$$ /$$$$$$ /$$   /$$  /$$$$$$   /$$$$$$  /$$   /$$
    | $$$    /$$$| $$  | $$| $$   |__  $$__/|_  $$_/| $$  | $$ /$$__  $$ /$$__  $$| $$  /$$/
    | $$$$  /$$$$| $$  | $$| $$      | $$     | $$  | $$  | $$| $$  \ $$| $$  \ $$| $$ /$$/ 
    | $$ $$/$$ $$| $$  | $$| $$      | $$     | $$  | $$$$$$$$| $$  | $$| $$  | $$| $$$$$/  
    | $$  $$$| $$| $$  | $$| $$      | $$     | $$  | $$__  $$| $$  | $$| $$  | $$| $$  $$  
    | $$\  $ | $$| $$  | $$| $$      | $$     | $$  | $$  | $$| $$  | $$| $$  | $$| $$\  $$ 
    | $$ \/  | $$|  $$$$$$/| $$$$$$$$| $$    /$$$$$$| $$  | $$|  $$$$$$/|  $$$$$$/| $$ \  $$
    |__/     |__/ \______/ |________/|__/   |______/|__/  |__/ \______/  \______/ |__/  \__/\n""")
    elif randint == 2:
        print(Fore.CYAN + """    .___  ___.  __    __   __      .___________. __   __    __    ______     ______    __  ___ 
    |   \/   | |  |  |  | |  |     |           ||  | |  |  |  |  /  __  \   /  __  \  |  |/  / 
    |  \  /  | |  |  |  | |  |     `---|  |----`|  | |  |__|  | |  |  |  | |  |  |  | |  '  /  
    |  |\/|  | |  |  |  | |  |         |  |     |  | |   __   | |  |  |  | |  |  |  | |    <   
    |  |  |  | |  `--'  | |  `----.    |  |     |  | |  |  |  | |  `--'  | |  `--'  | |  .  \  
    |__|  |__|  \______/  |_______|    |__|     |__| |__|  |__|  \______/   \______/  |__|\__\ \n""")
    elif randint == 3:
        print(Fore.YELLOW + """             :::   :::   :::    ::: :::    ::::::::::: ::::::::::: :::    :::  ::::::::   ::::::::  :::    ::: 
          :+:+: :+:+:  :+:    :+: :+:        :+:         :+:     :+:    :+: :+:    :+: :+:    :+: :+:   :+:   
        +:+ +:+:+ +:+ +:+    +:+ +:+        +:+         +:+     +:+    +:+ +:+    +:+ +:+    +:+ +:+  +:+     
       +#+  +:+  +#+ +#+    +:+ +#+        +#+         +#+     +#++:++#++ +#+    +:+ +#+    +:+ +#++:++       
      +#+       +#+ +#+    +#+ +#+        +#+         +#+     +#+    +#+ +#+    +#+ +#+    +#+ +#+  +#+       
     #+#       #+# #+#    #+# #+#        #+#         #+#     #+#    #+# #+#    #+# #+#    #+# #+#   #+#       
    ###       ###  ########  ########## ###     ########### ###    ###  ########   ########  ###    ###\n""")
    else:
        print("There was an error while choosing the logo.")
    if randint == 1:
        print(Fore.GREEN + "1.Bomb Webhook  2.Send A Message  3.Send An Image (Discord)")
    elif randint == 2:
        print(Fore.CYAN + "1.Bomb Webhook  2.Send A Message  3.Send An Image (Discord)")
    elif randint == 3:
        print(Fore.YELLOW + "1.Bomb Webhook  2.Send A Message  3.Send An Image (Discord)")
    else:
        print("1.Bomb Webhook  2.Send A Message  3.Send An Image (Discord)")
    choice = int(input())
    if choice == 1:
        if randint == 1:
            print(Fore.GREEN + "Enter a webhook URL")
        elif randint == 2:
            print(Fore.CYAN + "Enter a webhook URL")
        elif randint == 3:
            print(Fore.YELLOW + "Enter a webhook URL")
        else:
            print("Enter a webhook URL")
        hook = input()
        if "google" in hook:
            type = "g"
            if randint == 1:
                print(Fore.GREEN + "Switching webhook type to google chat")
            elif randint == 2:
                print(Fore.CYAN + "Switching webhook type to google chat")
            elif randint == 3:
                print(Fore.YELLOW + "Switching webhook type to google chat")
            else:
                print("Switching webhook type to google chat")
        elif "discord" in hook:
            type = "d"
            if randint == 1:
                print(Fore.GREEN + "Switching webhook type to discord")
            elif randint == 2:
                print(Fore.CYAN + "Switching webhook type to discord")
            elif randint == 3:
                print(Fore.YELLOW + "Switching webhook type to discord")
            else:
                print("Switching webhook type to discord")
        else:
            print(Fore.RED + "Unknown webhook type. Try using a google chat or discord integration link.")
        if randint == 1:
            print(Fore.GREEN + "Enter a message to fire")
        elif randint == 2:
            print(Fore.CYAN + "Enter a message to fire")
        elif randint == 3:
            print(Fore.YELLOW + "Enter a message to fire")
        else:
            print("Enter a message to fire")
        msg = input()
        if randint == 1:
            print(Fore.GREEN + "Enter a delay between firing each message (seconds)")
        elif randint == 2:
            print(Fore.CYAN + "Enter a delay between firing each message (seconds)")
        elif randint == 3:
            print(Fore.YELLOW + "Enter a delay between firing each message (seconds)")
        else:
            print("Enter a delay between firing each message (seconds)")
        delay = float(input())
        import time
        if randint == 1:
            print(Fore.GREEN + "Are you sure you want to continue? Press enter to start bombing.")
        elif randint == 2:
            print(Fore.CYAN + "Are you sure you want to continue? Press enter to start bombing.")
        elif randint == 3:
            print(Fore.YELLOW + "Are you sure you want to continue? Press enter to start bombing.")
        else:
            print("Are you sure you want to continue? Press enter to start bombing.")
        input()
        while True:
            if type == "g":
                bot_message = {
                    'text': (msg)}
                message_headers = {'Content-Type': 'application/json; charset=UTF-8'}
                http_obj = Http()
                response = http_obj.request(
                    uri=hook,
                    method='POST',
                    headers=message_headers,
                    body=dumps(bot_message),
                )
                print(response)
            elif type == "d":
                webhook = DiscordWebhook(url=hook, content=msg)
                response = webhook.execute()
                print(response)
            else:
                print("Unknown webhook type. Try using a google chat or discord integration link.")
            time.sleep(delay)

    elif choice == 2:
        if randint == 1:
            print(Fore.GREEN + "Enter a webhook URL")
        elif randint == 2:
            print(Fore.CYAN + "Enter a webhook URL")
        elif randint == 3:
            print(Fore.YELLOW + "Enter a webhook URL")
        else:
            print("Enter a webhook URL")
        hook = input()
        if "google" in hook:
            type = "g"
            if randint == 1:
                print(Fore.GREEN + "Switching webhook type to google chat")
            elif randint == 2:
                print(Fore.CYAN + "Switching webhook type to google chat")
            elif randint == 3:
                print(Fore.YELLOW + "Switching webhook type to google chat")
            else:
                print("Switching webhook type to google chat")
        elif "discord" in hook:
            type = "d"
            if randint == 1:
                print(Fore.GREEN + "Switching webhook type to discord")
            elif randint == 2:
                print(Fore.CYAN + "Switching webhook type to discord")
            elif randint == 3:
                print(Fore.YELLOW + "Switching webhook type to discord")
            else:
                print("Switching webhook type to discord")
        else:
            print(Fore.RED + "Unknown webhook type. Try using a google chat or discord integration link.")
        if randint == 1:
            print(Fore.GREEN + "Enter a message to fire")
        elif randint == 2:
            print(Fore.CYAN + "Enter a message to fire")
        elif randint == 3:
            print(Fore.YELLOW + "Enter a message to fire")
        else:
            print("Enter a message to fire")
        msg = input()
        if type == "g":
            bot_message = {
                'text': (msg)}
            message_headers = {'Content-Type': 'application/json; charset=UTF-8'}
            http_obj = Http()
            response = http_obj.request(
                uri=hook,
                method='POST',
                headers=message_headers,
                body=dumps(bot_message),
            )
            print(response)
        elif type == "d":
            webhook = DiscordWebhook(url=hook, content=msg)
            response = webhook.execute()
            print(response)
        else:
            print("Unknown webhook type. Try using a google chat or discord integration link.")
        main()
    elif choice == 3:
        if randint == 1:
            print(Fore.GREEN + "Enter a webhook URL")
        elif randint == 2:
            print(Fore.CYAN + "Enter a webhook URL")
        elif randint == 3:
            print(Fore.YELLOW + "Enter a webhook URL")
        else:
            print("Enter a webhook URL")
        hook = input()
        if "google" in hook:
            type = "g"
            if randint == 1:
                print(Fore.GREEN + "Sorry, but google chat webhooks do not support sending images. Restarting...")
                main()
            elif randint == 2:
                print(Fore.CYAN + "Sorry, but google chat webhooks do not support sending images. Restarting...")
                main()
            elif randint == 3:
                print(Fore.YELLOW + "Sorry, but google chat webhooks do not support sending images. Restarting...")
                main()
            else:
                print("Sorry, but google chat webhooks do not support sending images. Restarting...")
                main()
        elif "discord" in hook:
            type = "d"
            if randint == 1:
                print(Fore.GREEN + "Switching webhook type to discord")
            elif randint == 2:
                print(Fore.CYAN + "Switching webhook type to discord")
            elif randint == 3:
                print(Fore.YELLOW + "Switching webhook type to discord")
            else:
                print("Switching webhook type to discord")
        else:
            print(Fore.RED + "Unknown webhook type. Try using a discord integration link.")
        if randint == 1:
            print(Fore.GREEN + "Enter an image path to send")
        elif randint == 2:
            print(Fore.CYAN + "Enter an image path to send")
        elif randint == 3:
            print(Fore.YELLOW + "Enter an image path to send")
        else:
            print("Enter an image path to send")
        imgpath = input()
        webhook = DiscordWebhook(url=hook)
        with open(imgpath, "rb") as f:
            webhook.add_file(file=f.read(), filename='image.jpg')
        response = webhook.execute()
        print(response)
        main()
main()
quit("Thanks for using MultiHook!")