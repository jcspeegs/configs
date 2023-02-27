{ pkgs, ... }:
{
  environment.variables = { EDITOR = "vim"; };

  environment.systemPackages = with pkgs; [
    (vim-full.customize {
      vimrcConfig.packages.myplugins = with pkgs.vimPlugins; {
        start = [
          vim-airline
          vim-commentary
          vim-airline-themes
          tmuxline-vim
          vim-surround
          gruvbox
          fzf-vim
          vim-fugitive
          ale
        ];
        opt = [];
      };

      vimrcConfig.customRC = builtins.readFile ./vimrc;
    }
    )];
}
