import js from '@eslint/js';
import globals from 'globals';

export default [
  js.configs.recommended,
  {
    files: ["**/*.js", "**/*.jsx"],
    ignores: ["node_modules/**", "eslint.config.mjs", ".vscode/**", "dist/**", ".next/**"],
    languageOptions: {
      globals: globals.browser,
      sourceType: 'module'
    },
    rules: {
      'no-undef': 'warn',           // Warn instead of error for globals like fbq
      'no-unused-vars': 'warn',
      'quote-props': ['error', 'as-needed'],  // 🔑 Catches unquoted keys!
      'semi': ['warn', 'always']
    }
  }
];
