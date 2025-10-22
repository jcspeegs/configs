{ pkgs, ... }:
{
  environment.variables = { EDITOR = "vim"; };

  environment.systemPackages = with pkgs; [
    (vim-full.customize {
      vimrcConfig.packages.myplugins = with pkgs.vimPlugins; {
        start = [
          jedi-vim
          vim-airline
          vim-commentary
          vim-airline-themes
          tmuxline-vim
          vim-surround
          gruvbox
          fzf-vim
          vim-fugitive
          ale
          nerdtree
          # vim-nerdtree-syntax-highlight
          # vim-devicons
        ];
        opt = [];
      };

      vimrcConfig.customRC = builtins.readFile ./vimrc;
    })
  ] ++
  [(python3.withPackages (ps: with ps; [
      flake8
      flake8-bugbear
      flake8-docstrings
      pep8-naming
      flake8-quotes
  ]))] ++
  ( with python3Packages; [
      isort
      black
  ]);
}
