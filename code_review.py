"""
Email Validator Utility

This module provides an EmailValidator class for validating and normalizing email addresses.

Usage:
  validator = EmailValidator()
  if validator.validate(email):
    normalized_email = validator.normalize(email)
"""

import re # The 're' module is imported but not used
# Use 're' to perform comprehensive email validation

class EmailValidator:
  # Add a docstring for the class explaining its purpose.
  def validate(self, email):
    """Validates an email address."""
    # The current validation is very basic and doesn't conform to email standards
    # Use regular expression to validate the email according to RFC 5322 standard
    if not isinstance(email, str):
      raise ValueError("Email must be a string")
    if "@" not in email:
      return False
    # Splitting the email without handling multiple '@' signs will raise an error
    localpart, domain = email.split("@")
    if len(localpart) < 1 or len(localpart) > 64:
      return False
    # Validate the domain using DNS lookups  
    return True

  def normalize(self, email):
    """Normalizes an email address."""
    # remove leading/trailing whitespace
    email = email.strip()
    
    # remove dots from localpart
    localpart, domain = email.split("@")
    # Removing dots from the local part can change the email address
    # The replace method doesn't modify the string in place
    # Assign the result back to 'localpart'
    localpart.replace(".", "")

    # convert domain to lowercase
    normalized = f"{localpart}@{domain.lower()}"
    return normalized

# Consider using a well-tested library like 'email_validator' for validation and normalization
# This reduces the risk of bugs and non-compliance with email standards and allow to add additional specific validations easily

if __name__ == "__main__":
  validator = EmailValidator()
  
  emails = [
    "alice@example.com",
    "bob.smith@example.com",
    "invalid.email",
    "toolonglocalpartxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxx@example.com",
    "   carol@example.com   "
    # Add more test cases to identify issues like:
      # - multiple '@',
      # - domain validation, 
      # - domain with top-level-domain and
      # - invalid domain format and spaces in local part
  ]

  for email in emails:
    if validator.validate(email):
      print(f"Valid: {email}")
      normalized = validator.normalize(email)
      print(f"Normalized: {normalized}")
    else:
      print(f"Invalid: {email}")
      # Provide feedback on why the email is invalid to help users correct it