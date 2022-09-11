{ pkgs, ... }: {
  environment.interactiveShellInit = ( builtins.readFile ./alias ) +
  ''
    set -o vi
    source ${pkgs.powerline}/share/bash/powerline.sh
  ''
    ;
}
