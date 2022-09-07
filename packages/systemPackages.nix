{ pkgs, ... }: {

  environment.systemPackages = with pkgs; [
    curl
    discourse
    firefox
    git
    google-chrome
    gnome.gnome-tweaks
    gparted
    htop-vim
    mailspring
    numix-icon-theme
    numix-icon-theme-square
    numix-icon-theme-circle
    pithos
    powerline
    # powerline-fonts
    tdesktop
    tree
    wget
  ];
}
