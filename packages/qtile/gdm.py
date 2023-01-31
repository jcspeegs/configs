# Running Qtile inside Gnome
#
# https://docs.qtile.org/en/latest/manual/install/gnome.html
#
# Register Qtile with gnome-session
# Without it, a "Something has gone wrong!" message shows up a short while
# after logging in. dbus-send must be on your $PATH.

import subprocess
import os
from libqtile import hook

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

