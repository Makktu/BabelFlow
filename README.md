# BabelFlow

A simple and elegant desktop application for generating text using OpenAI's GPT-2 model. Like the mythical Tower of Babel, it creates an endless stream of fascinating linguistic combinations. See the 'Why?' section for details...

## Features

- User-friendly graphical interface
- Real-time text generation
- Automatic saving of outputs to file
- Word wrapping and attractive formatting
- Cross-platform compatibility

## Installation

1. Make sure you have Python 3.7 or later installed
2. Install the required dependencies:
```bash
pip install -r requirements.txt
```

## Running BabelFlow

Simply run:
```bash
python chatgpt2_gui.py
```

On first run, the application will automatically download the GPT-2 model (approximately 500MB). This is a one-time process.

## Usage

1. Enter your prompt in the input box
2. Click "Generate" to create text
3. The generated text will appear in the output area and be saved to `output_gpt2.txt`
4. Use the "Clear" button to reset the output display

## Why BabelFlow? For Lovers of Experimental Literature, That's Why...

BabelFlow serves as a digital descendant of various experimental writing techniques, from the Dadaist cut-up method to James Joyce's stream-of-consciousness masterpiece "Finnegans Wake." Like these predecessors, it explores the boundaries between meaning and chaos, structure and fluidity.

BabelFlow's neural networks create text that often hovers in a fascinating space between coherence and abstraction. It can generate:

- Stream-of-consciousness narratives reminiscent of Joyce or Virginia Woolf
- Found poetry that emerges from seemingly random combinations
- Surrealist prose that challenges our expectations of language
- Linguistic experiments that blur the line between sense and nonsense

By providing different prompts, you can guide the model towards various styles of experimental writing. For instance:
- Abstract prompts ("blue dreams dissolving") tend to produce more poetic, dreamlike text
- Technical prompts often result in fascinating pseudo-academic babble
- Mixing different writing styles in your prompt can create interesting linguistic collisions

Whether you're a fan of experimental literature, a poet seeking inspiration, or simply curious about the boundaries of machine-generated text, BabelFlow offers a playground for linguistic exploration. It's like having a tireless collaborator who's read everything but understood it just slightly wrong - in the most interesting ways possible.

## Requirements

- Python 3.7+
- ~500MB disk space for the GPT-2 model
- Internet connection for first-time model download

## Dependencies

- torch
- transformers
- numpy
- tkinter (usually comes with Python)

## Creating a Desktop Shortcut

### On macOS
1. Open TextEdit and create a new file
2. Paste the following (replace the paths with your actual paths):
```bash
#!/bin/bash
cd "PATH_TO_APP_DIRECTORY"
python chatgpt2_gui.py
```
3. Save the file with a `.command` extension (e.g., `BabelFlow.command`)
4. Open Terminal and make the file executable:
```bash
chmod +x /path/to/BabelFlow.command
```
5. Drag the `.command` file to your desktop
6. Double-click to run!

### On Windows
1. Right-click on the desktop
2. Select New > Shortcut
3. Enter the command (replace paths as needed):
```
python "C:\Path\To\chatgpt2_gui.py"
```
4. Give it a name (e.g., "BabelFlow")
5. Right-click the shortcut > Properties
6. In "Start in", enter the path to your app directory
7. Optional: Click "Change Icon" to customize the look

### On Linux
1. Create a new file: `babelflow.desktop`
2. Add the following content (replace paths as needed):
```
[Desktop Entry]
Name=BabelFlow
Exec=python /path/to/chatgpt2_gui.py
Path=/path/to/app/directory
Type=Application
Terminal=false
```
3. Make it executable:
```bash
chmod +x babelflow.desktop
```
4. Move to desktop:
```bash
mv babelflow.desktop ~/Desktop/
```

## Requirements
- Python 3.7+
- ~500MB disk space for the GPT-2 model
- Internet connection for first-time model download

## Dependencies

- torch
- transformers
- numpy
- tkinter (usually comes with Python)
