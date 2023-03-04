{ ... }: {
  networking.hostName = "tabby";
  imports = [ ./hardware-configuration.nix ];
  
  services.xserver.libinput = {
    enable = true;

    touchpad = {
      naturalScrolling = true;
      disableWhileTyping = true;
      tappingButtonMap = "lrm";
    };
  };
}
