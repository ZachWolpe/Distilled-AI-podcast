"""
---------------------------------------------------------------------------
prompt_engine.py

Reusable methods.

: zachcolinwolpe@gmail.com
: 12.12.24
---------------------------------------------------------------------------
"""
import argparse
import yaml


def write_to_file(text, path):
    """Writes the given text to a file at the specified path."""
    with open(path, 'w') as file:
        file.write(text)


def read_script(path_to_script):
    with open(path_to_script, 'r') as file:
        script_content = file.read()
    return script_content


def parse_runtime_yaml(yaml_path):
    """Parses the runtime YAML file and returns the configuration."""
    with open(yaml_path, 'r') as file:
        return yaml.safe_load(file)


# path_to_yml='./src/runtime.yml'
def load_yaml_config_from_argparse():
    parser = argparse.ArgumentParser(description="Parse runtime YAML configuration.")
    parser.add_argument('--yaml_path', '-y', type=str, default='./runtime.yml', help='Path to the runtime YAML file')
    args = parser.parse_args()
    config = parse_runtime_yaml(args.yaml_path)
    return config


if __name__ == "__main__":
    print('---->>> EXAMPLE <<<----')
    config = load_yaml_config_from_argparse()
    print('config::\n\n')
    print(config)
    print(config['stage_1_generate_script_from_pdf'].keys())
    print('\n\n')
