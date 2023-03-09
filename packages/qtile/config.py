import os
import subprocess
from collections import namedtuple

from libqtile import layout, widget, hook
from libqtile.bar import Bar
from libqtile.config import Click, Drag, Group, Key, Match, Screen
from libqtile.lazy import lazy
from libqtile.utils import guess_terminal

mod = "mod4"
mod1 = "alt"
mod2 = "control"

    # return [["#2F343F", "#2F343F"], # color 0 - gray_dk
    #         ["#2F343F", "#2F343F"], # color 1 - gray_dk
    #         ["#c0c5ce", "#c0c5ce"], # color 2 - gray_lt
    #         ["#fba922", "#fba922"], # color 3 - orange
    #         ["#3384d0", "#3384d0"], # color 4 - blue_1
    #         ["#f3f4f5", "#f3f4f5"], # color 5 - white
    #         ["#cd1f3f", "#cd1f3f"], # color 6 - red
    #         ["#62FF00", "#62FF00"], # color 7 - green
    #         ["#6790eb", "#6790eb"], # color 8 - blue_2
    #         ["#a9a9a9", "#a9a9a9"]] # color 9 - gray
colors = {
    'gray_dk':["#2F343F", "#2F343F"],
    'gray_dk2': ["#4c566a", "#4c566a"],
    'gray': ["#a9a9a9", "#a9a9a9"],
    'gray_lt': ["#c0c5ce", "#c0c5ce"],
    'orange': ["#fba922", "#fba922"],
    'blue_1': ["#3384d0", "#3384d0"],
    'blue_2': ["#6790eb", "#6790eb"],
    'blue_3': ["#4c566a", "#4c566a"],
    'white': ["#f3f4f5", "#f3f4f5"],
    'red': ["#cd1f3f", "#cd1f3f"],
    'green': ["#62FF00", "#62FF00"],
}
Colors = namedtuple('Colors', colors.keys())
colors = Colors(**colors)

bar_attrs = {
    'font': 'Hack',
    'fontsize': 26,
    'foreground': colors.gray_lt,
}
BarAttrs = namedtuple('BarAttrs', bar_attrs.keys())
bar_attrs = BarAttrs(**bar_attrs)

layout_theme = {
    "margin": 25,
    "border_width": 3,
    "border_focus": colors.blue_3,
    "border_normal": colors.gray_dk,
}

bar_cfg = {
    'size': 70,
    'opacity': 0.75,
}

bar_theme = {
    'background': colors.gray_dk,
}

groupbox_cfg = {
    'fontsize': 70,
    'margin_y': 3,
    'margin_x': 0,
    'padding_y': 6,
    'padding_x': 3,
    'borderwidth': 0,
    'disable_drag': True,
    'active': colors.white,
    'inactive': colors.gray,
    'rounded': False,
    'highlight_method': "text",
    'this_current_screen_border': colors.blue_2,
    'foreground': bar_attrs.foreground,
}

sep = {
    'linewidth': 1,
    'padding': 10,
    'foreground': bar_attrs.foreground,
}

net_cfg = {
    'font': bar_attrs.font,
    'fontsize': bar_attrs.fontsize,
    'foreground': bar_attrs.foreground,
    'padding': 0,
    'prefix': 'M',
    'use_bits': True,
}

net_graph = {
    'start_pos': 'top',
    'border_width': 0,
    'fill_color': colors.gray_lt,
    'graph_color': colors.blue_2,
}

text = {
    'foreground': bar_attrs.foreground,
    'fontsize': bar_attrs.fontsize,
}

clock_cfg = {
    'foreground': bar_attrs.foreground,
    'fontsize': 33,
    'format': '%-I:%M%p %a, %B %-d, %Y',
    'fmt': ' {}',
}

battery_cfg = {
    'charge_char': '󰂅',
    'discharge_char': '󰁹',
    'empty_char': '󱃌',
    'font': bar_attrs.font,
    'fontsize': bar_attrs.fontsize,
    'foreground': bar_attrs.foreground,
    'full_char': '󰁹',
    'hide_threshold': 0.8,
    'low_foreground': colors.red,
    'low_percentage': 0.2,
    'notify_below': 0.2,
}

memory_cfg = {
    'font': bar_attrs.font,
    'fontsize': bar_attrs.fontsize,
    'foreground': bar_attrs.foreground,
    'format': '{MemUsed:.1f}{mm}/{MemPercent}%',
    'measure_mem': 'G',
    'fmt': '{}',
}

systray_cfg = {
    'icon_size': bar_attrs.fontsize,
}

exit_cfg = {
    'default_text': '',
    'fontsize': bar_attrs.fontsize,
    'foreground': bar_attrs.foreground,
}

wlan_cfg = {
    'font': bar_attrs.font,
    'fontsize': bar_attrs.fontsize,
    'foreground': bar_attrs.foreground,
    'format': '{essid}/{percent:2.0%}',
    'fmt': '󰖩 {}',
}

thermal_cfg = {
    'font': bar_attrs.font,
    'fontsize': bar_attrs.fontsize,
    'foreground': bar_attrs.foreground,
    'foreground_alert': colors.red,
    'metric': True,
    'format': '{temp:.0f}{unit}',
    'padding': 6,
}

gpu_cfg = {
    'font': bar_attrs.font,
    'fontsize': bar_attrs.fontsize,
    'foreground': bar_attrs.foreground,
    'foreground_alert': colors.red,
    'format': '{temp}°C',
    'threshold': 80,
}

ping_cfg = {
    'cmd': ['ping', 'www.google.com'],
    # 'cmd': 'ping -c3 www.google.com | tail -n1 | cut -d"/" -f5',
    # 'fmt': '󰊭{}ms',
    # 'font': bar_attrs.font,
    # 'fontsize': bar_attrs.fontsize,
    # 'foreground': bar_attrs.foreground,
    # 'shell': True,
    # 'update_interval': 15,
}

# dmen_cmd = "dmenu_run -i -o .9 -dim .2 -h 60 -l 30 -w 960 -x 480 -sf 'black' -fn 'Hack'"
# dmen_cmd2 = ''

terminal = guess_terminal()

@hook.subscribe.startup_once
def start_once():
    home = os.path.expanduser('~')
    subprocess.call([home + '/.config/qtile/scripts/autostart.sh'])

keys = [
    # Super Keys
    Key([mod], "Up", lazy.window.toggle_fullscreen()),
    Key([mod], "q", lazy.window.kill(), desc="Kill focused window"),
    # Key([mod], "x", lazy.spawn('arcolinux-logout')),
    Key([mod], "z", lazy.spawn('betterlockscreen -l -- --timestr="%H:%M"')),
    Key([mod], "r", lazy.restart()),
    Key([mod, "control"], "r", lazy.reload_config(), desc="Reload the config"),
    Key([mod], "Escape", lazy.spawn('xkill')),

    # File browser
    Key([mod], "f", lazy.spawn('thunar')),
    # Email
    Key([mod], "m", lazy.spawn('mailspring')),
    # Music
    Key([mod], "p", lazy.spawn('pithos')),
    # Telegram
    Key([mod], "t", lazy.spawn('telegram-desktop')),
    # Web browser
    Key([mod], "w", lazy.spawn('firefox --new-window')),
    # Terminal
    Key([mod], "Return", lazy.spawn(terminal), desc="Launch terminal"),
    # Launcher
    # Key([mod], "d", lazy.spawn(dmen_cmd)),
    # Key([mod, "shift"], "d", lazy.spawn(dmen_cmd2)),
    # Key([mod], "F11", lazy.spawn('rofi -show run -fullscreen')),
    # Key([mod], "F12", lazy.spawn('rofi -show run')),
    # Conky
    # Key([mod], "c", lazy.spawn('conky-toggle')),
    # Volume
    Key([mod], "v", lazy.spawn('pavucontrol')),

    # QTILE LAYOUT KEYS
    Key([mod], "n", lazy.layout.normalize()),
    Key([mod], "space", lazy.next_layout(), desc="Toggle between layouts"),

    # SUPER + SHIFT KEYS
    Key([mod, "shift"], "x", lazy.shutdown(), desc="Shutdown Qtile"),

    # Switch between windows
    Key([mod], "h", lazy.layout.left(), desc="Move focus to left"),
    Key([mod], "l", lazy.layout.right(), desc="Move focus to right"),
    Key([mod], "j", lazy.layout.down(), desc="Move focus down"),
    Key([mod], "k", lazy.layout.up(), desc="Move focus up"),
]

gconfs = [
    {'name': '1', 'label': '', 'layout': 'monadtall',
     'spawn': 'termite'},
    {'name': '2', 'label': '󰈹', 'layout': 'monadtall',
     'spawn': 'firefox -P "default" --class="firefox"'},
    {'name': '3', 'label': ""},
    {'name': '4', 'label': "", 'layout': 'columns',
     'spawn': ['mailspring', 'telegram-desktop']},
    {'name': '5', 'label': ""},
    {'name': '6', 'label': "", 'layout':'monadtall',
     'spawn': 'thunar'},
    {'name': '7', 'label': ""},
]
groups = [Group(**gconf) for gconf in gconfs]

for i in groups:
    keys.extend([

        # Change workspace on current monitor
        Key([mod], i.name, lazy.group[i.name].toscreen()),
        Key([mod], "Tab", lazy.screen.next_group()),
        Key([mod, "shift"], "Tab", lazy.screen.prev_group()),
        Key(["mod1"], "Tab", lazy.screen.next_group()),
        Key(["mod1", "shift"], "Tab", lazy.screen.prev_group()),

        # Change monitor focus - super-ctrl-[hl]
        Key([mod, mod2], 'h', lazy.next_screen()),
        Key([mod, mod2], 'l', lazy.prev_screen()),

        # MOVE WINDOW TO SELECTED WORKSPACE 1-10 AND STAY ON WORKSPACE
        # Key([mod, "shift"], i.name, lazy.window.togroup(i.name)),

        # MOVE WINDOW TO SELECTED WORKSPACE 1-10 AND FOLLOW MOVED WINDOW TO WORKSPACE
        Key([mod, "shift"], i.name, lazy.window.togroup(i.name) , lazy.group[i.name].toscreen()),
    ])

layouts = [
    layout.MonadTall(**layout_theme),
    layout.MonadWide(**layout_theme),
    layout.Floating(**layout_theme),
    layout.Max(**layout_theme),
    layout.Columns(split=False, **layout_theme),
    # layout.Stack(**layout_theme),
    # Try more layouts by unleashing below layouts.
    # layout.Bsp(),
    # layout.Matrix(),
    # layout.RatioTile(),
    # layout.Tile(),
    # layout.TreeTab(),
    # layout.VerticalTile(),
    # layout.Zoomy(),
]


screens = [
    Screen(
        top=Bar(**bar_cfg,
            widgets=[
                widget.GroupBox(**bar_theme, **groupbox_cfg),
                widget.Spacer(**bar_theme, length=700),
                widget.Clock(**bar_theme, **clock_cfg),
                widget.Spacer(**bar_theme),
                widget.Net(**bar_theme, **net_cfg, fmt='{}', format='{down}'),
                widget.NetGraph(**bar_theme, **net_graph, bandwidth_type='down'),
                widget.Net(**bar_theme, **net_cfg, fmt='{}', format='{up}'),
                widget.NetGraph(**bar_theme, **net_graph, bandwidth_type='up'),
                # widget.Sep(**bar_theme, **sep),
                # widget.GenPollCommand(update_interval=15, cmd="echo asdf"),
                widget.Memory(**bar_theme, **memory_cfg),
                # widget.Sep(**bar_theme, **sep),
                widget.ThermalSensor(**bar_theme, **thermal_cfg, fmt='{}',
                                     tag_sensor='Package id 0', threshold=80),
                widget.NvidiaSensors(**bar_theme, **gpu_cfg, fmt='󰓓{}'),
                # widget.Wlan(**bar_theme, **wlan_cfg),
                # widget.Sep(**bar_theme, **sep),
                widget.Systray(**bar_theme, **systray_cfg),
                widget.QuickExit(**bar_theme, **exit_cfg),
            ]
        )
    )
]

if os.path.isfile('/sys/class/power_supply/battery_name'):
    screens.insert(widget.Battery(**bar_theme, **battery_cfg), 11)

# Drag floating layouts.
mouse = [
    Drag([mod], "Button1", lazy.window.set_position_floating(), start=lazy.window.get_position()),
    Drag([mod], "Button3", lazy.window.set_size_floating(), start=lazy.window.get_size()),
    Click([mod], "Button2", lazy.window.bring_to_front()),
]

dgroups_key_binder = None
dgroups_app_rules = []  # type: list
follow_mouse_focus = True
bring_front_click = False
cursor_warp = False
floating_layout = layout.Floating(
    float_rules=[
        # Run the utility of `xprop` to see the wm class and name of an X client.
        *layout.Floating.default_float_rules,
        Match(wm_class="confirmreset"),  # gitk
        Match(wm_class="makebranch"),  # gitk
        Match(wm_class="maketag"),  # gitk
        Match(wm_class="ssh-askpass"),  # ssh-askpass
        Match(title="branchdialog"),  # gitk
        Match(title="pinentry"),  # GPG key password entry
    ]
)
auto_fullscreen = True
focus_on_window_activation = "smart"
reconfigure_screens = True

# If things like steam games want to auto-minimize themselves when losing
# focus, should we respect this or not?
auto_minimize = True

# When using the Wayland backend, this can be used to configure input devices.
wl_input_rules = None

# XXX: Gasp! We're lying here. In fact, nobody really uses or cares about this
# string besides java UI toolkits; you can see several discussions on the
# mailing lists, GitHub issues, and other WM documentation that suggest setting
# this string if your java app doesn't work correctly. We may as well just lie
# and say that we're a working one by default.
#
# We choose LG3D to maximize irony: it is a 3D non-reparenting WM written in
# java that happens to be on java's whitelist.
wmname = "LG3D"


# Register Qtile with gnome-session
@hook.subscribe.startup
def dbus_register():
    id = os.environ.get('DESKTOP_AUTOSTART_ID')
    if not id:
        return
    subprocess.Popen(['dbus-send',
                      '--session',
                      '--print-reply',
                      '--dest=org.gnome.SessionManager',
                      '/org/gnome/SessionManager',
                      'org.gnome.SessionManager.RegisterClient',
                      'string:qtile',
                      'string:' + id])
