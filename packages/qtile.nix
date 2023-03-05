{pkgs, ...}:{
  environment.systemPackages = with pkgs; [
    betterlockscreen
    qtile
    dbus
    arandr
    ncpamixer
    pavucontrol
    termite
    xfce.thunar
    xfce.thunar-volman
    xfce.thunar-archive-plugin
    xfce.thunar-media-tags-plugin
  ];

  fonts.fonts = with pkgs; [
    hack-font
    # Get nerdfonts override string from:
    # https://github.com/ryanoasis/nerd-fonts/tree/master/patched-fonts
    (nerdfonts.override { fonts = [ "Hack" "NerdFontsSymbolsOnly"]; })
  ];

  services.xserver.windowManager.qtile.enable = true;
}
