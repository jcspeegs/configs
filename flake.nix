{
  description = "NixOS configuration";

  inputs = {
    nixpkgs.url = "nixpkgs/nixos-unstable";
    scripts.url = "github:jcspeegs/scripts";
    home-manager = {
      url = github:nix-community/home-manager;
      inputs.nixpkgs.follows = "nixpkgs";
    };
  };

  outputs = { self, nixpkgs, ... }@inputs:
  let
    system = "x86_64-linux";
    myMachine = custom: nixpkgs.lib.nixosSystem {
      inherit system;
      specialArgs = inputs // {inherit system; };
      modules = [ custom ./configuration.nix ];
    };
  in {
    nixosConfigurations = {
      lightshow = myMachine ./lightshow/lightshow.nix;
      tabby = myMachine ./tabby/tabby.nix;
    };
  };
}
