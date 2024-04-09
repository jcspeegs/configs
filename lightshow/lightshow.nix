{ ... }: {
  networking.hostName = "lightshow";

  services.xserver.videoDrivers = [ "nvidia" ];
  # https://nixos.wiki/wiki/Nvidia
  hardware.nvidia = {
    modesetting.enable = true;
    powerManagement.enable = false;
    open = false;
    nvidiaSettings = true;
  };

  environment.sessionVariables = rec { wifi_adapter = "wlp0s20f0u3u2"; };
  imports = [ ./hardware-configuration.nix ];
}
