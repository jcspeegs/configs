{pkgs, ...}:{
  environment.systemPackages = with pkgs; [
    betterlockscreen
    qtile
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
  ];

  services.xserver.windowManager.qtile.enable = true;
}
