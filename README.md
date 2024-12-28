# Your AI-Powered Legal Assistant

This is an advanced AI-driven legal assistant designed to help users interact with legal documents, ask questions, and receive intelligent responses. With an intuitive GUI built using Python's Tkinter library, Helix provides a seamless chat-based experience for document analysis and legal queries.

## Features

### 1. **Interactive Chat Interface**
- A responsive and user-friendly GUI for real-time interaction.
- Chat functionality for legal assistance, including:
  - Question answering.
  - Document summarization.
  - General legal queries.

### 2. **Document Upload and Analysis**
- Upload Word documents (.docx) for analysis.
- Extract and summarize key information.
- AI-powered responses tailored to document content.

### 3. **Advanced AI Model Integration**
- Powered by the Llama language model.
- Dynamically loads the AI model from the `LLM model` directory.

### 4. **Customizable Chat Settings**
- Clear chat functionality.
- Responsive UI elements with hover and animation effects.

### 5. **Lightweight and Scalable Design**
- Modular codebase for easy maintenance and scalability.
- Integrated with advanced backend processing for AI tasks.

## Installation

### Prerequisites
- Python 3.8+
- Required Python packages:
  - `tkinter`
  - `numpy`
  - `llama` (or your specific model package)
  - `python-docx`

### Steps
1. Clone the repository:
   ```bash
   git clone https://github.com/asghar-rizvi/AI-LLM-with-GUI-Python
   cd AI-LLM-with-GUI-Python
   ```
2. Install required dependencies:
   ```bash
   pip install -r requirements.txt
   ```
3. Place your AI model file in the `LLM model` directory.
   - Ensure there is only one model file in the directory.

4. Run the application:
   ```bash
   python main.py
   ```

## Usage

1. Launch the application using the above command.
2. Interact with the chat interface for queries or document analysis:
   - Type your query and click "Send".
   - Upload a document using the "Upload Document" button.
3. Review the AI responses in the chat display.
4. Use the "Delete Chat" button to clear the conversation.

## Code Structure

- **`main.py`**: Contains the core functionality for AI model interaction and document processing.
- **`gui.py`**: Handles the GUI creation and user interactions.
- **`utils.py`**: Contains utility functions for file handling and data processing.
- **`LLM model/`**: Directory for storing the AI model file.
- **`assets/`**: Contains any required static assets like icons or additional resources.

## How It Works

1. **Chat with AI**:
   - Messages are processed in `chat_with_model()`.
   - AI responses are displayed in the chat interface.
2. **Document Analysis**:
   - Upload a document via the "Upload Document" button.
   - The `chat_with_upload_document(file_path)` function processes the document and provides a summary or analysis.
3. **Dynamic Model Loading**:
   - The `get_model_path()` function identifies the AI model file dynamically from the `LLM model` directory.

## Future Enhancements

- Add support for additional document formats (PDF, TXT).
- Enhance the AI model's capabilities for legal-specific tasks.
- Introduce multi-language support for global accessibility.

## License

This project is licensed under the [MIT License](LICENSE).

---

> **Note**: This project is intended for educational and experimental purposes. Ensure compliance with applicable laws and ethical guidelines when using AI for legal assistance.

---

Start your AI-powered legal journey today!!!

