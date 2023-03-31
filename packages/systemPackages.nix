{ pkgs, ... }: {

  environment.systemPackages = with pkgs; [
    bat
    burpsuite
    curl
    discord
    fd
    firefox
    fzf
    gimp
    git
    gnome.nautilus
    gnome.sushi
    gvfs
    gnome.gvfs
    google-chrome
    gparted
    htop-vim
    inkscape
    kdenlive frei0r ffmpeg-full
    lastpass-cli
    mailspring
    mlocate
    mpv
    networkmanager-openvpn
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
    feh
    sqlmap
    variety
    wget
    wpscan
    youtube-dl
  ];

  fonts.fonts = with pkgs; [
    hack-font
    # Get nerdfonts override string from:
    # https://github.com/ryanoasis/nerd-fonts/tree/master/patched-fonts
    (nerdfonts.override { fonts = [ "FiraCode" "Hack" "NerdFontsSymbolsOnly"]; })
  ];
}
