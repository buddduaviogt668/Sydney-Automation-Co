const { pathToRegexp } = require('path-to-regexp');

try {
  const keys = [];
  const regexp = pathToRegexp("/c-bus-programmer-:suburb((?!sydney$)[^/]+)", keys);
  console.log("Regex works:", regexp);
  console.log("Match sutherland:", regexp.exec("/c-bus-programmer-sutherland-shire"));
  console.log("Match sydney:", regexp.exec("/c-bus-programmer-sydney"));
} catch (e) {
  console.error("Error:", e.message);
}
