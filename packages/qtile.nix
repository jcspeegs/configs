{pkgs, ...}:{
  environment.systemPackages = with pkgs; [
    qtile
  ];

  services.xserver.windowManager.qtile.enable = true;
}
