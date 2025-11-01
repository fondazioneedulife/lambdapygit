{
  inputs = {
    flake-utils.url = "github:numtide/flake-utils";
    nixpkgs.url = "github:NixOS/nixpkgs/nixos-unstable";
  };

  outputs = { self, flake-utils, nixpkgs, ... }:
    flake-utils.lib.eachDefaultSystem (
      system: let
        pkgs = import nixpkgs { inherit system; };
      in {
        devShell = pkgs.mkShell {
          name = "lambdapygit_devenv";
          packages = (with pkgs; [
            basedpyright
            python3
            tinymist
            typst
          ]);
        };
      }
    );
}
