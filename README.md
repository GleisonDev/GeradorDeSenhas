# Password Generator Application

This application is a simple yet effective password generator built using Python and several key libraries. It provides a user-friendly graphical interface to generate strong and secure passwords.

## Technologies Used

* **Python:** The core programming language used for the entire application.
* **PySimpleGUI:** A graphical user interface (GUI) library that simplifies the creation of desktop applications. It allows for easy design and implementation of the application's interface.
* **random:** A Python built-in module used to generate cryptographically strong random numbers, essential for creating secure passwords.
* **pygame:** A cross-platform set of Python modules designed for writing video games. In this application, it's used for audio playback, adding a fun and interactive element.
* **threading:** A Python module used to implement multithreading, allowing for concurrent execution of tasks, such as playing audio without blocking the main application.

## How to Use

1.  **Installation:**
    * Ensure you have Python installed on your system.
    * Install the required libraries using pip:
        * `pip install PySimpleGUI pygame`
2.  **Running the Application:**
    * Execute the Python script (`password_gen.py`).
    * The application window will appear, presenting fields to set the site name, user name, and the desire amount of characters that the password will have.
    * Click the "Gerar Senha" button to generate a new password.
    * The generated password will be displayed in the output area.
    * The password will be saved in a file named `senhas.txt` in the same directory as the script.
    * The application will also play a sound when it starts, and it will keep playing until you close the window.
3.  **Exiting the Application:**
    * Close the application window to stop the audio playback and exit the program.

## Features

* Generates strong, random passwords.
* Allows users to specify the length of the password.
* Saves generated passwords to a text file.
* Plays background audio that loops until the application is closed.

## Contributing

Feel free to contribute to this project by submitting pull requests or opening issues for bug reports or feature requests.

## License

This project is licensed under the MIT License.
