#!/usr/bin/env bash

function run {
  if ! pgrep $1 ;
  then
    $@&
  fi
}

# run() { [[ ! $( pgrep $1 ) ]] && $@& }

#Set your native resolution IF it does not exist in xrandr
#More info in the script
#run $HOME/.config/qtile/scripts/set-screen-resolution-in-virtualbox.sh

#Find out your monitor name with xrandr or arandr (save and you get this line)
case $HOSTNAME in
    lightshow)
        xrandr --output DP-0 --mode 1920x1080 --pos 4672x0 --rotate normal --scale 1.1 --output DP-1 --off --output HDMI-0 --mode 1920x1080 --pos 2560x0 --rotate normal --scale 1.1 --output DP-2 --primary --mode 2560x1440 --pos 0x0 --rotate normal --output DP-3 --off --output DP-4 --off --output DP-5 --off --output USB-C-0 --off
        ;;
    tabby)
        xrandr --output eDP-1 --primary --mode 2736x1824 --pos 0x0 --rotate normal --output DP-1 --off --output HDMI-1 --off --output DP-2 --off --output HDMI-2 --off
        # xrandr --output eDP-1 --primary --mode 2736x1824 --pos 0x0 --rotate normal --output DP-1 --off --output HDMI-1 --off --output DP-2 --off --output HDMI-2 --off --dpi 200
        ;;
esac


#Some ways to set your wallpaper besides variety or nitrogen
#feh --bg-fill /usr/share/backgrounds/arcolinux/arco-wallpaper.jpg &
#start the conky to learn the shortcuts
#(conky -c $HOME/.config/qtile/scripts/system-overview) &

#starting utility applications at boot time
picom --config /etc/nixos/packages/picom.conf --experimental-backend &
dunst --config ~/.config/dunst/dunstrc &
run variety &
run nm-applet &
# run pamac-tray &
# run xfce4-power-manager &
# numlockx on &
# blueberry-tray &
# /usr/lib/polkit-gnome/polkit-gnome-authentication-agent-1 &
# /usr/lib/xfce4/notifyd/xfce4-notifyd &
# run /opt/piavpn/bin/pia-client &

#starting user applications at boot time
# run volumeicon &
#run discord &
#nitrogen --restore &
#run caffeine -a &
#run firefox -P "hass" --class="hass" --new-window "http://docky:8123/floorplan" &
# run thunar &
#run dropbox &
#run insync start &
# run telegram-desktop &
# run mailspring &
# run termite &
#run firefox -P 'default' --class='firefox' &
