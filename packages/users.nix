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

  users.groups = {
    mlocate.gid = 50;
  };

  users.users = {
    guest = ( base_user { pw = "guest"; desc= "Guest User"; });

    ugflows = lib.mkMerge[
      ( base_user { pw = "ugflows"; desc = "Justin Speegle"; })
      { extraGroups = [ "wheel" ]; }
    ];
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
  };
}
