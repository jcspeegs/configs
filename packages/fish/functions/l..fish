function l. --wraps=ls --description "listing of dotfiles"
    ls -A $argv | grep -E "^\."
end
