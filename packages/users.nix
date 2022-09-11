{ config, pkgs, ... }:

let
  hm_uri = "https://github.com/nix-community/home-manager/archive/master.tar.gz";
  hm = builtins.fetchTarball hm_uri;

in {
  imports = [(import "${hm}/nixos")];

  users.users.test = {
    isNormalUser = true;
    extraGroups = [ "netorkmanager" ];
  };
  home-manager.users.test = {
    home.stateVersion = "22.05";
    programs.tmux = {
      extraConfig = builtins.readFile ./tmux_airline;
    };
  };
  
  users.users.ugflows = {
    isNormalUser = true;
    description = "Justin Speegle";
    extraGroups = [ "networkmanager" "wheel" ];
  };

  home-manager.users.ugflows = {
    home.stateVersion = "22.05";
    programs.tmux = {
      extraConfig = builtins.readFile ./tmux.conf
        + builtins.readFile ./tmux_airline;
    };

    programs.git = {
      enable = true;
      userEmail = "justin@speegs.com";
    };
  };
}
