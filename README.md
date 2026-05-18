# LeetCode Practice

Python solutions to LeetCode problems, each with its own unit test.

## Setup

```bash
pip install -r requirements.txt
```

## Running Tests

```bash
# Run all tests
pytest

# Run tests for a specific problem
pytest test_0001_two_sum.py -v
```

## Cursor Editor Settings

### Disabling Autocomplete / Autofill

The following settings in `%APPDATA%\Cursor\User\settings.json` disable all code suggestions and autofill:

```json
"editor.inlineSuggest.enabled": false,
"cursor.completions.enabled": false,
"editor.quickSuggestions": { "other": false, "comments": false, "strings": false },
"editor.suggest.enabled": false,
"editor.parameterHints.enabled": false,
"editor.suggestOnTriggerCharacters": false,
"editor.wordBasedSuggestions": "off",
"editor.tabCompletion": "off",
"editor.suggest.preview": false,
"editor.suggest.showSnippets": false,
"editor.suggest.showKeywords": false,
"editor.acceptSuggestionOnEnter": "off",
"editor.hover.enabled": false,
"python.languageServer": "None",
"vsintellicode.features.python.intellicode": "disabled"
```

### Re-enabling Autocomplete

To turn autocomplete back on, remove the settings above (or flip them to their defaults) and reload the window via `Ctrl+Shift+P` → **Reload Window**. Key defaults to restore:

```json
"editor.inlineSuggest.enabled": true,
"cursor.completions.enabled": true,
"editor.quickSuggestions": { "other": "on", "comments": "off", "strings": "off" },
"editor.suggest.enabled": true,
"editor.parameterHints.enabled": true,
"editor.hover.enabled": true,
"python.languageServer": "Pylance"
```

## File Naming

Each problem gets two files:

- `p{number}_{name}.py` — solution (e.g. `p0001_two_sum.py`)
- `test_p{number}_{name}.py` — unit tests (e.g. `test_p0001_two_sum.py`)
