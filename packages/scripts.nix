{ pkgs, scripts, system, ... }: {
  nixpkgs.overlays = [
    scripts.overlays.tmux-sessionizer
  ];
  environment.systemPackages = [
    pkgs.tmux-sessionizer
  ];
}
