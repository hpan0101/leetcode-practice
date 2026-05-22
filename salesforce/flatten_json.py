import json


class Solution:
    def flatten_dict(self, nested_dict, parent_key='', sep='.'):
        """
        Recursively flattens a nested dictionary.

        :param nested_dict: The dictionary to flatten.
        :param parent_key: The accumulated key path from higher levels.
        :param sep: The separator used to join nested keys.
        :return: A flat dictionary.
        """
        items = []
        for key, value in nested_dict.items():
            new_key = f"{parent_key}{sep}{key}" if parent_key else key

            if isinstance(value, dict):
                items.extend(self.flatten_dict(value, new_key, sep=sep).items())
            else:
                items.append((new_key, value))

        return dict(items)

    def flatten_json_to_string(self, json_str, sep='.'):
        """
        Takes a JSON string, flattens its internal nested structure,
        and outputs the result as a flat JSON string.
        """
        raw_data = json.loads(json_str)
        flat_data = self.flatten_dict(raw_data, sep=sep)
        return json.dumps(flat_data, indent=4)


# --- Example Usage ---
if __name__ == "__main__":
    input_json = """
    {
        "user": "Alice",
        "profile": {
            "age": 28,
            "address": {
                "city": "San Francisco",
                "zip": "94105"
            }
        },
        "status": "active"
    }
    """

    sol = Solution()

    print("--- Original Nested JSON ---")
    print(input_json)

    print("\n--- Flattened String Output ---")
    flat_string_output = sol.flatten_json_to_string(input_json, sep='.')
    print(flat_string_output)
