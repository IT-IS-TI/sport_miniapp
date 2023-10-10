module.exports = {
  testEnvironment: 'jsdom', 
    testMatch: ['**/__tests__/**/*.js?(x)', '**/?(*.)+(spec|test).js?(x)'], // Patterns for searching test files
    moduleFileExtensions: ['js', 'jsx', 'json', 'node'], // File extensions that can be imported in tests
  transform: {
      '^.+\\.jsx?$': 'babel-jest', // Use Babel to transpilate JavaScript and JSX
  },
    setupFilesAfterEnv: ['./setupTests.js'], // Files, 
    coveragePathIgnorePatterns: ['/node_modules/'], // Ignore coverage for files from node_modules
  moduleNameMapper: {
      '\\.(css|less|scss)$': 'identity-obj-proxy', // Stub for importing CSS modules
  },
};