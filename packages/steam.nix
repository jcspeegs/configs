{ ... }: {
  packages.steam = {
    enable = true;
    remotePlay.openFirewall = true;
    locallNetworkGameTransfers.openFirewall = true;
  };

  # nixpkgs.config.allowUnfreePredicate = pkg: builtins.elem (lib.getName pkg) [
  #   "steam"
  #   "steam-original"
  #   "steam-runtime"
  # ];

}
