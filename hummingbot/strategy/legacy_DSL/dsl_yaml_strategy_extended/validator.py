import yaml
import argparse

# Import the necessary function from language.py
from language import main as parse_strategy


# def load_yaml(file_path):
#     try:
#         with open(file_path, 'r') as file:
#             return yaml.safe_load(file)
#     except FileNotFoundError:
#         print(f"File not found: {file_path}")
#         exit(1)
#     except yaml.YAMLError as exc:
#         print(f"Error parsing YAML: {exc}")
#         exit(1)


def validate_strategy(strategy):
    required_fields = ['name', 'type', 'author', 'description', 'markets']
    for field in required_fields:
        if not strategy.get(field):
            return {"valid": False, "message": f"Strategy {field} is missing"}

    # Validate strategy type
    valid_types = ['StrategyBase', 'Script', 'PMM', 'LM']
    if strategy['type'] not in valid_types:
        return {"valid": False, "message": f"Invalid strategy type: {strategy['type']}"}

    # Add more specific validations as needed
    return {"valid": True, "message": "Strategy is valid"}



def validate_market(market):
    if not market.get('connector'):
        return {"valid": False, "message": "Market connector is missing"}
    valid_connectors = ['binance', 'kucoin', 'ascent_ex', 'gate_io']
    if market['connector'] not in valid_connectors:
        return {"valid": False, "message": f"Invalid market connector: {market['connector']}"}

    if not market.get('pairs'):
        return {"valid": False, "message": "Market pairs are missing"}

    # Add more specific validations as needed
    return {"valid": True, "message": "Market is valid"}

def validate_parameter(parameter):
    required_fields = ['name', 'type', 'description', 'prompt_msg', 'default', 'keyword', 'dynamic_reconfigure', 'prompt_on_new']
    for field in required_fields:
        if field not in parameter:
            return {"valid": False, "message": f"Parameter {field} is missing"}

    valid_types = ['int', 'float', 'str', 'bool', 'list', 'dict']
    if parameter['type'] not in valid_types:
        return {"valid": False, "message": f"Invalid parameter type: {parameter['type']}"}

    # Add more specific validations as needed
    return {"valid": True, "message": "Parameter is valid"}

def save_yaml(strategy_dict, output_file_path):
    """
    Saves the validated strategy dictionary to a YAML file.
    """
    try:
        with open(output_file_path, 'w') as file:
            yaml.dump(strategy_dict, file)
        print(f"Validated strategy saved to: {output_file_path}")
    except Exception as e:
        print(f"Error saving file: {e}")


def main(file_path):
    # Use the parse_strategy function from language.py with the provided file path
    strategy = parse_strategy(file_path)
    if not strategy:
        print("Failed to parse strategy.")
        return None

    # Convert the strategy object to a dictionary for validation
    strategy_dict = strategy.to_dict()

    # Validate the parsed strategy
    strategy_result = validate_strategy(strategy_dict)
    if not strategy_result['valid']:
        print(f"Strategy validation failed: {strategy_result['message']}")
        return None

    # Validate each market
    for market in strategy_dict.get('markets', []):
        market_result = validate_market(market)
        print(f"Market validation: {market_result['message']}")

    # Validate each parameter
    for parameter in strategy_dict.get('parameters', []):
        parameter_result = validate_parameter(parameter)
        print(f"Parameter validation: {parameter_result['message']}")

    # Wrap the strategy_dict in a parent dictionary with 'strategy_model' as the key
    wrapped_strategy_dict = {'strategy_model': strategy_dict}

    # Save the validated strategy data to the new file
    base_name = file_path.rsplit('.', 1)[0]  # This removes the extension
    output_file_path = f"{base_name}_validated.yaml"
    save_yaml(wrapped_strategy_dict, output_file_path)
    return output_file_path


if __name__ == '__main__':
    parser = argparse.ArgumentParser(description="Validate a strategy YAML file")
    parser.add_argument('file_path', help="Path to the strategy YAML file")
    args = parser.parse_args()

    main(args.file_path)



