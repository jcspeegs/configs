function nupf --description "Update flake, rebuild nixos, activate the new generation, and make it the default boot entry"
    set -l config /home/ugflows/builds/configs
    set -l host (prompt_hostname)
    nix flake update --commit-lock-file $config
    sudo nixos-rebuild switch --flake $config#$host
end
