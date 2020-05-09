import os
import re
import socket
import subprocess
from libqtile.config import Drag, Key, Screen, Group, Drag, Click, Rule
from libqtile.command import lazy
from libqtile import layout, bar, widget, hook
from libqtile.widget import Spacer
import arcobattery

from libqtile.log_utils import logger
from powerline.bindings.qtile.widget import PowerlineTextBox

#mod4 or mod = super key
mod = "mod4"
mod1 = "alt"
mod2 = "control"
home = os.path.expanduser('~')

# Settings - Global
global_opacity= .75

# Settings - Bar
bar_opacity = global_opacity
bar_size = 40

# Settings - Dmenu
dmen_settings = {
	'o' : global_opacity,
        'dim' : 0.15,
        'h' : 60,
        'l' : 30,
        'w' : 960,
        'x' : 480,
        'nb' : '#191919',
	'nf' : '#fea63c',
	'sb' : '#fea63c',
	'sf' : '#191919',
	'fn' : 'NotoMonoRegular:bold:pixelsize=44'
                }

s = ' '
dmen_opt = ['-{} "{}"'.format(k,v) for k,v in dmen_settings.items()]
dmen_cmd = "dmenu_run -i " + s.join(dmen_opt)
dmen_opt2 = ['-{} "{}"'.format(k,v)
	for k,v in dmen_settings.items() if k != 'l']
dmen_cmd2 = "dmenu_run -i " + s.join(dmen_opt2)

# Variables - Layout
gap = 20
border_width = 5

# COLORS
def init_colors():
    return [["#2F343F", "#2F343F"], # color 0
            ["#2F343F", "#2F343F"], # color 1
            ["#c0c5ce", "#c0c5ce"], # color 2
            ["#fba922", "#fba922"], # color 3
            ["#3384d0", "#3384d0"], # color 4
            ["#f3f4f5", "#f3f4f5"], # color 5
            ["#cd1f3f", "#cd1f3f"], # color 6
            ["#62FF00", "#62FF00"], # color 7
            ["#6790eb", "#6790eb"], # color 8
            ["#a9a9a9", "#a9a9a9"]] # color 9

colors = init_colors()
@lazy.function
def window_to_prev_group(qtile):
    if qtile.currentWindow is not None:
        i = qtile.groups.index(qtile.currentGroup)
        qtile.currentWindow.togroup(qtile.groups[i - 1].name)

@lazy.function
def window_to_next_group(qtile):
    if qtile.currentWindow is not None:
        i = qtile.groups.index(qtile.currentGroup)
        qtile.currentWindow.togroup(qtile.groups[i + 1].name)

keys = [

# Personal Keys

    # Function Keys
    Key([], "F12", lazy.spawn('xfce4-terminal --drop-down')),

    # Super Keys
    Key([mod], "f", lazy.spawn('thunar')),
    Key([mod], "Up", lazy.window.toggle_fullscreen()),
    Key([mod], "m", lazy.spawn('mailspring')),
    Key([mod], "p", lazy.spawn('pithos')),
    Key([mod], "q", lazy.window.kill()),
    Key([mod], "t", lazy.spawn('telegram-desktop')),
    Key([mod], "w", lazy.spawn('firefox')),
    Key([mod], "x", lazy.spawn('arcolinux-logout')),
    Key([mod], "Return", lazy.spawn('termite')),
    Key([mod], "KP_Enter", lazy.spawn('termite')),
    Key([mod], "r", lazy.restart()),

    Key([mod], "c", lazy.spawn('conky-toggle')),
    Key([mod], "v", lazy.spawn('pavucontrol')),
    Key([mod], "Escape", lazy.spawn('xkill')),
    Key([mod], "F5", lazy.spawn('meld')),
    Key([mod], "F6", lazy.spawn('vlc --video-on-top')),
    Key([mod], "F7", lazy.spawn('virtualbox')),
    Key([mod], "F10", lazy.spawn("spotify")),
    Key([mod], "F11", lazy.spawn('rofi -show run -fullscreen')),
    Key([mod], "F12", lazy.spawn('rofi -show run')),

    # SUPER + SHIFT KEYS
    Key([mod, "shift"], "d",
        lazy.spawn("dmenu_run -i -nb '#191919' -nf '#fea63c' -sb '#fea63c' -sf '#191919' -fn 'NotoMonoRegular:bold:pixelsize=14'")),
    Key([mod, "shift"], "r", lazy.restart()),
    Key([mod, "control"], "r", lazy.restart()),
    # Key([mod, "shift"], "x", lazy.shutdown()),

    # CONTROL + ALT KEYS
    Key(["mod1", "control"], "Return", lazy.spawn('conky-rotate -n')),
    Key(["mod1", "control"], "Prior", lazy.spawn('conky-rotate -p')),
    Key(["mod1", "control"], "a", lazy.spawn('xfce4-appfinder')),
    Key(["mod1", "control"], "c", lazy.spawn('catfish')),
    Key(["mod1", "control"], "e", lazy.spawn('arcolinux-tweak-tool')),
    Key(["mod1", "control"], "g", lazy.spawn('chromium -no-default-browser-check')),
    Key(["mod1", "control"], "i", lazy.spawn('nitrogen')),
    Key(["mod1", "control"], "k", lazy.spawn('arcolinux-logout')),
    Key(["mod1", "control"], "l", lazy.spawn('arcolinux-logout')),
    Key(["mod1", "control"], "m", lazy.spawn('xfce4-settings-manager')),
    Key(["mod1", "control"], "o", lazy.spawn(home + '/.config/qtile/scripts/picom-toggle.sh')),
    Key(["mod1", "control"], "b", lazy.spawn('thunar')),
    Key(["mod1", "control"], "p", lazy.spawn('pamac-manager')),
    Key(["mod1", "control"], "r", lazy.spawn('rofi-theme-selector')),
    Key(["mod1", "control"], "u", lazy.spawn('pavucontrol')),
    Key(["mod1", "control"], "v", lazy.spawn('vivaldi-stable')),
    Key(["mod1", "control"], "w", lazy.spawn('arcolinux-welcome-app')),

    # ALT + ... KEYS
    Key(["mod1"], "f", lazy.spawn('variety -f')),
    Key(["mod1"], "h", lazy.spawn('urxvt -e htop')),
    Key(["mod1"], "n", lazy.spawn('variety -n')),
    Key(["mod1"], "p", lazy.spawn('variety -p')),
    Key(["mod1"], "t", lazy.spawn('variety -t')),
    Key(["mod1"], "Up", lazy.spawn('variety --pause')),
    Key(["mod1"], "Down", lazy.spawn('variety --resume')),
    Key(["mod1"], "Left", lazy.spawn('variety -p')),
    Key(["mod1"], "Right", lazy.spawn('variety -n')),
    Key(["mod1"], "F2", lazy.spawn('gmrun')),
    Key(["mod1"], "F3", lazy.spawn('xfce4-appfinder')),

    # VARIETY KEYS WITH PYWAL
    Key(["mod1", "shift"],
        "f", lazy.spawn(home + '/.config/qtile/scripts/set-pywal.sh -f')),
    Key(["mod1", "shift"], "p",
        lazy.spawn(home + '/.config/qtile/scripts/set-pywal.sh -p')),
    Key(["mod1", "shift"], "n",
        lazy.spawn(home + '/.config/qtile/scripts/set-pywal.sh -n')),
    Key(["mod1", "shift"], "u",
        lazy.spawn(home + '/.config/qtile/scripts/set-pywal.sh -u')),

    # CONTROL + SHIFT KEYS
    Key([mod2, "shift"], "Escape", lazy.spawn('xfce4-taskmanager')),

    # SCREENSHOTS
    Key([], "Print",
        lazy.spawn("scrot 'ArcoLinux-%Y-%m-%d-%s_screenshot_$wx$h.jpg' -e 'mv $f $$(xdg-user-dir PICTURES)'")),
    Key([mod2], "Print",
        lazy.spawn('xfce4-screenshooter')),
    Key([mod2, "shift"], "Print",
        lazy.spawn('gnome-screenshot -i')),

# MULTIMEDIA KEYS

# INCREASE/DECREASE BRIGHTNESS
    Key([], "XF86MonBrightnessUp", lazy.spawn("xbacklight -inc 5")),
    Key([], "XF86MonBrightnessDown", lazy.spawn("xbacklight -dec 5")),

# INCREASE/DECREASE/MUTE VOLUME
    Key([], "XF86AudioMute",
        lazy.spawn("amixer -q set Master toggle")),
    Key([], "XF86AudioLowerVolume",
        lazy.spawn("amixer -q set Master 5%-")),
    Key([], "XF86AudioRaiseVolume",
        lazy.spawn("amixer -q set Master 5%+")),

    Key([], "XF86AudioPlay", lazy.spawn("playerctl play-pause")),
    Key([], "XF86AudioNext", lazy.spawn("playerctl next")),
    Key([], "XF86AudioPrev", lazy.spawn("playerctl previous")),
    Key([], "XF86AudioStop", lazy.spawn("playerctl stop")),

#    Key([], "XF86AudioPlay", lazy.spawn("mpc toggle")),
#    Key([], "XF86AudioNext", lazy.spawn("mpc next")),
#    Key([], "XF86AudioPrev", lazy.spawn("mpc prev")),
#    Key([], "XF86AudioStop", lazy.spawn("mpc stop")),

# QTILE LAYOUT KEYS
    Key([mod], "n", lazy.layout.normalize()),
    Key([mod], "space", lazy.next_layout()),

# CHANGE FOCUS
#    Key([mod], "Up", lazy.layout.up()),
#    Key([mod], "Down", lazy.layout.down()),
#    Key([mod], "Left", lazy.layout.left()),
#    Key([mod], "Right", lazy.layout.right()),
    Key([mod], "k", lazy.layout.up()),
    Key([mod], "j", lazy.layout.down()),
    Key([mod], "h", lazy.layout.left()),
    Key([mod], "l", lazy.layout.right()),


# RESIZE UP, DOWN, LEFT, RIGHT
    Key([mod, "control"], "l",
        lazy.layout.grow_right(),
        lazy.layout.grow(),
        lazy.layout.increase_ratio(),
        lazy.layout.delete(),
        ),
    Key([mod, "control"], "Right",
        lazy.layout.grow_right(),
        lazy.layout.grow(),
        lazy.layout.increase_ratio(),
        lazy.layout.delete(),
        ),
    Key([mod, "control"], "h",
        lazy.layout.grow_left(),
        lazy.layout.shrink(),
        lazy.layout.decrease_ratio(),
        lazy.layout.add(),
        ),
    Key([mod, "control"], "Left",
        lazy.layout.grow_left(),
        lazy.layout.shrink(),
        lazy.layout.decrease_ratio(),
        lazy.layout.add(),
        ),
    Key([mod, "control"], "k",
        lazy.layout.grow_up(),
        lazy.layout.grow(),
        lazy.layout.decrease_nmaster(),
        ),
    Key([mod, "control"], "Up",
        lazy.layout.grow_up(),
        lazy.layout.grow(),
        lazy.layout.decrease_nmaster(),
        ),
    Key([mod, "control"], "j",
        lazy.layout.grow_down(),
        lazy.layout.shrink(),
        lazy.layout.increase_nmaster(),
        ),
    Key([mod, "control"], "Down",
            lazy.layout.grow_down(),
            lazy.layout.shrink(),
            lazy.layout.increase_nmaster(),
            ),


# FLIP LAYOUT FOR MONADTALL/MONADWIDE
    Key([mod, "shift"], "f", lazy.layout.flip()),

# FLIP LAYOUT FOR BSP
    Key([mod, "mod1"], "k", lazy.layout.flip_up()),
    Key([mod, "mod1"], "j", lazy.layout.flip_down()),
    Key([mod, "mod1"], "l", lazy.layout.flip_right()),
    Key([mod, "mod1"], "h", lazy.layout.flip_left()),

# MOVE WINDOWS UP OR DOWN BSP LAYOUT
    Key([mod, "shift"], "k", lazy.layout.shuffle_up()),
    Key([mod, "shift"], "j", lazy.layout.shuffle_down()),
    Key([mod, "shift"], "h", lazy.layout.shuffle_left()),
    Key([mod, "shift"], "l", lazy.layout.shuffle_right()),

# MOVE WINDOWS UP OR DOWN MONADTALL/MONADWIDE LAYOUT
    Key([mod, "shift"], "Up", lazy.layout.shuffle_up()),
    Key([mod, "shift"], "Down", lazy.layout.shuffle_down()),
    Key([mod, "shift"], "Left", lazy.layout.swap_left()),
    Key([mod, "shift"], "Right", lazy.layout.swap_right()),

# TOGGLE FLOATING LAYOUT
    Key([mod, "shift"], "space", lazy.window.toggle_floating()),
    ]

groups = []

# FOR QWERTY KEYBOARDS
#group_names = ["1", "2", "3", "4", "5", "6", "7", "8", "9", "0",]
#group_labels = ["", "", "", "", "", "", "", "", "", "",]
#group_labels = ["Web", "Edit/chat", "Image", "Gimp", "Meld", "Video", "Vb", "Files", "Mail", "Music",]
#group_layouts = ["monadtall", "matrix", "monadtall", "bsp", "monadtall", "matrix", "monadtall", "bsp", "monadtall", "monadtall",]

group_names = ['1', '2', '3', '4', '5', '6']
group_labels = ["" ,"", "", "", "", ""]

for i in range(len(group_names)):
    groups.append(
        Group(
            name=group_names[i],
            layout='monadtall',
            label=group_labels[i],
        ))

for i in groups:
    keys.extend([

        #CHANGE WORKSPACES
        Key([mod], i.name, lazy.group[i.name].toscreen()),
        Key([mod], "Tab", lazy.screen.next_group()),
        Key([mod, "shift"], "Tab", lazy.screen.prev_group()),
        Key(["mod1"], "Tab", lazy.screen.next_group()),
        Key(["mod1", "shift"], "Tab", lazy.screen.prev_group()),

        # MOVE WINDOW TO SELECTED WORKSPACE 1-10 AND STAY ON WORKSPACE
        #Key([mod, "shift"], i.name, lazy.window.togroup(i.name)),

        # MOVE WINDOW TO SELECTED WORKSPACE 1-10 AND FOLLOW MOVED WINDOW TO WORKSPACE
        Key([mod, "shift"], i.name, lazy.window.togroup(i.name) , lazy.group[i.name].toscreen()),
    ])

# Dmenu key bindings
keys.extend([
	Key([mod], "d", lazy.spawn(dmen_cmd)),
	Key([mod, "shift"], "d", lazy.spawn(dmen_cmd2))
	])

def init_layout_theme():
    return {"margin":gap,
            "border_width":border_width,
            "border_focus": "#5e81ac",
            "border_normal": "#4c566a"
            }

layout_theme = init_layout_theme()

layouts = [
    layout.MonadTall(**layout_theme),
    layout.MonadWide(**layout_theme),
    layout.Matrix(**layout_theme),
    layout.Bsp(**layout_theme),
    layout.Floating(**layout_theme),
    layout.RatioTile(**layout_theme),
    layout.Max(**layout_theme)
]


# WIDGETS FOR THE BAR
def init_widgets_defaults():
    return dict(font="Noto Sans",
                fontsize = 20,
                padding = 2,
                background=colors[1])

widget_defaults = init_widgets_defaults()

def init_widgets_list():
    prompt = "{0}@{1}: ".format(os.environ["USER"], socket.gethostname())
    widgets_list = [
               widget.GroupBox(font="FontAwesome",
                        fontsize = 28,
                        margin_y = 3,
                        margin_x = 0,
                        padding_y = 6,
                        padding_x = 5,
                        borderwidth = 0,
                        disable_drag = True,
                        active = colors[9],
                        inactive = colors[5],
                        rounded = False,
                        highlight_method = "text",
                        this_current_screen_border = colors[8],
                        foreground = colors[2],
                        background = colors[1]
                        ),
               widget.Sep(
                        linewidth = 1,
                        padding = 10,
                        foreground = colors[2],
                        background = colors[1]
                        ),
               widget.CurrentLayout(
                        font = "Noto Sans Bold",
                        foreground = colors[5],
                        background = colors[1]
                        ),
               widget.Sep(
                        linewidth = 1,
                        padding = 10,
                        foreground = colors[2],
                        background = colors[1]
                        ),
               widget.WindowName(font="Noto Sans",
                        fontsize = 14,
                        foreground = colors[5],
                        background = colors[1],
                        ),
               widget.Net(
                         font="Noto Sans",
                         fontsize=12,
                         interface="wlp2s0",
                         foreground=colors[2],
                         background=colors[1],
                         padding = 0,
                         ),
               widget.Sep(
                        linewidth = 1,
                        padding = 10,
                        foreground = colors[2],
                        background = colors[1]
                        ),
               # widget.Sep(
               #          linewidth = 1,
               #          padding = 10,
               #          foreground = colors[2],
               #          background = colors[1]
               #          ),
               # widget.NetGraph(
               #          font="Noto Sans",
               #          fontsize=12,
               #          bandwidth="down",
               #          interface="auto",
               #          fill_color = colors[8],
               #          foreground=colors[2],
               #          background=colors[1],
               #          graph_color = colors[8],
               #          border_color = colors[2],
               #          padding = 0,
               #          border_width = 1,
               #          line_width = 1,
               #          ),
               # widget.Sep(
               #          linewidth = 1,
               #          padding = 10,
               #          foreground = colors[2],
               #          background = colors[1]
               #          ),
               # # do not activate in Virtualbox - will break qtile
               # widget.ThermalSensor(
               #          foreground = colors[5],
               #          foreground_alert = colors[6],
               #          background = colors[1],
               #          metric = True,
               #          padding = 3,
               #          threshold = 80
               #          ),
               widget.TextBox(
                        font="FontAwesome",
                        text="  ",
                        foreground=colors[3],
                        background=colors[1],
                        padding = 0,
                        fontsize=16
                        ),
               widget.Clock(
                        foreground = colors[5],
                        background = colors[1],
                        fontsize = 20,
                        format="%I:%M%p %a,%B %m, %Y"
                        ),
               widget.Sep(
               linewidth = 1,
               padding = 10,
               foreground = colors[2],
               background = colors[1]
               ),
               # battery option 1  ArcoLinux Horizontal icons do not forget to import arcobattery at the top
               arcobattery.BatteryIcon(
               padding=0,
               scale=0.9,
               y_poss=2,
               theme_path=home + "/.config/qtile/icons/battery_icons_horiz",
               update_interval = 5,
               background = colors[1]
               ),
               # # battery option 2  from Qtile
               # widget.Sep(
               #          linewidth = 1,
               #          padding = 10,
               #          foreground = colors[2],
               #          background = colors[1]
               #          ),
               # widget.Battery(
               #          font="Noto Sans",
               #          update_interval = 10,
               #          fontsize = 12,
               #          foreground = colors[5],
               #          background = colors[1],
	           #          ),
#               widget.TextBox(
#                        font="FontAwesome",
#                        text="  ",
#                        foreground=colors[6],
#                        background=colors[1],
#                        padding = 0,
#                        fontsize=16
#                        ),
#               widget.CPUGraph(
#                        border_color = colors[2],
#                        fill_color = colors[8],
#                        graph_color = colors[8],
#                        background=colors[1],
#                        border_width = 1,
#                        line_width = 1,
#                        core = "all",
#                        type = "box"
#                        ),
               widget.Sep(
                        linewidth = 1,
                        padding = 10,
                        foreground = colors[2],
                        background = colors[1]
                        ),
               widget.TextBox(
                        font="FontAwesome",
                        text="  ",
                        foreground=colors[4],
                        background=colors[1],
                        padding = 0,
                        fontsize=16
                        ),
               widget.Memory(
                        font="Noto Sans",
                        format = '{MemUsed}M/{MemTotal}M',
                        update_interval = 1,
                        fontsize = 16,
                        foreground = colors[5],
                        background = colors[1],
                       ),
               widget.Sep(
                        linewidth = 1,
                        padding = 10,
                        foreground = colors[2],
                        background = colors[1]
                        ),
               widget.Systray(
                        background=colors[1],
                        icon_size = 27,
                        padding = 10
                        ),
              ]
    return widgets_list

widgets_list = init_widgets_list()


def init_widgets_screen1():
    widgets_screen1 = init_widgets_list()
    return widgets_screen1

def init_widgets_screen2():
    widgets_screen2 = init_widgets_list()
    return widgets_screen2

widgets_screen1 = init_widgets_screen1()
widgets_screen2 = init_widgets_screen2()


def init_screens(bo, s):
    return [Screen(top=bar.Bar(widgets=init_widgets_screen1(), size=s,opacity=bo)),
            Screen(top=bar.Bar(widgets=init_widgets_screen2(), size=26))]

screens = init_screens(bo=bar_opacity, s=bar_size)

# MOUSE CONFIGURATION
mouse = [
    Drag([mod], "Button1", lazy.window.set_position_floating(),
         start=lazy.window.get_position()),
    Drag([mod], "Button3", lazy.window.set_size_floating(),
         start=lazy.window.get_size())
]

dgroups_key_binder = None
dgroups_app_rules = []

# ASSIGN APPLICATIONS TO A SPECIFIC GROUPNAME
@hook.subscribe.client_new
def assign_app_group(client):
    d = {}
    d["2"] = ["Navigator", "firefox", "Firefox"]
    d["3"] = ["Meld", "meld", "org.gnome.meld", "org.gnome.Meld" ]
    d["4"] = [ "telegram-desktop", "TelegramDesktop", 
        "Thunderbird", "thunderbird",
        "Mailspring", "mailspring"]
    d["5"] = ["Pithos", "pithos" ]
    d["6"] = ["Thunar", "thunar",
    "Nautilus", "org.gnome.Nautilus",
    "nautilus", "org.gnome.nautilus"]

    wm_class = client.window.get_wm_class()[0]

    for i in range(len(d)):
        if wm_class in list(d.values())[i]:
            group = list(d.keys())[i]
            client.togroup(group)
            client.group.cmd_toscreen()

main = None

@hook.subscribe.startup_once
def start_once():
    home = os.path.expanduser('~')
    subprocess.call([home + '/.config/qtile/scripts/autostart.sh'])

@hook.subscribe.startup
def start_always():
    # Set the cursor to something sane in X
    subprocess.Popen(['xsetroot', '-cursor_name', 'left_ptr'])

@hook.subscribe.client_new
def set_floating(window):
    if (window.window.get_wm_transient_for()
            or window.window.get_wm_type() in floating_types):
        window.floating = True

floating_types = ["notification", "toolbar", "splash", "dialog"]


follow_mouse_focus = True
bring_front_click = False
cursor_warp = False
floating_layout = layout.Floating(float_rules=[
    {'wmclass': 'Arcolinux-welcome-app.py'},
    {'wmclass': 'Arcolinux-tweak-tool.py'},
    {'wmclass': 'confirm'},
    {'wmclass': 'dialog'},
    {'wmclass': 'download'},
    {'wmclass': 'error'},
    {'wmclass': 'file_progress'},
    {'wmclass': 'notification'},
    {'wmclass': 'splash'},
    {'wmclass': 'toolbar'},
    {'wmclass': 'confirmreset'},
    {'wmclass': 'makebranch'},
    {'wmclass': 'maketag'},
    {'wmclass': 'Arandr'},
    {'wmclass': 'feh'},
    {'wmclass': 'Galculator'},
    {'wmclass': 'arcolinux-logout'},
    {'wmclass': 'xfce4-terminal'},
    {'wname': 'branchdialog'},
    {'wname': 'Open File'},
    {'wname': 'pinentry'},
    {'wmclass': 'ssh-askpass'},

],  fullscreen_border_width = 0, border_width = 0)
auto_fullscreen = True

focus_on_window_activation = "focus" # or smart

wmname = "LG3D"
