{ config, pkgs, ... }:

{
  imports =
    [ ./hardware-configuration.nix
      ./packages/systemPackages.nix
      ./packages/vim.nix
      ./packages/tmux.nix
      ./packages/bash.nix
    ];

  # Bootloader.
  boot.loader.systemd-boot.enable = true;
  boot.loader.efi.canTouchEfiVariables = true;
  boot.loader.efi.efiSysMountPoint = "/boot/efi";

  networking.hostName = "nixos";
  networking.networkmanager.enable = true;

  # Enables wireless support via wpa_supplicant.
  # networking.wireless.enable = true;

  time.timeZone = "America/Los_Angeles";
  i18n.defaultLocale = "en_US.utf8";

  # Enable the X11 windowing system.
  services.xserver.enable = true;

  # Configure keymap in X11
  services.xserver = {
    layout = "us";
    xkbVariant = "";
  };

  # Enable the GNOME Desktop Environment.
  services.xserver.displayManager.gdm.enable = true;
  services.xserver.desktopManager.gnome.enable = true;

  # Enable CUPS to print documents.
  services.printing.enable = true;

  # Enable sound with pipewire.
  sound.enable = true;
  hardware.pulseaudio.enable = false;
  security.rtkit.enable = true;
  services.pipewire = {
    enable = true;
    alsa.enable = true;
    alsa.support32Bit = true;
    pulse.enable = true;
    #jack.enable = true;

    # use the example session manager (no others are packaged yet so this is enabled by default,
    # no need to redefine it in your config for now)
    #media-session.enable = true;
  };

  # Enable touchpad support (enabled default in most desktopManager).
  # services.xserver.libinput.enable = true;

  # Define a user account. Don't forget to set a password with ‘passwd’.
  users.users.ugflows = {
    isNormalUser = true;
    description = "Justin Speegle";
    extraGroups = [ "networkmanager" "wheel" ];
  };

  # Allow unfree packages
  nixpkgs.config.allowUnfree = true;

		  # Some programs need SUID wrappers, can be configured further or are
		  # started in user sessions.
		  # programs.mtr.enable = true;
		  # programs.gnupg.agent = {
		  #   enable = true;
		  #   enableSSHSupport = true;
		  # };

		  # List services that you want to enable:

		  # Enable the OpenSSH daemon.
		  # services.openssh.enable = true;

		  # Open ports in the firewall.
		  # networking.firewall.allowedTCPPorts = [ ... ];
		  # networking.firewall.allowedUDPPorts = [ ... ];
		  # Or disable the firewall altogether.
		  # networking.firewall.enable = false;

		  # This value determines the NixOS release from which the default
		  # settings for stateful data, like file locations and database versions
		  # on your system were taken. It‘s perfectly fine and recommended to leave
		  # this value at the release version of the first install of this system.
		  # Before changing this value read the documentation for this option
		  # (e.g. man configuration.nix or on https://nixos.org/nixos/options.html).
		  system.stateVersion = "22.11"; # Did you read the comment?

}
