import os
import subprocess

from libqtile import bar, layout, widget, hook
from libqtile.config import Click, Drag, Group, Key, Match, Screen
from libqtile.lazy import lazy
from libqtile.utils import guess_terminal

mod = "mod4"
mod1 = "alt"
mod2 = "control"
GAP = 25
BORDER_WIDTH = 3
BORDER_FOCUS_COLOR = "#5e81ac"
BORDER_NORMAL_COLOR = "#4c566a"

terminal = guess_terminal()

@hook.subscribe.startup_once
def start_once():
    home = os.path.expanduser('~')
    subprocess.call([home + '/.config/qtile/scripts/autostart.sh'])

keys = [
    # A list of available commands that can be bound to keys can be found
    # at https://docs.qtile.org/en/latest/manual/config/lazy.html

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
    Key([mod], "w", lazy.spawn('firefox')),
    # Terminal
    Key([mod], "Return", lazy.spawn(terminal), desc="Launch terminal"),
    # Key([mod], "Return", lazy.spawn('termite')),
    # Key([mod], "KP_Enter", lazy.spawn('termite')),
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

names = ['1', '2', '3', '4', '5', '6', '7']
# labels = ['1', '2', '3', '4', '5', '6', '7']
labels = ["" ,"", "", "", "", "", "" ]
layouts = ["max", "monadtall", "monadtall", "monadtall", "monadtall",
           "monadtall", "max"]
spawns = ['termite', 'firefox -P "default" --class="firefox"', None,
         ['mailspring', 'telegram-desktop'], None, 'thunar', None]
groups = [Group(name=name, layout=layout, label=label, spawn=spawn)
          for name, label, layout, spawn in zip(names, labels, layouts, spawns)]

# groups = []

# FOR QWERTY KEYBOARDS
#group_names = ["1", "2", "3", "4", "5", "6", "7", "8", "9", "0",]
#group_labels = ["", "", "", "", "", "", "", "", "", "",]
#group_labels = ["Web", "Edit/chat", "Image", "Gimp", "Meld", "Video", "Vb", "Files", "Mail", "Music",]
#group_layouts = ["monadtall", "matrix", "monadtall", "bsp", "monadtall", "matrix", "monadtall", "bsp", "monadtall", "monadtall",]

# group_names = ['1', '2', '3', '4', '5', '6', '7']
# group_labels = ['1', '2', '3', '4', '5', '6', '7']
# # group_labels = ["" ,"", "", "", "", "", "" ]
# group_layouts = ["max", "monadtall", "monadtall", "monadtall", "monadtall", "monadtall", "max"]
# group_spawn = ['termite', 'firefox -P "default" --class="firefox"', None, ['mailspring', 'telegram-desktop'], None, 'thunar', 'firefox -P "hass" --class="hass" --new-window "http://docky:8123/floorplan"']

# for i in range(len(group_names)):
#     groups.append(
#         Group(
#             name=group_names[i],
#             layout=group_layouts[i],
#             label=group_labels[i],
#             spawn=group_spawn[i],
#         ))
for i in groups:
    keys.extend([

        #CHANGE WORKSPACES
        Key([mod], i.name, lazy.group[i.name].toscreen()),
        Key([mod], "Tab", lazy.screen.next_group()),
        Key([mod, "shift"], "Tab", lazy.screen.prev_group()),
        Key(["mod1"], "Tab", lazy.screen.next_group()),
        Key(["mod1", "shift"], "Tab", lazy.screen.prev_group()),

        # MOVE WINDOW TO SELECTED WORKSPACE 1-10 AND STAY ON WORKSPACE
        Key([mod, "shift"], i.name, lazy.window.togroup(i.name)),

        # MOVE WINDOW TO SELECTED WORKSPACE 1-10 AND FOLLOW MOVED WINDOW TO WORKSPACE
        Key([mod, "shift"], i.name, lazy.window.togroup(i.name) , lazy.group[i.name].toscreen()),
    ])
# groups = [Group(i) for i in "123456"]

# for i in groups:
#     keys.extend(
#         [
#             # mod1 + letter of group = switch to group
#             Key(
#                 [mod],
#                 i.name,
#                 lazy.group[i.name].toscreen(),
#                 desc="Switch to group {}".format(i.name),
#             ),
#             # mod1 + shift + letter of group = switch to & move focused window to group
#             Key(
#                 [mod, "shift"],
#                 i.name,
#                 lazy.window.togroup(i.name, switch_group=True),
#                 desc="Switch to & move focused window to group {}".format(i.name),
#             ),
#             # Or, use below if you prefer not to switch to that group.
#             # # mod1 + shift + letter of group = move focused window to group
#             # Key([mod, "shift"], i.name, lazy.window.togroup(i.name),
#             #     desc="move focused window to group {}".format(i.name)),
#         ]
#     )

layout_theme = {
    "margin": GAP,
    "border_width": BORDER_WIDTH,
    "border_focus": BORDER_FOCUS_COLOR,
    "border_normal": BORDER_NORMAL_COLOR,
    }

layouts = [
    layout.MonadTall(**layout_theme),
    layout.MonadWide(**layout_theme),
    layout.Floating(**layout_theme),
    layout.Max(**layout_theme),
    # layout.Max(),
    # layout.Floating(),
    # layout.Columns(border_focus_stack=["#d75f5f", "#8f3d3d"], border_width=4),
    # Try more layouts by unleashing below layouts.
    # layout.Stack(num_stacks=2),
    # layout.Bsp(),
    # layout.Matrix(),
    # layout.MonadTall(),
    # layout.MonadWide(),
    # layout.RatioTile(),
    # layout.Tile(),
    # layout.TreeTab(),
    # layout.VerticalTile(),
    # layout.Zoomy(),
]

widget_defaults = dict(
    font="sans",
    fontsize=12,
    padding=3,
)
extension_defaults = widget_defaults.copy()

screens = [
    Screen(
        bottom=bar.Bar(
            [
                widget.CurrentLayout(),
                widget.GroupBox(),
                widget.Prompt(),
                widget.WindowName(),
                widget.Chord(
                    chords_colors={
                        "launch": ("#ff0000", "#ffffff"),
                    },
                    name_transform=lambda name: name.upper(),
                ),
                widget.TextBox("default config", name="default"),
                widget.TextBox("Press &lt;M-r&gt; to spawn", foreground="#d75f5f"),
                widget.Systray(),
                widget.Clock(format="%Y-%m-%d %a %I:%M %p"),
                widget.QuickExit(),
            ],
            24,
            # border_width=[2, 0, 2, 0],  # Draw top and bottom borders
            # border_color=["ff00ff", "000000", "ff00ff", "000000"]  # Borders are magenta
        ),
    ),
]

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
