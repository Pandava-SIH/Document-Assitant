import re

def fill_legal_document(user_document_text, user_details, legal_document_template):
    """
    Fill in user details from their document into a legal document template.

    Args:
        user_document_text (str): Text extracted from the user's document.
        user_details (dict): User-specific details to be filled into the legal document.
        legal_document_template (str): Template of the legal document with placeholders.

    Returns:
        str: The filled legal document.
    """
    # Define regular expressions to identify placeholders in the template.
    placeholder_pattern = r'\{[(\w+)]\}'  # Placeholder format: {placeholder_name}

    # Find all placeholders in the template.
    placeholders = re.findall(placeholder_pattern, legal_document_template)

    # Initialize the filled document with the template.
    filled_document = legal_document_template

    # Iterate through placeholders and fill in user details.
    for placeholder in placeholders:
        if placeholder in user_details:
            # Replace the placeholder with the corresponding user detail.
            filled_document = filled_document.replace(f'{{{placeholder}}}', user_details[placeholder])
        else:
            print(f"Warning: Placeholder '{placeholder}' not found in user details.")

    return filled_document