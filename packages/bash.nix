{ pkgs, lib, ... }: {
  programs.bash = {
    interactiveShellInit = lib.strings.concatStringsSep "\n" [
      (builtins.readFile ./bashrc)
      (builtins.readFile ./alias)
      ''
        # source ${pkgs.powerline}/share/bash/powerline.sh
      ''
    ];

    shellAliases = {
      ll = "ls -lrtaFh";
      l = "ls";
    };
  };

  environment.systemPackages = [ pkgs.starship ];
  programs.starship.enable = true;
  # Nerd font symbols
  # programs.starship.settings = builtins.fromTOML (builtins.readFile ./starship.toml);
}
