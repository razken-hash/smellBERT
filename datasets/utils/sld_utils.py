import hashlib


def get_file_hash(file_path, hash_algorithm='sha256'):
    hash_func = hashlib.new(hash_algorithm)

    with open(file_path, 'rb') as file:
        while chunk := file.read(8192):
            hash_func.update(chunk)

    return hash_func.hexdigest()


def verify_file_hash(file, original_hash):
    return original_hash == get_file_hash(file)


def create_instance_item(code_smells, class_code):
    return {
        "Code Smells": code_smells,
        "Class Code": class_code
    }
