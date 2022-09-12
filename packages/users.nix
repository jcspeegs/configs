{ lib, config, pkgs, ... }:

let
  hm_uri = "https://github.com/nix-community/home-manager/archive/master.tar.gz";
  hm = builtins.fetchTarball hm_uri;
  base_user = { pw, desc}: {
    isNormalUser = true;
    extraGroups = [ "networkmanager" ];
    password = pw;
    description = desc;
  };

in {
  imports = [(import "${hm}/nixos")];

  users.users = {
    guest = ( base_user { pw = "guest"; desc= "Guest User"; });

    ugflows = lib.mkMerge[
      ( base_user { pw = "ugflows"; desc = "Justin Speegle"; })
      { extraGroups = [ "wheel" ]; }
    ];
  };

  home-manager.users.ugflows = {
    home.stateVersion = "22.05";

    programs.tmux = {
      enable = true;
      extraConfig = builtins.readFile ./tmux.conf;
    };

    programs.git = {
      enable = true;
      userEmail = "justin@speegs.com";
    };
  };
}
