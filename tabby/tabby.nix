{ ... }: {
  networking.hostName = "tabby";
  imports = [ ./hardware-configuration.nix ];
}
