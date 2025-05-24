# Contributing to Seraphine Translations

Thank you for your interest in helping with Seraphine's translations! This guide will help you understand how to contribute translations to the project.

## Translation Files

Seraphine uses Qt's translation system (`.ts` files) for UI translations and JSON files for game-related content. The translation files are located in:

- UI Translations: `app/resource/i18n/Seraphine.{locale}.ts`
- Game Modes: `app/resource/i18n/gamemodes.json`

Currently supported languages:
- English (en_US)
- Portuguese (pt_BR)
- Chinese Simplified (zh_CN)

## How to Add/Update Translations

### UI Translations (.ts files)

1. **File Structure**
   - Each translation file follows the Qt TS format
   - Files are named as `Seraphine.{locale}.ts` (e.g., `Seraphine.en_US.ts`)
   - Translations are organized by context (e.g., `ToolsTranslator`, `MainWindow`, `SettingInterface`)

2. **Adding New Translations**
   ```xml
   <context>
       <name>ContextName</name>
       <message>
           <location filename="../../path/to/source.py" line="123"/>
           <source>Original Text</source>
           <translation>Translated Text</translation>
       </message>
   </context>
   ```

3. **Best Practices**
   - Keep translations concise and natural
   - Maintain consistent terminology
   - Preserve any HTML tags in the original text
   - Test translations in the application

### Game Modes (gamemodes.json)

1. **File Structure**
   ```json
   {
       "Original Text": {
           "en": "English Translation",
           "pt": "Portuguese Translation"
       }
   }
   ```

2. **Adding New Translations**
   - Add entries for both English and Portuguese
   - Keep game mode names consistent with official League of Legends terminology
   - Use proper capitalization and formatting

## Translation Guidelines

1. **General Rules**
   - Use proper grammar and punctuation
   - Maintain consistent terminology across all translations
   - Keep translations natural and idiomatic
   - Preserve any special characters or formatting

2. **Game-Specific Terms**
   - Use official League of Legends terminology
   - Keep champion names in English
   - Use consistent translations for roles and game modes
   - Follow Riot Games' style guide for game terms

3. **Technical Terms**
   - Keep technical terms in English if no common translation exists
   - Use consistent translations for UI elements
   - Maintain proper capitalization

## Testing Translations

1. **Before Submitting**
   - Test translations in the application
   - Verify all strings are properly translated
   - Check for any formatting issues
   - Ensure no translation keys are missing

2. **Common Issues to Check**
   - Missing translations
   - Incorrect formatting
   - Inconsistent terminology
   - Grammar and spelling errors

## Submitting Changes

1. **Pull Request Process**
   - Create a new branch for your translations
   - Update only the necessary translation files
   - Include a clear description of changes
   - Reference any related issues

2. **Commit Messages**
   - Use clear, descriptive commit messages
   - Specify which language(s) were updated
   - Mention the type of changes (new translations, updates, fixes)

## Getting Help

If you need assistance with translations:
- Open an issue on GitHub
- Join our community discussions
- Reference the official League of Legends terminology

## Code of Conduct

Please be respectful and professional when contributing translations. We aim to maintain a welcoming and inclusive community for all contributors.

## License

By contributing translations, you agree that your contributions will be licensed under the project's [GPLv3 license](LICENSE). 