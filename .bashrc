# If not running interactively, don't do anything
[[ $- != *i* ]] && return

set -o vi

not_base_os() { [[ $HOSTNAME != 'rgb-dt' ]] && $@ ; }
exist_run() { [[ -f "$1" ]] && source "$1" ; }

# Export environment variables
export EDITOR='vim'
export VISUAL='vim'
export HISTCONTROL=ignoreboth:erasedups
export PAGER='less'
not_base_os export PAGER='most'
# Fix transparent background when openning vim inside screen
export TERM=screen-256color

# Update PATH
prepend_path () { [[ -d "$1" ]] && export PATH="$1":$PATH ; }
append_path () { [[ -d "$1" ]] && export PATH=$PATH:"$1" ; }
prepend_path ~/scripts
prepend_path ~/.local/bin

# Personal aliases
[[ -f $HOME/.alias ]] && . $HOME/.alias

#ignore upper and lowercase when TAB completion
bind "set completion-ignore-case on"

#shopt
shopt -s autocd # change to named directory
shopt -s cdspell # autocorrects cd misspellings
shopt -s cmdhist # save multi-line commands in history as single line
shopt -s dotglob
shopt -s histappend # do not overwrite history
shopt -s expand_aliases # expand aliases

# Powerline
not_base_os powerline-daemon -q
POWERLINE_BASH_CONTINUATION=1
POWERLINE_BASH_SELECT=1
not_base_os exist_run /usr/share/powerline/bindings/bash/powerline.sh
not_base_os exist_run /usr/share/powerline/bash/powerline.sh

# # ex = EXtractor for all kinds of archives
# # usage: ex <file>
ex ()
{
  if [ -f $1 ] ; then
    case $1 in
      *.tar.bz2)   tar xjf $1   ;;
      *.tar.gz)    tar xzf $1   ;;
      *.bz2)       bunzip2 $1   ;;
      *.rar)       unrar x $1   ;;
      *.gz)        gunzip $1    ;;
      *.tar)       tar xf $1    ;;
      *.tbz2)      tar xjf $1   ;;
      *.tgz)       tar xzf $1   ;;
      *.zip)       unzip $1     ;;
      *.Z)         uncompress $1;;
      *.7z)        7z x $1      ;;
      *.deb)       ar x $1      ;;
      *.tar.xz)    tar xf $1    ;;
      *.tar.zst)   tar xf $1    ;;
      *)           echo "'$1' cannot be extracted via ex()" ;;
    esac
  else
    echo "'$1' is not a valid file"
  fi
}

# FZF
export FZF_DEFAULT_OPTS="--multi --height=50% --info=inline --reverse --preview='[[ \$(file --mime {}) =~ binary ]] && echo {} is a binary file || (bat {} || cat {}) 2> /dev/null | head -300' --preview-window='right:hidden:99%:wrap' --bind='f3:execute(bat {} || less -f {}),f2:toggle-preview,ctrl-d:half-page-down,ctrl-u:half-page-up,ctrl-a:select-all+accept,ctrl-y:execute-silent(echo {+} | pbcopy)'"
FD_OPTIONS="--follow --exclude .git"
export FZF_DEFAULT_COMMAND="fd --type f --type l --hidden $FD_OPTIONS"
export FZF_CTRL_T_COMMAND="fd --hidden $FD_OPTIONS"
export FZF_ALT_C_COMMAND="fd --type d --hidden $FD_OPTIONS"

export BAT_PAGER="less -R"

# https://wiki.archlinux.org/index.php/Fzf
# source /usr/share/fzf/key-bindings.bash
# source /usr/share/fzf/completion.bash

parse_git_branch() {
	    git branch 2> /dev/null | sed -e '/^[^*]/d' -e 's/* \(.*\)/(\1)/'
    }
PS1='[\!]\[\033[01;36m\]\u@\H:\[\033[01;34m\]\w\[\e[91m\]$(parse_git_branch)\[\033[01;34m\]\$\[\033[00m\] '

# reporting tools - install when not installed
# [[ $HOSTNAME != 'rgb-dt' ]] && neofetch
not_base_os neofetch
#screenfetch
#alsi
#paleofetch
#fetch
#hfetch
#sfetch
#ufetch
#ufetch-arco
#pfetch
#sysinfo
#sysinfo-retro
#cpufetch
#colorscript random
