from matplotlib import pyplot as plt

from Funtionality.Config import get_config, GRAY_COLOR

# Side Menu stylesheet reset
top_side_menu = "background: #164863;border-top-left-radius: 25px;border-top-right-radius: 25px;"
btm_side_menu = "background: #164863;border-bottom-left-radius: 25px;border-bottom-right-radius: 25px;"
choice_side_menu = "background: #164863;"

top_side_menu_dark = "background: #7346ad;border-top-left-radius: 25px;border-top-right-radius: 25px;"
btm_side_menu_dark = "background: #7346ad;border-bottom-left-radius: 25px;border-bottom-right-radius: 25px;"
choice_side_menu_dark = "background: #7346ad;"


def get_theme():
    values = get_config()
    index = values['theme']
    if index == "0":
        plt.rcParams['text.color'] = 'white'
        plt.rcParams['axes.labelcolor'] = 'white'
        return False
    else:
        plt.rcParams['text.color'] = GRAY_COLOR
        plt.rcParams['axes.labelcolor'] = GRAY_COLOR
        return True