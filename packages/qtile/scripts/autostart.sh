#!/usr/bin/env bash

function run {
  if ! pgrep $1 ;
  then
    $@&
  fi
}

#Set your native resolution IF it does not exist in xrandr
#More info in the script
#run $HOME/.config/qtile/scripts/set-screen-resolution-in-virtualbox.sh

#Find out your monitor name with xrandr or arandr (save and you get this line)
case $HOSTNAME in
    tabby)
        xrandr --output eDP-1 --primary --mode 2736x1824 --pos 0x0 \
            --rotate normal --output DP-1 --off --output HDMI-1 --off \
            --output DP-2 --off --output HDMI-2 --off --dpi 200
        ;;
esac


#Some ways to set your wallpaper besides variety or nitrogen
#feh --bg-fill /usr/share/backgrounds/arcolinux/arco-wallpaper.jpg &
#start the conky to learn the shortcuts
#(conky -c $HOME/.config/qtile/scripts/system-overview) &

#starting utility applications at boot time
# run variety &
# run nm-applet &
# run pamac-tray &
# run xfce4-power-manager &
# numlockx on &
# blueberry-tray &
# picom --config $HOME/.config/qtile/scripts/picom.conf &
# /usr/lib/polkit-gnome/polkit-gnome-authentication-agent-1 &
# /usr/lib/xfce4/notifyd/xfce4-notifyd &
# run /opt/piavpn/bin/pia-client &

#starting user applications at boot time
# run volumeicon &
#run discord &
#nitrogen --restore &
#run caffeine -a &
#run firefox -P "hass" --class="hass" --new-window "http://docky:8123/floorplan" &
#run thunar &
#run dropbox &
#run insync start &
#run telegram-desktop &
#run mailspring &
#run termite &
#run firefox -P 'default' --class='firefox' &
