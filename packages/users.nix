{lib, config, pkgs, home-manager, ... }:

let
  base_user = { description, initialHashedPassword}: {
    isNormalUser = true;
    extraGroups = [ "networkmanager" ];
    inherit description initialHashedPassword;
  };

in {
  imports = [ home-manager.nixosModule ];

  users.groups = {
    mlocate.gid = 50;
  };

  users.users = {
    ugflows = base_user {
      description = "Justin Speegle";
      initialHashedPassword = "$y$j9T$SDE34MFtSI.HSD2HUPI9/.$yWvN51QE6EXe.509RO09Wjzk4c81IuHgChBo/EIEjh4"; } //
      { extraGroups = [ "wheel" ]; };

    jesse = base_user {
      description = "Jesse Speegle";
      initialHashedPassword = "$y$j9T$0DwfegL.74k4/8y33qh021$FyAAEw1trxviRjJbVyH3TNTbFnDGTFeUrAPOk/Qb.O6";
    };

    jensen = base_user {
      description = "Jensen Speegle";
      initialHashedPassword = "$y$j9T$M0kvGW2qIeM.jQjvLNchm0$vd7tnp8REDJNjPf70LpyoERrCenyllt4OsTIRgOHBI1";
    };

    lauren = base_user {
      description = "Lauren Speegle";
      initialHashedPassword = "$y$j9T$xNHI2KNDVbTUq5JtWwAkv.$GZ2ItUCejAQ7Qo4UwDfMEwAA5ErPhFneXSyQcAJxRpA";
    };
  };

  home-manager.users.ugflows = {
    home.stateVersion = "22.05";
    # https://github.com/NixOS/nixpkgs/issues/196651
    # manual.manpages.enable = false;

    programs.tmux = {
      enable = true;
      extraConfig = builtins.readFile ./tmux.conf;
    };

    programs.git = {
      enable = true;
      userEmail = "justin@speegs.com";
    };

    xdg.configFile."pianobar/config".source = ./pianobar.conf;
    xdg.configFile."qtile/config.py".source = qtile/config.py;
    xdg.configFile."qtile/scripts".source = qtile/scripts;
    xdg.configFile."termite/config".source = termite/config;
    xdg.configFile."bat/config".source = bat/config;
  };
}
