{pkgs, ...}:{
  environment.systemPackages = with pkgs; [
    qtile
    arandr
    termite
  ];

  fonts.fonts = with pkgs; [
    hack-font
  ];

  services.xserver.windowManager.qtile.enable = true;
}
