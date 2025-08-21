import re

def create_radiotherapy_dict(file_content):
    """
    Creates a dictionary from the provided text content, removing all dots and hyphens from the key,
    and correctly separating the key and value.

    Args:
        file_content: A string containing the text from the file.

    Returns:
        A dictionary with the formatted keys and values.
    """
    radiotherapy_dict = {}
    lines = file_content.strip().split('\n')
    for line in lines:
        # Use a regular expression to capture the numeric code and the description.
        # This pattern captures all digits, including the one after the hyphen, as the key.
        # The rest of the line is captured as the value.
        match = re.search(r'([\d\.]+)-(\d+)\s+-\s+(.+)', line)
        if match:
            # Group 1 is the part before the first hyphen, with dots.
            # Group 2 is the digit after the first hyphen.
            # Combine them and remove dots to form the final key.
            key = (match.group(1) + match.group(2)).replace('.', '')
            # Group 3 is the procedure description.
            value = match.group(3).strip()
            radiotherapy_dict[key] = value
        else:
            # Fallback for lines that don't match the regex exactly
            parts = line.split('-', 1)
            if len(parts) == 2:
                key = parts[0].strip().replace('.', '').replace('-', '')
                value = parts[1].strip()
                radiotherapy_dict[key] = value
    return radiotherapy_dict


with open('C:\\Users\\175 MX\\Documents\\Gustavo\\datasus\\data_rt_states\\states\\arquivos_auxiliares\\txt\\tabela_radioterapia.txt', 'r', encoding='utf-8') as f:
    file_content = f.read()

radiotherapy_procedures = create_radiotherapy_dict(file_content)

print(radiotherapy_procedures)