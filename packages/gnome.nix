{ pkgs, ... }: {

  # Enable the GNOME Desktop Environment.
  services.xserver = {
    displayManager.gdm.enable = true;
    desktopManager.gnome.enable = true;
  };

  environment.systemPackages = with pkgs; [
    gnome-tweaks
  ];

  # Exclude default gnome apps
  environment.gnome.excludePackages = (with pkgs; [
    gnome-photos
    gnome-tour
    epiphany
    geary
    totem
    gnome-music
  ]);
  # ]) ++ (with pkgs.gnome; [
  #   gnome-music
  #   # gedit
  # ]);

  # services.xserver.desktopManager.gnome.extraGSettingsOverrides = ''
  # [org/gnome/desktop/interface]
  # color-scheme='prefer-dark'
  # font-antialiasing='grayscale'
  # font-hinting='slight'
  # '';
}
