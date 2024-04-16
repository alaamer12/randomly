import functools

def automatic_fixer(func):  # or name it ensure_file_exists
    @functools.wraps(func)
    def wrapper(*args, **kwargs):
        try:
            return func(*args, **kwargs)
        except FileNotFoundError:
            # If the file is not found, create an empty file
            file_path = args[0]
            with open(file_path, 'w') as file:
                file.write('')
            print(f"File not found. Created an empty file: {file_path}")
            # Retry the original function after fixing the issue
            return func(*args, **kwargs)
        except Exception as e:
            # In case of any other exception, log and return None
            print(f"Error: {e}")
            return None
    return wrapper

@automatic_fixer
def process_file(file_path):
    with open(file_path, 'r') as file:
        content = file.read()
        # Assume some processing logic here
        result = content.upper()
    return result

# print(type(automatic_fixer))
if __name__ == '__main__':
    # file_path = 'test.txt'
    # result = process_file(file_path)
    # print(result)
    pass