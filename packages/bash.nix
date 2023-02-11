{ pkgs, lib, ... }: {
  programs.bash.interactiveShellInit =
    lib.strings.concatStringsSep "\n" [
      (builtins.readFile ./bashrc)
      (builtins.readFile ./alias)
      ''
        source ${pkgs.powerline}/share/bash/powerline.sh
      ''
    ];
}
