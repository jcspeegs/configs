{pkgs, ...}:
  # Build iwlib for use with Wlan widget
let iwlib = with pkgs; python3.pkgs.buildPythonPackage rec {
  pname = "iwlib";
  version = "1.7.0";
  src = fetchPypi {
    inherit pname version;
    sha256 = "a805f6597a70ee3001aba8f039fb7b2dcb75dc15c4e7852f5594fd6379196da1";
  };
  
  doCheck = false;
  propagatedBuildInputs = [ pkgs.wirelesstools pkgs.python3Packages.cffi ];
};
in {
  nixpkgs.overlays = [
    ( self: super: {
      qtile = super.qtile.unwrapped.override ( old: rec {
        propagatedBuildInputs = old.propagatedBuildInputs ++ [ iwlib ];
        pythonImportsCheck = [ "iwlib" ];
      });
    })
  ];

  environment.systemPackages = with pkgs; [
      betterlockscreen
      qtile
      # dbus
      dmenu
      arandr
      ncpamixer
      lm_sensors
      networkmanagerapplet
      pavucontrol
      termite
      rofi
      rofi-vpn
      rofi-power-menu
      rofi-file-browser
      xfce.thunar
      xfce.thunar-volman
      xfce.thunar-archive-plugin
      xfce.thunar-media-tags-plugin
    # (python310.withPackages my-python-packages)
  ];

  fonts.fonts = with pkgs; [
    hack-font
    # Get nerdfonts override string from:
    # https://github.com/ryanoasis/nerd-fonts/tree/master/patched-fonts
    (nerdfonts.override { fonts = [ "Hack" "NerdFontsSymbolsOnly"]; })
  ];

  services.xserver.windowManager.qtile.enable = true;
  services.picom.enable = true;

  environment.sessionVariables = rec {
    XDG_SESSION_DESKTOP  = "qtile";
  };
}
