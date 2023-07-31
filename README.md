# Python Computer Assistant

Welcome to the Python Computer Assistant project! This project is a voice-controlled computer assistant built using Python. The assistant allows you to execute various commands using voice input and interact with your computer in a fun and convenient way.

## Prerequisites

Before running the Python Computer Assistant, make sure you have the following installed on your system:

- Python 3.x
- The required Python packages: `winsound`, `speech_recognition`, `pyautogui`, `requests`, `g4f`, `pyttsx3`, `ctypes`, `sys`, `sqlite3`, and `pygame`.

You can install the necessary packages using `pip`. For example:

```bash
pip install speech_recognition pyautogui requests g4f pyttsx3 pygame
```

Please note that some parts of the project might be platform-specific and tested on Windows. Adjustments may be needed for other operating systems.

## Getting Started

1. Clone this repository to your local machine.

```bash
git clone https://github.com/yourusername/python-computer-assistant.git
cd python-computer-assistant
```

2. Run the `main.py` file to start the Python Computer Assistant.

```bash
python main.py
```

## Features

### Voice Commands

The Python Computer Assistant currently supports the following voice commands:

- **Take a Screenshot:** Capture a screenshot of the current screen.

- **Live Write a Code:** Interactively write code based on your voice input. The code will be typed in real-time.

- **Write a Code:** Write code based on your voice input. The code will be saved to a text file and opened with Notepad.

- **Tell Me a Joke:** Get a random joke and display it in Notepad.

- **Search Something:** Perform a Google search for your specified query.

- **Google Search:** Perform a Google search for your specified query.

- **Chat:** Interact with a ChatGPT API. The assistant will open Notepad and display the generated response.

- **Close:** Close the currently active tab.

- **Connect Bluetooth:** Connect Bluetooth devices using the BluetoothConnect module.

- **Netflix Search:** Search for content on Netflix.

- **Netflix Login:** Log in to Netflix.

- **Netflix First:** Open the first Netflix show or movie.

### Additional Features

- **Text-to-Speech:** The assistant can read out responses using the `pyttsx3` library.

- **Database Integration:** Store executed commands in a local SQLite database for future use.

## Customize the Assistant

Feel free to modify the assistant to suit your needs. You can extend its capabilities by adding new voice commands or integrating with other APIs.

## License

This project is licensed under the MIT License. See the `LICENSE` file for details.

## Acknowledgments

- The project uses the g4f library for ChatGPT API integration.
- The `pyttsx3` library is used for text-to-speech functionality.

## Support

If you encounter any issues or have questions, please create an issue in the repository or contact the project maintainer at `your.email@example.com`.

---

Thank you for choosing the Python Computer Assistant! We hope this assistant will enhance your computer experience and make it more enjoyable and efficient. Happy coding!