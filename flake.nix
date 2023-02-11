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

  outputs = { self, nixpkgs, home-manager, ... }@inputs:
  let system = "x86_64-linux"; in {
    nixosConfigurations = {
      lightshow = nixpkgs.lib.nixosSystem {
        inherit system;
        specialArgs = inputs // { inherit system; };
        modules = [
          lightshow/lightshow.nix
          ./configuration.nix
        ];
      };
      tabby = nixpkgs.lib.nixosSystem {
        inherit system;
        specialArgs = inputs // { inherit system; };
        modules = [
          tabby/tabby.nix
          ./configuration.nix
        ];
      };
    };
  };
}
