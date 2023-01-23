{ pkgs, ... }: {

  environment.systemPackages = with pkgs; [
    curl
    discourse
    firefox
    gimp
    git
    gnome.gnome-tweaks
    google-chrome
    gparted
    htop-vim
    inkscape
    kdenlive frei0r ffmpeg-full
    lastpass-cli
    mailspring
    mlocate
    mpv
    nikto
    numix-icon-theme
    numix-icon-theme-circle
    numix-icon-theme-square
    obs-studio
    pinentry-curses
    pithos
    pianobar
    plexamp
    plex-media-player
    powerline
    # powerline-fonts
    tdesktop
    tree
    wget
    wpscan
  ];
}
