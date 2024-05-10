function fish_user_key_bindings --description "Set key bindings"
    # ctrl-p pianobar
    bind \cp "guake --show -e 'tmux-sessionizer pianobar pianobar'"

    # ctrl-f tmux session
    bind \cf "tmux-sessionizer"

    # fzf
    # https://nixos.wiki/wiki/Fzf
    if command -s fzf-share >/dev/null
        source (fzf-share)/key-bindings.fish
    end
    fzf_key_bindings
end
