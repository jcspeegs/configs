import os
import subprocess
from collections import namedtuple
from box import Box
import yaml

from libqtile import layout, widget, hook
from libqtile.bar import Bar
from libqtile.config import Click, Drag, Group, Key, Match, Screen, \
    ScratchPad, DropDown
from libqtile.lazy import lazy
from libqtile.utils import guess_terminal

home = os.path.expanduser('~')
cfg = os.path.join(home, '.config', 'qtile', 'config.yaml')

mod, mod1, mod2 = 'mod4', 'alt', 'control'
# mod1 = "alt"
# mod2 = "control"

cfg = Box.from_yaml(filename=cfg)
bar_theme = cfg.bar_theme

rofi_cmd = "rofi -show combi -modes combi -combi-modes 'window,drun,run,ssh'" \
    "-font 'Hack 18' -show-icons"
# dmen_cmd = "dmenu_run -i -o .9 -dim .2 -h 60 -l 30 -w 960 -x 480 -sf 'black' -fn 'Hack'"
# dmen_cmd2 = ''

terminal = guess_terminal()

@hook.subscribe.startup_once
def start_once(home=home):
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
    Key([mod], "f", lazy.spawn('nautilus')),
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
    Key([mod], "d", lazy.spawn(rofi_cmd)),
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

    # Scroll groups
    Key([mod], "Tab", lazy.screen.next_group()),
    Key([mod, "shift"], "Tab", lazy.screen.prev_group()),
    Key(["mod1"], "Tab", lazy.screen.next_group()),
    Key(["mod1", "shift"], "Tab", lazy.screen.prev_group()),

    # Change monitor focus - super-ctrl-[hl]
    Key([mod, mod2], 'h', lazy.next_screen()),
    Key([mod, mod2], 'l', lazy.prev_screen()),

    # Dropdown
    Key([], 'F12', lazy.group['scratchpad'].dropdown_toggle('qtile_log')),
    Key([], 'F8', lazy.group['scratchpad'].dropdown_toggle('pianobar')),
    Key([mod], "grave", lazy.group['scratchpad'].dropdown_toggle('dropterm')),
]

static_groups = [
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

pianobar = "termite -e 'pianobar'"
qtile_log = f"termite -e 'tail -fn 199 {home}/.local/share/qtile/qtile.log'"
dropterm = "termite"
dropdowns = [{'name': 'qtile_log', 'cmd': qtile_log},
             {'name': 'pianobar', 'cmd': pianobar},
             {'name': 'dropterm', 'cmd': dropterm},]

dropdowns = [DropDown(**dropdown, **cfg.dropdown_theme) for dropdown in dropdowns]
groups = [Group(**group) for group in static_groups]
groups += [ScratchPad('scratchpad', dropdowns)]

names = [group.get('name') for group in static_groups]
for name in names:
    keys.extend([

        # Change workspace on current monitor
        Key([mod], name, lazy.group[name].toscreen()),

        # MOVE WINDOW TO SELECTED WORKSPACE 1-10 AND STAY ON WORKSPACE
        # Key([mod, "shift"], name, lazy.window.togroup(i.name)),

        # MOVE WINDOW TO SELECTED WORKSPACE 1-10 AND FOLLOW MOVED WINDOW TO WORKSPACE
        Key([mod, "shift"], name, lazy.window.togroup(name), lazy.group[name].toscreen()),
    ])

layouts = [
    layout.MonadTall(**cfg.layout_theme),
    layout.MonadWide(**cfg.layout_theme),
    layout.Max(**cfg.layout_theme),
    layout.Columns(split=False, **cfg.layout_theme),
    # layout.Stack(**cfg.layout_theme),
    # Try more layouts by unleashing below layouts.
    # layout.Bsp(),
    # layout.Matrix(),
    # layout.RatioTile(),
    # layout.Tile(),
    # layout.TreeTab(),
    # layout.VerticalTile(),
    # layout.Zoomy(),
]

widgets=[
    widget.GroupBox(**bar_theme, **cfg.groupbox_cfg),
    widget.Spacer(**bar_theme, length=700),
    widget.Clock(**bar_theme, **cfg.clock_cfg),
    widget.Spacer(**bar_theme),
    widget.Net(**bar_theme, **cfg.net_cfg, fmt='{}', format='{down}'),
    widget.NetGraph(**bar_theme, **cfg.net_graph, bandwidth_type='down'),
    widget.Net(**bar_theme, **cfg.net_cfg, fmt='{}', format='{up}'),
    widget.NetGraph(**bar_theme, **cfg.net_graph, bandwidth_type='up'),
    # widget.GenPollCommand(update_interval=15, cmd="echo asdf"),
    widget.Memory(**bar_theme, **cfg.memory_cfg),
    # widget.ThermalSensor(**bar_theme, **cfg.thermal_cfg, fmt='{}',
    #                      tag_sensor='Package id 0', threshold=80),
    # widget.NvidiaSensors(**bar_theme, **cfg.gpu_cfg, fmt='󰓓{}'),
    # widget.Battery(**bar_theme, **cfg.battery_cfg),
    widget.Wlan(**bar_theme, **cfg.wlan_cfg, interface=os.getenv('wifi_adapter')),
    widget.Systray(**bar_theme, **cfg.systray_cfg),
    widget.QuickExit(**bar_theme, **cfg.exit_cfg),
]

if os.path.isdir('/sys/class/power_supply/BAT1'):
    widgets.insert(-3, widget.Battery(**bar_theme, **cfg.battery_cfg))

screens = [Screen(top=Bar(**cfg.bar_cfg, widgets=widgets)) ]

# Drag floating layouts.
mouse = [
    Drag([mod], "Button1", lazy.window.set_position_floating(), start=lazy.window.get_position()),
    Drag([mod], "Button3", lazy.window.set_size_floating(), start=lazy.window.get_size()),
    Click([mod], "Button2", lazy.window.bring_to_front()),
]

floating_layout = layout.Floating(
    border_width = 0,
    float_rules=[
        # Run the utility of `xprop` to see the wm class and name of an X client.
        *layout.Floating.default_float_rules,
        Match(wm_class="confirmreset"),  # gitk
        Match(wm_class="makebranch"),  # gitk
        Match(wm_class="maketag"),  # gitk
        Match(wm_class="ssh-askpass"),  # ssh-askpass
        Match(title="branchdialog"),  # gitk
        Match(title="pinentry"),  # GPG key password entry
        Match(wm_class="Variety"),  # Variety wallpaper
        Match(title="Calculator"),
    ]
)

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
