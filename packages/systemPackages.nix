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
    mailspring
    numix-icon-theme
    numix-icon-theme-circle
    numix-icon-theme-square
    obs-studio
    pithos
    powerline
    # powerline-fonts
    tdesktop
    tree
    wget
  ];
}
