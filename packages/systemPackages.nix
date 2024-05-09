{ pkgs, ... }: {

  environment.systemPackages = with pkgs; [
    guake
    man-pages
    man-pages-posix
    linux-manual
    bat
    discord
    burpsuite
    thc-hydra
    nikto
    nmap
    metasploit
    wapiti
    aircrack-ng
    wifite2
    iw
    tshark
    reaverwps-t6x
    bully
    cowpatty
    hashcat
    pixiewps
    kismet
    airgeddon
    wavemon
    curl
    discord
    fd
    firefox
    tor-browser-bundle-bin
    xorg.libpciaccess
    fzf
    gimp
    git
    gnome.nautilus
    gnome.sushi
    gtop
    gvfs
    gnome.gvfs
    google-chrome
    tor-browser-bundle-bin
    gparted
    htop-vim
    inkscape
    kdenlive frei0r ffmpeg-full
    lastpass-cli
    mailspring
    mlocate
    mpv
    networkmanager-openvpn
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
    virtualbox
    kubectl
    kubernetes-helm
    dig
    ripgrep
    nfs-utils
    argocd
    kubeseal
    jq
  ];

  fonts.packages = with pkgs; [
    hack-font
    # Get nerdfonts override string from:
    # https://github.com/ryanoasis/nerd-fonts/tree/master/patched-fonts
    ( nerdfonts.override { fonts = [ "FiraCode" "Hack" "NerdFontsSymbolsOnly" ]; } )
  ];

  nixpkgs.config.permittedInsecurePackages = [
    "mailspring-1.12.0"
  ];

  # nixpkgs.config.allowUnfreePredicate = pkg: builtins.elem (lib.getName pkg) [
  #   "steam"
  #   "steam-original"
  #   "steam-runtime"
  # ];
}
