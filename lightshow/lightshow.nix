{ config, ... }: {
  networking.hostName = "lightshow";

  services.xserver.videoDrivers = [ "nvidia" ];
  # https://nixos.wiki/wiki/Nvidia
  hardware.nvidia = {
    package = config.boot.kernelPackages.nvidiaPackages.stable;
    modesetting.enable = true;
    powerManagement.enable = false;
    powerManagement.finegrained = false;
    open = false;
    nvidiaSettings = true;
  };

  environment.sessionVariables = rec { wifi_adapter = "wlp0s20f0u3u2"; };
  imports = [ ./hardware-configuration.nix ];

  fileSystems."/home/ugflows/mnt/data" = {
    device = "/dev/desk/by-uuid/d935e28a-867f-49ae-acd0-1f26b27a163c";
    fsType = "ext4";
    options = [
      "defaults"
      "nofail"
    ];
  };
}
