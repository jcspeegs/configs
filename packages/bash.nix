{ pkgs, ... }: {
  environment.interactiveShellInit = ( builtins.readFile ./alias ) +
    '' source ${pkgs.powerline}/share/bash/powerline.sh ''
    ;
}
