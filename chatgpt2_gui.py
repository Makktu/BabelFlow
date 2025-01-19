import tkinter as tk
from tkinter import ttk, scrolledtext, messagebox
from transformers import pipeline
import torch
import os
import threading
import time

class GPT2App:
    def __init__(self, root):
        self.root = root
        self.root.title("BabelFlow - a GPT-2 Text Generator")
        self.root.geometry("800x900")  # Made taller to accommodate new controls
        
        # Initialize the model
        self.initialize_model()
        
        # Initialize default parameters
        self.params = {
            'temperature': 0.2,
            'max_length': 250,
            'min_length': 50,
            'top_k': 40,
            'top_p': 0.95,
            'repetition_penalty': 1.2,
        }
        
        # Create GUI elements
        self.create_widgets()
        
    def initialize_model(self):
        os.environ["TOKENIZERS_PARALLELISM"] = "false"
        try:
            device = 0 if torch.cuda.is_available() else -1
            self.generator = pipeline("text-generation", model="gpt2", device=device)
            self.model_info = f"Model: {self.generator.model.name_or_path} | Device: {self.generator.device}"
        except Exception as e:
            messagebox.showerror("Error", f"Failed to initialize model: {str(e)}")
            self.root.quit()
            
    def create_widgets(self):
        # Configure a custom font
        self.custom_font = ('Arial', 14)  # 4pt bigger than default
        self.output_font = ('Arial', 14)
        
        # Model info label
        self.info_label = ttk.Label(self.root, text=self.model_info, font=self.custom_font)
        self.info_label.pack(pady=10)
        
        # Settings frame
        settings_frame = ttk.LabelFrame(self.root, text="Generation Settings", padding=(10, 5))
        settings_frame.pack(padx=20, pady=5, fill="x")
        
        # Create settings controls
        self.create_settings_controls(settings_frame)
        
        # Input frame
        input_frame = ttk.LabelFrame(self.root, text="Input", padding=(10, 5))
        input_frame.pack(padx=20, pady=5, fill="x")
        
        self.prompt_entry = scrolledtext.ScrolledText(input_frame, height=4, font=self.custom_font, wrap=tk.WORD)
        self.prompt_entry.pack(padx=10, pady=5, fill="x")
        
        # Controls frame
        controls_frame = ttk.Frame(self.root)
        controls_frame.pack(padx=20, pady=5, fill="x")
        
        self.generate_button = ttk.Button(controls_frame, text="Generate", command=self.generate_text)
        self.generate_button.pack(side="left", padx=5)
        
        self.clear_button = ttk.Button(controls_frame, text="Clear", command=self.clear_output)
        self.clear_button.pack(side="left", padx=5)
        
        # Output frame
        output_frame = ttk.LabelFrame(self.root, text="Output", padding=(10, 5))
        output_frame.pack(padx=20, pady=5, fill="both", expand=True)
        
        self.output_text = scrolledtext.ScrolledText(
            output_frame,
            font=self.output_font,
            wrap=tk.WORD,  # Enable word wrapping
            padx=10,       # Internal padding
            pady=5
        )
        self.output_text.pack(padx=10, pady=5, fill="both", expand=True)
        
        # Status bar
        self.status_var = tk.StringVar()
        self.status_bar = ttk.Label(self.root, textvariable=self.status_var, font=self.custom_font)
        self.status_bar.pack(pady=10)
        
    def create_settings_controls(self, parent):
        # Create a frame for each row of controls
        controls_frame = ttk.Frame(parent)
        controls_frame.pack(fill="x", padx=5, pady=5)
        
        # Length controls
        length_frame = ttk.LabelFrame(controls_frame, text="Length Controls", padding=(5, 5))
        length_frame.pack(side="left", fill="x", expand=True, padx=5)
        
        ttk.Label(length_frame, text="Min Length:").grid(row=0, column=0, padx=5)
        self.min_length = ttk.Entry(length_frame, width=8)
        self.min_length.insert(0, str(self.params['min_length']))
        self.min_length.grid(row=0, column=1, padx=5)
        
        ttk.Label(length_frame, text="Max Length:").grid(row=0, column=2, padx=5)
        self.max_length = ttk.Entry(length_frame, width=8)
        self.max_length.insert(0, str(self.params['max_length']))
        self.max_length.grid(row=0, column=3, padx=5)
        
        # Coherence controls
        coherence_frame = ttk.LabelFrame(controls_frame, text="Coherence Controls", padding=(5, 5))
        coherence_frame.pack(side="left", fill="x", expand=True, padx=5)
        
        # Temperature slider
        ttk.Label(coherence_frame, text="Temperature:").grid(row=0, column=0, padx=5)
        self.temperature = ttk.Scale(coherence_frame, from_=0.1, to=1.0, orient="horizontal")
        self.temperature.set(self.params['temperature'])
        self.temperature.grid(row=0, column=1, padx=5, sticky="ew")
        
        # Top-p slider
        ttk.Label(coherence_frame, text="Top-p:").grid(row=1, column=0, padx=5)
        self.top_p = ttk.Scale(coherence_frame, from_=0.1, to=1.0, orient="horizontal")
        self.top_p.set(self.params['top_p'])
        self.top_p.grid(row=1, column=1, padx=5, sticky="ew")
        
        # Repetition penalty slider
        ttk.Label(coherence_frame, text="Rep. Penalty:").grid(row=2, column=0, padx=5)
        self.rep_penalty = ttk.Scale(coherence_frame, from_=1.0, to=2.0, orient="horizontal")
        self.rep_penalty.set(self.params['repetition_penalty'])
        self.rep_penalty.grid(row=2, column=1, padx=5, sticky="ew")
        
        # Help button
        help_button = ttk.Button(controls_frame, text="?", width=1, command=self.show_parameter_help)
        help_button.pack(side="right", padx=5)
        
    def show_parameter_help(self):
        help_text = """Parameter Guide:

                    Temperature (0.1-1.0):
                    Lower = more focused and coherent
                    Higher = more creative and random

                    Top-p (0.1-1.0):
                    Lower = more focused on likely words
                    Higher = more diverse vocabulary

                    Repetition Penalty (1.0-2.0):
                    Higher = less repetition
                    Lower = more natural but may repeat

                    Length Controls:
                    Min/Max Length: Control the output size in tokens
                    (roughly 4 characters per token)"""
        
        messagebox.showinfo("Parameter Guide", help_text)
        
    def get_current_parameters(self):
        try:
            return {
                'temperature': float(self.temperature.get()),
                'max_length': int(self.max_length.get()),
                'min_length': int(self.min_length.get()),
                'top_k': self.params['top_k'],
                'top_p': float(self.top_p.get()),
                'repetition_penalty': float(self.rep_penalty.get()),
                'no_repeat_ngram_size': 3,
                'num_return_sequences': 3,
                'do_sample': True,
                'truncation': False,
                'bad_words_ids': [[50256]]
            }
        except ValueError as e:
            messagebox.showerror("Invalid Input", "Please ensure all values are numbers within the allowed ranges.")
            raise e
            
    def generate_text(self):
        prompt = self.prompt_entry.get("1.0", "end-1c").strip()
        if not prompt:
            messagebox.showwarning("Warning", "Please enter a prompt first!")
            return
            
        # Disable generate button
        self.generate_button.configure(style='DarkRed.TButton')
        self.generate_button.state(['disabled'])
        self.status_var.set("Generating text...")
        
        # Run generation in a separate thread to keep GUI responsive
        thread = threading.Thread(target=self._generate_text_thread, args=(prompt,))
        thread.daemon = True
        thread.start()
        
    def _generate_text_thread(self, prompt):
        try:
            # Get current parameters from GUI
            params = self.get_current_parameters()
            
            result = self.generator(
                prompt,
                **params
            )
            
            clean_result = result[0]["generated_text"].replace("\n", " ")
            
            # Update GUI in the main thread
            self.root.after(0, self._update_output, prompt, clean_result)

            # Add a small delay to simulate a longer generation time
            time.sleep(2)
            
        except ValueError:
            # Error already shown by get_current_parameters
            self.root.after(0, lambda: self.generate_button.state(['!disabled']))
            self.root.after(0, lambda: self.status_var.set("Ready"))
        except Exception as e:
            self.root.after(0, lambda: messagebox.showerror("Error", f"Error generating text: {str(e)}"))
            self.root.after(0, lambda: self.generate_button.state(['!disabled']))
            self.root.after(0, lambda: self.status_var.set("Ready"))
            
    def _update_output(self, prompt, result):
        # Update output text area with improved formatting
        separator = "\n" + "─" * 50 + "\n"  # Using a nicer separator
        formatted_text = f"Prompt:\n\n{prompt}\n\nOutput:\n\n{result}{separator}\n"
        
        self.output_text.insert("end", formatted_text)
        self.output_text.see("end")
        
        # Save to file with the same formatting
        with open("output_gpt2.txt", 'a', encoding='utf-8') as file:
            file.write(formatted_text)

        # re-enable generate button
        self.generate_button.configure(style='TButton')
        self.generate_button.state(['!disabled'])
        self.status_var.set("Ready")
            
    def clear_output(self):
        self.output_text.delete("1.0", "end")

def main():
    root = tk.Tk()
    app = GPT2App(root)
    root.mainloop()

if __name__ == "__main__":
    main()
