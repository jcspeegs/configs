if status is-interactive
    fish_vi_key_bindings
    set -u fish_greeting

    # FZF
    # set -x FZF_DEFAULT_OPTS_FILE "/home/ugflows/.config/fzfrc"
    set -x FZF_DEFAULT_OPTS '
        --height 50%
        --layout=reverse
        --border
        --preview="[[ \$(file --mime {}) =~ binary ]] && echo {} is a binary file || cat {} | head -300"
        --bind="F2:toggle-preview,ctrl-d:half-page-down,ctrl-u:half-page-up"
        --no-mouse
        --multi
        --preview-window="hidden:wrap
    '

    # Starship
    starship init fish | source
end
