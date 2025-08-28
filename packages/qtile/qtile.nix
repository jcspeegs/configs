{lib, pkgs, ...}:
# with pkgs.python3Packages;
# let iwlib = callPackage ./iwlib.nix {};
# in {
{
  # nixpkgs.overlays = [
  #   ( self: super: {
  #     qtile-unwrapped = super.qtile-unwrapped.overrideAttrs ( old: rec {
  #       propagatedBuildInputs = old.propagatedBuildInputs
  #         ++ [ /*iwlib*/ python-box pyyaml numpy ]
  #       ;
  #       pythonImportsCheck = [ "iwlib" "box" "yaml" "numpy" ];
  #     });
  #   })
  # ];

  environment.systemPackages = with pkgs;[
      (python3.withPackages (p: with p; [ numpy ]))
      betterlockscreen
      dunst
      arandr
      ncpamixer
      lm_sensors
      networkmanagerapplet
      pavucontrol
      termite
      picom
      # picom-jonaburg
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

    # https://github.com/NixOS/nixpkgs/blob/nixos-unstable/nixos/modules/services/x11/window-managers/qtile.nix
    services.xserver.windowManager.qtile = {
      enable = true;

      # extraPackages = python3Packages: with python3Packages; [
      extraPackages = p: with p; [
        qtile-extras
        python-box
        pyyaml
        iwlib
      ];
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
