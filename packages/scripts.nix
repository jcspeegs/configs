{ pkgs, scripts, system, ... }:
let
  tmux-sessionizer = scripts.packages.${system}.tmux-sessionizer;
in {
  nixpkgs.overlays = [
    (_: _: { inherit tmux-sessionizer; })
  ];
  environment.systemPackages = [
    pkgs.tmux-sessionizer
  ];
}
