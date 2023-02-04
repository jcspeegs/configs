{ pkgs, ... }:
{
  environment.variables = { EDITOR = "vim"; };

  environment.systemPackages = with pkgs; [
    ((vim_configurable.override { }).customize {
      name = "vim";
      vimrcConfig.packages.myplugins = with pkgs.vimPlugins; {
        start = [
          vim-airline
          vim-commentary
          vim-airline-themes
          tmuxline-vim
          vim-surround
          gruvbox
          fzf-vim
        ];
        opt = [];
      };

      vimrcConfig.customRC = builtins.readFile ./vimrc;
    }
    )];
}
