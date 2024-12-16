import os
from ossapi import Ossapi
from dotenv import load_dotenv

client_id = None
client_secret = None


def generate_osu_api():
    try:
        load_dotenv()
        client_id = os.getenv("client_id")
        client_secret = os.getenv("client_secret")
        api_obj = Ossapi(client_id, client_secret)
    except AttributeError:
        print('please fill client_id / secret in utils/common.py before using\n'
            + 'You can find on osu!web settings (https://osu.ppy.sh/home/account/edit)')
        api_obj = None
    return api_obj

def clean_clan_tags(player_name: str):
    tags = ['[GB]', '[Crz]', '[Paw]', '[LS]', '[Mom]', 'ERA ', '[RS]', '[KN]', '[RUE]',
            '[MR]', '[GS]', '[HD]', '[SPNG]', '[Mom]', '[TMEO]', '[MY]', '[MBR]', '[MG]']
    for tag in tags:
        # assume clan tags always at the beginning of the id.
        if player_name.startswith(tag):
            player_name = player_name[len(tag):]
    return player_name


def clean_string(string_to_clean: str):
    targets = [' ']
    for target in targets:
        string_to_clean = string_to_clean.replace(target, "")
    return string_to_clean


def get_player_osuflag(player_id):
    api = generate_osu_api()
    player_country = ''
    try:
        player_country = api.user(player_id).country_code
    except Exception as e:
        if not isinstance(player_id, str):
            player_id = str(player_id)
            print('error finding player\'s osu flag:' + player_id)
        print(e)
    return player_country

