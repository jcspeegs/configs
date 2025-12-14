{ pkgs, ... }: {

  # # https://wiki.nixos.org/wiki/Python_quickstart_using_uv
  # # https://wiki.nixos.org/wiki/Python
  # programs.nix-ld.enable = true;

  # direnv mostly intended to be used with devenv
  # https://devenv.sh/automatic-shell-activation/
  programs.direnv.enable = true;

  environment.systemPackages = with pkgs; [
    # https://github.com/ajeetdsouza/zoxide
    zoxide
    apostrophe
    warp-terminal
    ttyd
    vhs
    glow
    gh
    claude-code
    devenv
    # uv
    video-trimmer
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
    tor-browser
    xorg.libpciaccess
    gimp
    git
    nautilus
    sushi
    gtop
    gvfs
    gnome.gvfs
    google-chrome
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
    telegram-desktop
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
