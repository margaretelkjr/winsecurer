# WinSecurer

WinSecurer is a simple Python tool designed to enhance file security by adding password protection to any Windows directory. It allows users to lock directories with a password, making them hidden and inaccessible without the correct password.

## Features

- **Lock a Directory:** Hide and protect any directory with a password.
- **Unlock a Directory:** Restore access to the directory with the correct password.

## Requirements

- Windows Operating System
- Python 3.x

## Installation

1. Clone the repository:

   ```bash
   git clone https://github.com/yourusername/winsecurer.git
   ```

2. Navigate to the directory:

   ```bash
   cd winsecurer
   ```

## Usage

1. Run the program:

   ```bash
   python WinSecurer.py
   ```

2. Follow the on-screen instructions to lock or unlock a directory.

## Security Notice

- The program uses SHA-256 hashing to store passwords securely, but it does not encrypt the directory contents. It only hides the directory to prevent casual access.
- Ensure to remember your password as there is no password recovery mechanism.

## License

This project is licensed under the MIT License. See the [LICENSE](LICENSE) file for details.

## Contributing

Contributions are welcome. Please open an issue or submit a pull request on GitHub.

## Acknowledgments

- Inspired by the need for simple directory protection on Windows systems.
- Utilizes Python's built-in libraries for hashing and Windows API calls.