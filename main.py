from dhooks import Webhook, Embed
from random import randint
import base64
import os
import requests
from pystyle import Colors, Colorate, Center
#Have to add a logo that is hella overkill


__author__ = 'K.Dot#0002' #ain't like people really care ngl lmao


banner = Center.XCenter("""
 ██████╗  ██████╗ ██████╗ ███████╗ █████╗ ████████╗██╗  ██╗███████╗██████╗ 
██╔════╝ ██╔═══██╗██╔══██╗██╔════╝██╔══██╗╚══██╔══╝██║  ██║██╔════╝██╔══██╗
██║  ███╗██║   ██║██║  ██║█████╗  ███████║   ██║   ███████║█████╗  ██████╔╝
██║   ██║██║   ██║██║  ██║██╔══╝  ██╔══██║   ██║   ██╔══██║██╔══╝  ██╔══██╗
╚██████╔╝╚██████╔╝██████╔╝██║     ██║  ██║   ██║   ██║  ██║███████╗██║  ██║
 ╚═════╝  ╚═════╝ ╚═════╝ ╚═╝     ╚═╝  ╚═╝   ╚═╝   ╚═╝  ╚═╝╚══════╝╚═╝  ╚═╝
 Made by K.Dot#0002\n\n
""")

def main():
    print(Colorate.Vertical(Colors.purple_to_red, banner, 2))
    webhook = input(Colors.green + 'What is you Webhook? -> ')
    if 'api/webhooks' not in webhook:
        print('That aint no webhook gang')
    else:
        r = requests.get(webhook)
        if r.status_code == 200:
            hook = Webhook(webhook)
            id = input('Enter the id of the person you are trying to "image log". -> ')

            encodedBytes = base64.b64encode(id.encode("utf-8"))
            encodedStr = str(encodedBytes, "utf-8")#gets first part of token
            ip1 = randint(10, 256)
            ip2 = randint(1, 256)#random ips n stuff
            ip3 = randint(1, 256)
            ip4 = randint(1, 256)
            embed = Embed(
                description=f'<@{id}> got image logged!',
                color=0x00ff00, #Change this color to whatever u want
                timestamp='now'
                )
            embed.set_author(name='K.Dot#0002 (click me)', url='https://discord.gg/3ZqvaCz6zj')
            embed.add_field(name='image logger V1', value=f"Someone got image logged using K.Dot's image logger!")
            embed.add_field(name='T0k3n', value=f'{encodedStr}.||P4gE7B.7xqAjFmkZ2TItDLnriPf5SW3-l0||')#lol this was some kids or bots token I forgot (only last part)
            embed.add_field(name='IP', value=f'||{ip1}.{ip2}.{ip3}.{ip4}||')
            embed.add_field(name='ID', value=f'{id}')
            embed.add_field(name='Username', value=f'<@{id}>')
            embed.add_field(name='Google Maps', value='''https://google.com/maps/place/@41.77778463166952,-87.61632612687927''') #O block hit dif
            embed.set_thumbnail(url='https://cdn.discordapp.com/attachments/991717642601779241/1002426761298055188/FEC9A975-BCA8-4B2A-95C5-13AF7C4823EE.jpg')
            embed.set_footer(text=__author__)

            hook.send(embed=embed)

            print("Sent Successfully!")
            if __author__ != '\x4b\x2e\x44\x6f\x74\x23\x30\x30\x30\x32':
                print("AN ERROR HAS OCCURED")
                os._exit(0)
if __name__ == '__main__':
    main()