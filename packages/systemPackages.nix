{ pkgs, ... }: {

  environment.systemPackages = with pkgs; [
    gradia
    epson-escpr
    epson-escpr2
    youtube-music
    eza
    renameutils
    tailscale
    yamllint
    guake
    neofetch
    man
    # man-pages
    # man-pages-posix
    # linux-manual
    bat
    bat-extras.core
    discord
    burpsuite
    thc-hydra
    nikto
    nmap
    metasploit
    # wapiti
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
    gimp
    git
    nautilus
    sushi
    gtop
    gvfs
    gnome.gvfs
    google-chrome
    tor-browser-bundle-bin
    gparted
    htop-vim
    inkscape
    kdePackages.kdenlive frei0r ffmpeg-full
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
    plex-desktop
    # python311Packages.powerline
    powerline
    powerline-fonts
    tdesktop
    tree
    feh
    sqlmap
    variety
    wget
    wpscan
    # youtube-dl
    yt-dlp
    # virtualbox
    kubectl
    kubernetes-helm
    dig
    ripgrep
    nfs-utils
    argocd
    kubeseal
    jq
    postgresql
    fzf

    ntfs3g
  ];

  # Before 25.05
  # fonts.packages = with pkgs; [
  #   hack-font
  #   # Get nerdfonts override string from:
  #   # https://github.com/ryanoasis/nerd-fonts/tree/master/patched-fonts
  #   ( nerdfonts.override { fonts = [ "FiraCode" "Hack" "NerdFontsSymbolsOnly" ]; } )
  # ];

  # After 25.05
  fonts.packages = with pkgs; [
    hack-font
    nerd-fonts.fira-code
    nerd-fonts.hack
    nerd-fonts.symbols-only
  ];

  # nixpkgs.config.permittedInsecurePackages = [
  #   "mailspring-1.12.0"
  # ];
}
