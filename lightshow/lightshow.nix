{ ... }: {
  networking.hostName = "lightshow";
  services.xserver.videoDrivers = [ "nvidia" ];
  environment.sessionVariables = rec { wifi_adapter = "wlp0s20f0u4"; };
  imports = [ ./hardware-configuration.nix ];
}
