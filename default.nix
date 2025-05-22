{ pkgs ? import
    (fetchTarball {
      name = "jpetrucciani-2025-05-22";
      url = "https://github.com/jpetrucciani/nix/archive/bd0d0e3171ca5472efbd5c1b1fc259b114df142f.tar.gz";
      sha256 = "0h49vqd570sjmqrl0sa54nkw1wkzi3drhjkyfspmx8n1a8xl4mr7";
    })
    { }
}:
let
  name = "groceries";

  uvEnv = pkgs.uv-nix.mkEnv {
    inherit name; python = pkgs.python313;
    workspaceRoot = ./.;
    pyprojectOverrides = final: prev: { };
  };

  tools = with pkgs; {
    cli = [
      jfmt
      nixup
    ];
    uv = [ uv uvEnv ];
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
} // uvEnv.uvEnvVars)) // { inherit scripts; }
