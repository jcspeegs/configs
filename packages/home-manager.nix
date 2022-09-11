{ config, pkgs, ... }:

let
  hm_uri = "https://github.com/nix-community/home-manager/archive/master.tar.gz";
  hm = builtins.fetchTarball ${hm_uri};

in {
  imports = [(import "${hm}/nixos")];

  home-manager.users.ugflows = {
  };
}
