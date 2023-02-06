{
  description = "NixOS configuration";

  inputs = {
    nixpkgs.url = "nixpkgs/nixos-unstable";

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
          specialArgs = inputs;
          modules = [
            lightshow/lightshow.nix
            ./configuration.nix
          ];
        };
        tabby = nixpkgs.lib.nixosSystem {
          inherit system;
          specialArgs = { inherit inputs; };
          modules = [
            tabby/tabby.nix
            ./configuration.nix
          ];
        };
      };
    };
}
