{ ... }: {
  networking.hostName = "tabby";
  environment.sessionVariables = rec { wifi_adapter = "wlp1s0"; };
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
