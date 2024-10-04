{
  description = "NixOS configuration";

  inputs = {
    nixpkgs.url = "nixpkgs/nixos-unstable";
    nixpkgs-stable.url = "nixpkgs/nixos-24.05";
    scripts.url = "github:jcspeegs/scripts";
    home-manager = {
      url = github:nix-community/home-manager;
      inputs.nixpkgs.follows = "nixpkgs";
    };
  };

  outputs = { self, nixpkgs, nixpkgs-stable, ... }@inputs:
  let
    system = "x86_64-linux";
    # overlay-stable = _: prev: {
    #   stable = nixpkgs-stable.legacyPackages.${prev.system};
    # };
    myMachine = custom: nixpkgs.lib.nixosSystem {
      inherit system;
      specialArgs = inputs // {inherit system; };
      modules = [
        custom
        ./configuration.nix
        # ({ config, pkgs, ... }: { nixpkgs.overlays = [ overlay-stable ]; })
      ];
    };
  in {
    nixosConfigurations = {
      lightshow = myMachine ./lightshow/lightshow.nix;
      tabby = myMachine ./tabby/tabby.nix;
    };
  };
}
