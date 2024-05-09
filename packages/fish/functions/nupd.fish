function nupd --description "Rebuild nixos, activate the new generation, and make it the default boot entry (without updating flake)"
    set -l config /home/ugflows/builds/configs
    set -l host (prompt_hostname)
    sudo nixos-rebuild switch --flake $config#$host
end
