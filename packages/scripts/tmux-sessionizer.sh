path=${1:-$(find ~ -mindepth 1 -maxdepth 1 -type d | fzf)}
name=$(basename "$path" | tr . _)
pid=$(pgrep tmux)
cmd=$2

# Tmux not running
if [[ -z $TMUX ]] && [[ -z $pid ]]; then
    tmux new-session -s $name -c $path $cmd
    exit 0
fi

# Tmux running, session name does not exist
if ! tmux has-session -t=$name 2>/dev/null ; then
    echo 'inside1'
    tmux new-session -ds $name -c $path $cmd
fi

# Tmux running, session name exists, 
tmux switch-client -t $name 2>/dev/null || tmux attach -t $name
