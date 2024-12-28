import tkinter as tk
from tkinter import ttk, filedialog, scrolledtext, messagebox
from main import summarize_document, chat_with_model,  chat_with_upload_document

# Function to create the chat window
def open_chat_window(root, pre_filled_message=None):
    chat_window = tk.Toplevel(root)
    chat_window.title("Chat with Helix - Esq")
    chat_window.state("zoomed")
    chat_window.configure(bg='#1e1e2e')

    # Responsive layout
    chat_window.rowconfigure(0, weight=1)  # Chat display section
    chat_window.rowconfigure(1, weight=0)  # Input section
    chat_window.columnconfigure(0, weight=1)

    # Chat Display
    chat_display = scrolledtext.ScrolledText(
        chat_window,
        wrap=tk.WORD,
        bg='#282a36',
        fg='white',
        font=('Helvetica', 14),
        state='disabled',
        padx=15,
        pady=10,
        relief='flat'
    )
    chat_display.grid(row=0, column=0, sticky="nsew", padx=15, pady=15)

    input_frame = tk.Frame(chat_window, bg='#1e1e2e')
    input_frame.grid(row=1, column=0, sticky="ew", padx=15, pady=15)
    input_frame.columnconfigure(0, weight=1)  # Upload button
    input_frame.columnconfigure(1, weight=1)  # Spacing before Send button
    input_frame.columnconfigure(2, weight=1)  # Send button
    input_frame.columnconfigure(3, weight=1)  # Spacing after Send button
    input_frame.columnconfigure(4, weight=1)  # Delete Chat button

    # User Input Text Box
    user_input = tk.Text(
        input_frame,
        height=3,
        font=('Helvetica', 12),
        bg='#2d2d3e',
        fg='white',
        insertbackground='white',
        wrap=tk.WORD,
        relief='flat',
        highlightthickness=1,
        highlightbackground="#3e3e4e",
        highlightcolor="#5e5e7e",
        padx=10,
        pady=10
    )
    user_input.grid(row=0, column=0, columnspan=5, sticky="ew", padx=(10, 10), pady=(10, 5))

    # Upload Document Button
    def upload_document():
        file_path = filedialog.askopenfilename(filetypes=[("Word Documents", "*.docx")])
        chat_window.lift()
        chat_window.focus_force()
        if file_path:
            insert_text('model', f"🤖 Helix - Esq: Reading Document ...\n\n")
            response = chat_with_upload_document(file_path)
            insert_text('model', f"🤖 Helix - Esq: {response}\n\n")
        chat_window.lift()
        chat_window.focus_force()
    upload_btn = ttk.Button(
        input_frame, text="Upload Document", command=upload_document, style="Send.TButton"
    )
    upload_btn.grid(row=1, column=0, sticky="n", padx=(0, 10), pady=5)

    # Send Button
    send_btn = ttk.Button(input_frame, text="Send", command=lambda: send_message(), style="Send.TButton")
    send_btn.grid(row=1, column=2, sticky="n", padx=10, pady=5)

    # Clear Chat Button
    def clear_chat():
        chat_display.configure(state='normal')
        chat_display.delete("1.0", tk.END)
        chat_display.configure(state='disabled')

    clear_chat_btn = ttk.Button(
        input_frame, text="Delete Chat", command=clear_chat, style="Send.TButton"
    )
    clear_chat_btn.grid(row=1, column=4, sticky="n", padx=(10, 0), pady=5)

    # Function to insert text into chat display
    def insert_text(tag, text):
        chat_display.configure(state='normal')
        chat_display.insert(tk.END, text, tag)
        chat_display.configure(state='disabled')
        chat_display.see(tk.END)

    # Handle sending a message
    def send_message():
        user_text = user_input.get("1.0", tk.END).strip()
        if user_text:
            insert_text('user', f"🧑‍💻 You: {user_text}\n\n")
            response = chat_with_model(user_text)
            insert_text('model', f"🤖 Helix - Esq: {response}\n\n")
            user_input.delete("1.0", tk.END)
        else:
            messagebox.showwarning("Chat", "Please enter a message.")

    # Tags for chat display
    chat_display.tag_configure('user', foreground='#FFB74D', font=('Helvetica', 14, 'bold'))
    chat_display.tag_configure('model', foreground='#5dc9f8', font=('Helvetica', 14, 'italic'))

    # Pre-filled message handling
    if pre_filled_message:
        insert_text('user', f"🧑‍💻 You: Summarize this document...\n\n")
        insert_text('model', f"🤖 Helix - Esq: {pre_filled_message}\n\n")

    # Footer Section for Branding
    footer_label = ttk.Label(
        chat_window,
        text="✨ Powered by Helix - Your AI Legal Assistant ✨",
        background="#1e1e2e",
        foreground="#FFB74D",
        font=('Helvetica', 12, 'italic')
    )
    footer_label.grid(row=2, column=0, pady=(0, 15), sticky="ew")

# Main GUI
def create_gui():
    root = tk.Tk()
    root.title("Helix - Esq")
    root.state("zoomed")  # Open main window in full-screen mode
    root.configure(bg='#1e1e2e')

    style = ttk.Style()
    style.theme_use("clam")
    style.configure('TFrame', background='#1e1e2e')
    style.configure('TLabel', background='#1e1e2e', foreground='white', font=('Helvetica', 24, 'bold'))
    style.configure('TButton', font=('Helvetica', 14, 'bold'), padding=10, relief='flat')
    style.map('TButton', background=[('active', '#5e5e7e'), ('!active', '#3e3e4e')], foreground=[('!disabled', 'white')])

    main_frame = ttk.Frame(root)
    main_frame.pack(expand=True)

    # Title Label
    title_label = ttk.Label(
        main_frame,
        text="🔹 Welcome to Helix - Esq 🔹",
        style='TLabel',
        anchor="center",
        foreground="#FFB74D"
    )
    title_label.grid(row=0, column=0, pady=(30, 10), padx=20)

    # Subtitle Label
    subtitle_label = ttk.Label(
        main_frame,
        text="\t    Your AI-Powered Legal Advisor & Assistant\nProviding Smart Document Summaries and Personalized Guidance",
        font=('Helvetica', 14, 'italic'),
        foreground="white"
    )
    subtitle_label.grid(row=1, column=0, pady=(0, 30), padx=20)

    # Start Chatting Button
    start_chatting_btn = ttk.Button(
        main_frame,
        text="💬 Start Chatting",
        command=lambda: open_chat_window(root)
    )
    start_chatting_btn.grid(row=2, column=0, pady=10, padx=20, sticky='ew')

    # Summarize Documents Button
    def summarize_docs():
        file_path = filedialog.askopenfilename(filetypes=[("Word Documents", "*.docx")])
        if file_path:
            pre_filled_message = summarize_document(file_path)  # Get the summary
            open_chat_window(root, pre_filled_message=pre_filled_message)

    summarize_docs_btn = ttk.Button(
        main_frame,
        text="📄 Summarize Documents",
        command=summarize_docs
    )
    summarize_docs_btn.grid(row=3, column=0, pady=10, padx=20, sticky='ew')

    # Version Information Section
    version_info = ttk.Label(
        main_frame,
        text=(
            "🌟 **What's New in Helix - Esq 1.0?** 🌟\n"
            "• Advanced Document Summarization\n"
            "• Refined User Experience with a Modern Interface\n"
            "• Reliable AI-Powered Legal Assistance\n\n"
            "   Stay tuned for exciting updates and features!"
        ),
        wraplength=800,
        font=('Helvetica', 12),
        justify="center",
        background='#1e1e2e',
        foreground='#cecedf'
    )
    version_info.grid(row=4, column=0, pady=(30, 10), padx=20)

    root.mainloop()

if __name__ == "__main__":
    create_gui()
