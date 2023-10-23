{ pkgs }: {
  deps = [
    pkgs.python39Packages.pip
    pkgs.neofetch
		pkgs.nodePackages.prettier
  ];
}