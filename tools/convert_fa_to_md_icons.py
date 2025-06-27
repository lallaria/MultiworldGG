#!/usr/bin/env python3
"""
Script to convert fa_icons.py format to md_icons dictionary format.

The fa_icons.py file contains lines like:
0xF2FB line
0xF2FC lock_open
0xF2FD lyft

The md_icons format is a dictionary like:
md_icons.update({
    "flag-checkered": "\\uf11e",
    "treasure-chest": "\\udb81\\udf26",
    "search-location": "\\ueede",
})
"""

import re
import os


def convert_hex_to_unicode_escape(hex_code):
    """
    Convert a hex code like '0xF2FB' to a Unicode escape sequence like '\\uf2fb'
    """
    # Remove the '0x' prefix and convert to lowercase
    hex_value = hex_code[2:].lower()
    
    # Convert to Unicode escape sequence
    # For codes <= 0xFFFF, use \u
    # For codes > 0xFFFF, use \U (but we'll handle as surrogate pairs)
    code_point = int(hex_value, 16)
    
    if code_point <= 0xFFFF:
        return f"\\u{hex_value}"
    else:
        # For codes > 0xFFFF, we need to use surrogate pairs
        # This is more complex and might need special handling
        return f"\\u{hex_value}"


def parse_fa_icons_file(file_path):
    """
    Parse the fa_icons.py file and extract icon mappings.
    
    Returns a dictionary with icon names as keys and hex codes as values.
    """
    icon_mappings = {}
    
    try:
        with open(file_path, 'r', encoding='utf-8') as file:
            for line_num, line in enumerate(file, 1):
                line = line.strip()
                
                # Skip empty lines
                if not line:
                    continue
                
                # Match pattern: 0xXXXX icon_name
                match = re.match(r'^0x([0-9A-Fa-f]+)\s+(\w+)$', line)
                if match:
                    hex_code = f"0x{match.group(1)}"
                    icon_name = match.group(2)
                    icon_mappings[icon_name] = hex_code
                else:
                    print(f"Warning: Could not parse line {line_num}: {line}")
    
    except FileNotFoundError:
        print(f"Error: File '{file_path}' not found.")
        return {}
    except Exception as e:
        print(f"Error reading file: {e}")
        return {}
    
    return icon_mappings


def generate_md_icons_dict(icon_mappings, output_file=None):
    """
    Generate md_icons dictionary format from icon mappings.
    
    Args:
        icon_mappings: Dictionary with icon names as keys and hex codes as values
        output_file: Optional file path to write the output to
    """
    # Convert to md_icons format
    md_icons_entries = []
    
    for icon_name, hex_code in icon_mappings.items():
        unicode_escape = convert_hex_to_unicode_escape(hex_code)
        md_icons_entries.append(f'    "{icon_name}": "{unicode_escape}",')
    
    # Sort entries alphabetically for consistency
    md_icons_entries.sort()
    
    # Generate the complete dictionary
    output_lines = [
        "# Converted from fa_icons.py",
        "# Format: md_icons.update({",
        "#     \"icon-name\": \"\\uXXXX\",",
        "# })",
        "",
        "md_icons.update({"
    ]
    
    output_lines.extend(md_icons_entries)
    output_lines.append("})")
    
    output_text = "\n".join(output_lines)
    
    if output_file:
        try:
            with open(output_file, 'w', encoding='utf-8') as file:
                file.write(output_text)
            print(f"Successfully wrote {len(icon_mappings)} icons to '{output_file}'")
        except Exception as e:
            print(f"Error writing to file: {e}")
    else:
        print(output_text)
    
    return output_text


def main():
    """Main function to run the conversion."""
    # Path to the fa_icons.py file
    fa_icons_path = "data/gui/kivydi/fa_icons.py"
    
    # Output file path (optional)
    output_path = "converted_md_icons.py"
    
    print("Converting fa_icons.py to md_icons format...")
    print(f"Input file: {fa_icons_path}")
    print(f"Output file: {output_path}")
    print("-" * 50)
    
    # Parse the fa_icons file
    icon_mappings = parse_fa_icons_file(fa_icons_path)
    
    if not icon_mappings:
        print("No icons found or error occurred during parsing.")
        return
    
    print(f"Found {len(icon_mappings)} icons to convert.")
    
    # Generate the md_icons format
    generate_md_icons_dict(icon_mappings, output_path)
    
    print("-" * 50)
    print("Conversion complete!")
    print(f"You can now copy the contents of '{output_path}' to your md_icons dictionary.")


if __name__ == "__main__":
    main() 