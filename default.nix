{ pkgs ? import
    (fetchTarball {
      name = "jpetrucciani-2025-06-29";
      url = "https://github.com/jpetrucciani/nix/archive/99daa58a9a5ef743962c37933fa047e6bfb3aa05.tar.gz";
      sha256 = "1597kqyb8ysxm55cpn04l2z87h7inj5dff50lrbb5kjq4y83vnsl";
    })
    { }
}:
let
  name = "lists-backend";

  uvEnv = pkgs.uv-nix.mkEnv {
    inherit name; python = pkgs.python313;
    workspaceRoot = pkgs.nix-gitignore.gitignoreSource [ ".git" ] ./.;
    pyprojectOverrides = final: prev: { };
  };

  tools = with pkgs; {
    cli = [
      jfmt
      nixup
    ];
    python = [
      black
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
