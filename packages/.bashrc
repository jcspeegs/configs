set -o vi

# fzf key-bindings
if command -v fzf-share >/dev/null; then
    source "$(fzf-share)/key-bindings.bash"
    source "$(fzf-share)/completion.bash"
fi

# fzf
export FZF_DEFAULT_OPTS='--height 50% --layout=reverse --border --preview="[[ \$(file --mime {}) =~ binary ]] && echo {} is a binary file || cat {} | head -300" --bind="F2:toggle-preview,ctrl-d:half-page-down,ctrl-u:half-page-up" --no-mouse --multi --preview-window="hidden:wrap"'

# C-n Nixos config editing session
bind '"":"/etc/nixos/packages/scripts/tmux-sessionizer.sh /etc/nixos \"vim configuration.nix\"\n"'
# C-p pianobar session
bind '"":"/etc/nixos/packages/scripts/tmux-sessionizer.sh pianobar pianobar\n"'
