{ pkgs ? import
    (fetchTarball {
      name = "jpetrucciani-2025-06-28";
      url = "https://github.com/jpetrucciani/nix/archive/48e138e7880999ef8aa1a1804a43bbbf64fdfddd.tar.gz";
      sha256 = "02jlrdn831mjzaiwvpgz5gbxyddc9cq364nbvdx7dvf7w72l15pl";
    })
    { }
}:
let
  name = "lists";


  tools = with pkgs; {
    cli = [
      jfmt
      nixup
      redis
    ];
    java = [
      maven
      zulu
    ];
    scripts = pkgs.lib.attrsets.attrValues scripts;
  };

  scripts = with pkgs; { };
  paths = pkgs.lib.flatten [ (builtins.attrValues tools) ];
  env = pkgs.buildEnv {
    inherit name paths; buildInputs = paths;
  };
in
(env.overrideAttrs (_: {
  inherit name;
  NIXUP = "0.0.9";
})) // { inherit scripts; }
