{ pkgs ? import
    (fetchTarball {
      name = "jpetrucciani-2025-06-27";
      url = "https://github.com/jpetrucciani/nix/archive/bb9791c111e63120a095189ca79c7321e15571ae.tar.gz";
      sha256 = "0xyahy0dz3jw6whb5fqzbg1120inxpqwhb04ph3ad81gjlx29hhx";
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
