{lib, pkgs, ...}:
with pkgs.python3Packages;
# let iwlib = callPackage ./iwlib.nix {};
# in {
{
  nixpkgs.overlays = [
    ( self: super: {
      qtile-unwrapped = super.qtile-unwrapped.overrideAttrs ( old: rec {
        propagatedBuildInputs = old.propagatedBuildInputs
          ++ [ iwlib python-box pyyaml ]
        ;
        pythonImportsCheck = [ "iwlib" "box" "yaml" ];
      });
    })
  ];

  environment.systemPackages = with pkgs;[
      betterlockscreen
      stable.qtile
      dunst
      arandr
      ncpamixer
      lm_sensors
      networkmanagerapplet
      pavucontrol
      termite
      picom-jonaburg
      rofi
      rofi-vpn
      rofi-power-menu
      rofi-file-browser
      xfce.thunar
      xfce.thunar-volman
      xfce.thunar-archive-plugin
      xfce.thunar-media-tags-plugin
    ]
    ;

    services.xserver.windowManager.qtile = {
      enable = true;
      # Use stable overlay
      package = pkgs.stable.qtile;
    };

  # https://man.archlinux.org/man/picom.1#CONFIGURATION_FILES
  # services.picom = {
  #   enable = true;
  #   vSync = false;
  #   fade = true;
  #   inactiveOpacity = 0.95;
  #   settings = {
  #     # frame-opacity = 0.85;
  #     corner-radius = 15;
  #   };
  # };

  environment.sessionVariables = rec {
    XDG_SESSION_DESKTOP  = "qtile";
  };
}
