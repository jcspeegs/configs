with import <nixpkgs> {}; 
with builtins;
let
tmux-sessionizer = writeShellApplication {
  name = "ts";
  runtimeInputs = [ tmux ];
  text = readFile ./scripts/tmux-sessionizer.sh;
};
in {
  environment.systemPackages = [
    tmux-sessionizer
  ];
}
