{ lib, config, pkgs, home-manager, ... }:

let
  base_user = { pw, desc}: {
    isNormalUser = true;
    extraGroups = [ "networkmanager" ];
    password = pw;
    description = desc;
  };

in {
  imports = [ home-manager.nixosModule ];

  users.groups = {
    mlocate.gid = 50;
  };

  users.users = {
    guest = ( base_user { pw = "guest"; desc= "Guest User"; });

    ugflows = lib.mkMerge[
      ( base_user { pw = "ugflows"; desc = "Justin Speegle"; })
      { extraGroups = [ "wheel" ]; }
    ];

    jesse = ( base_user { pw = "jesse"; desc = "Jesse Speegle"; });
    jensen = ( base_user { pw = "jensen"; desc = "Jensen Speegle"; });
    lauren = ( base_user { pw = "lauren"; desc = "Lauren Speegle"; });
  };

  home-manager.users.ugflows = {
    home.stateVersion = "22.05";
    # https://github.com/NixOS/nixpkgs/issues/196651
    manual.manpages.enable = false;

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
  };
}
