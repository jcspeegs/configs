{ pkgs, lib, ... }: {
  programs.bash.interactiveShellInit =
    lib.strings.concatStringsSep "\n" [
      (builtins.readFile ./alias)
      (builtins.readFile ./.bashrc)
      ''
        source ${pkgs.powerline}/share/bash/powerline.sh
      ''
    ];
}
