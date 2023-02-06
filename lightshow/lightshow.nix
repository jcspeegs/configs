{ ... }: {
  networking.hostName = "lightshow";
  imports = [ ./hardware-configuration.nix ];
}
