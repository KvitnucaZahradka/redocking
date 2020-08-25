## here I am keeping the default tmux name
tmux_session_name: "redocker"

## here I am keeping the default shell name
default_shell_name: "redocker.sh"

## here I am keeping the default shell path
default_shell_path: "/bin/bash"

## here I am keeping the allowed redocker names
redocker_names:
    - sf_gpu_nvidia_tf2
    - sf_gpu_google_tf22
    - sf_cpu_ubuntu_rasa

## here I am keeping the allowed registries
allowed_registries:
    - "local"
    - "None"
    - "catchthiscase.com"
    
## here I am keeping the required variables for every `redocker configuration`
required_variables:
    - "redocker_name"
    - "virtual_env"
    - "enforce_venv"
    - "docker_registry"
    - "docker_registry_tag"
    - "clean_image"
    - "image_postfix"