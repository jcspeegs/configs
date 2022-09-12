{ ... }:

{
  programs.tmux = {
    enable = true;
    extraConfig = builtins.readFile ./tmux_airline;
    # extraConfig = builtins.readFile ./tmux.conf
    #   + builtins.readFile ./tmux_airline;
  };
}
