{ ... }: {
  networking.hostName = "lightshow";
  services.xserver.videoDrivers = [ "nvidia" ];
  imports = [ ./hardware-configuration.nix ];
}
