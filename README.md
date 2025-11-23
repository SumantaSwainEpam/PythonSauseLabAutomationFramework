# Sauce Demo POM Automation Framework

This project is a comprehensive automation testing framework built using the Python Pytest framework, applying the Page Object Model (POM) design pattern for the [Sauce Demo](https://www.saucedemo.com/) web application. The framework integrates advanced utilities for browser management, reporting, logging, screenshot capture, and YAML-based test data management to enable scalable and maintainable end-to-end web UI testing.

## Features

- **Page Object Model:** All web page elements and actions are organized, encapsulated, and reusable across multiple test cases.
- **Multi-Browser Support:** Ability to run tests on various browsers by specifying the browser at runtime.
- **Advanced HTML Reporting:** Automatically generates timestamped HTML test reports with detailed logs and embedded screenshots for failed tests.
- **Centralized Logging:** Uniform logging system with dedicated Loggers directory for debugging and traceability.
- **Automatic Screenshot Capture:** Screenshots are taken automatically on test failures and stored in a dedicated screenshots directory.
- **YAML Configuration Management:** Test data and configuration managed through YAML files for easy maintenance.
- **Data-Driven Testing:** Utilities for reading and managing test data from external sources.
- **Login Helper Utilities:** Specialized utilities for authentication workflows.
- **Flexible Configuration:** Easily configure test parameters such as browser choice from the command line.
- **Organized Test Artifacts:** Each test execution generates timestamped reports with logs and screenshots in structured directories.
- **Scalability:** Ready for easy extension with new page objects, tests, and business workflows.



