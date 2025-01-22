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

  # fileSystems."/home/ugflows/mnt/data" = {
  # # fileSystems."/data" = {
  #   mountPoint = "/home/ugflows/mnt/data";
  #   device = "/dev/disk/by-uuid/afe055a1-b9d8-4be9-a1b8-2313fc6bc267";
  #   # fsType = "ext4";
  #   # options = [
  #   #   "defaults"
  #   #   "nofail"
  #   #   "uid=1000"
  #   #   "user"
  #   #   "gid=100"
  #   # ];
  # };

  imports = [ ./hardware-configuration.nix ];
}
