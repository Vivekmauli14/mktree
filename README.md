# mktree

**mktree** is a command-line utility that allows users to create directory structures and files from structured text files, JSON, or XML formats. It is compatible with all Unix-based systems and supports setting file permissions during creation.

## Features

- Create directory structures and files from structured text, JSON, or XML files.
- Supports specifying file permissions during creation.
- Compatible with all Unix-based systems.
- Easy to use with a simple command-line interface.
- Debugging options to help users understand the creation process.

## Installation via GitHub Releases

You can easily install `mktree` by downloading the precompiled binary from the GitHub Releases page. Follow these steps to set it up:

1. **Download the Release:**
   - Go to the [mktree Releases page](https://github.com/Vivekmauli14/mktree/releases) on GitHub.
   - Find the latest release and download the appropriate binary for your operating system (e.g., `mktree-linux`, `mktree-macos`).

2. **Make the Binary Executable:**
   Open your terminal and navigate to the directory where you downloaded the binary. Run the following command to make it executable:
   ```bash
   chmod +x mktree

3. Verify the Installation
   To ensure mktree is installed correctly, run the following command:

  ```bash
     mktree --help
  ```

## Contributing

If you'd like to contribute to `mktree`, please follow these guidelines:

1. **Fork the Repository**: Click on the "Fork" button at the top right of the repository page.
2. **Create a Feature Branch**: Create a new branch for your feature or bug fix.

## Future Development Features

Here are a few features that could be developed further:

- **Support for YAML file structures**: Expand the tool to read and interpret YAML files for directory structure creation.
- **Improved Error Handling**: Enhance error messages for better user guidance in case of issues.
- **Interactive Mode**: Implement an interactive mode for users to create directory structures on the fly.
- **Configuration Options**: Add configuration options to customize file and directory permissions during creation.
