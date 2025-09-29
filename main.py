import utils

def main(**kwargs):
    func = kwargs.get("func")
    params = kwargs.get("params", {})
    
    if not func:
        print("No function provided.")
        return
    if not hasattr(utils, func):
        print(f"Function '{func}' not found in utils module.")
        return
    if not isinstance(params, dict):
        print("Params should be a dictionary.")
        return
    try:
        function_to_call = getattr(utils, func)
        result = function_to_call(*params.values())
        print(f"Result: {result}")
    except Exception as error:
        print(f"An error occurred: {error}")

if __name__ == "__main__":
    
    while True:
        print('Enter "exit" to quit.')
        user_input = input('Enter function name: ').lower()
        if user_input == "exit": break
        params = {}
        params['var1'] = input('Enter value for var1: ')
        if params['var1'] == 'exit': break
        params['var2'] = input('Enter value for var2: ')
        if params['var2'] == 'exit': break
        
        main(func=user_input, params=params)

    print("Script executed successfully.")
