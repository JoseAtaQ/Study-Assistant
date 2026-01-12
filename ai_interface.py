import requests
import json

class AIInterface:
    # Initialize the AI interface
    def __init__(self, model_name: str = "llama2"):
        # Store model name
        self.model_name = model_name
        self.base_url = "http://localhost:11434/api"
        self.context = None

        # Check connectivity on startup
        try:
            response = requests.get(f"{self.base_url}/tags", timeout=3)
            if response.status_code == 200:
                print(f"✅ Connected to Ollama. Current model target: {self.model_name}")
        except:
            print("Warning: Could not connect to Ollama. Make sure the app is open.")

    #Check if model is installed
    def is_model_installed(self) -> bool:
        """Check if the specific model is already downloaded."""
        try:
            response = requests.get(f"{self.base_url}/tags", timeout=2)
            models = [m['name'] for m in response.json().get('models', [])]
            # Check for the name directly or with the :latest tag
            return self.model_name in models or f"{self.model_name}:latest" in models
        except:
            return False
        
    # ask to download model if not installed
    def download_model(self):
        """Triggers the pull request to Ollama."""
        print(f"Starting download for '{self.model_name}'...")
        print("This may take a few minutes. Please don't close the program.")
        url = f"{self.base_url}/pull"
        try:
            # (5 mins) for the download
            response = requests.post(url, json={"name": self.model_name, "stream": False}, timeout=300)
            if response.status_code == 200:
                print(f"✅ {self.model_name} is ready to use!")
            else:
                print(f"❌ Download failed: {response.text}")
        except Exception as e:
            print(f"❌ Error during download: {e}")

    # Send a prompt and get a response
    def chat(self, prompt: str) -> str:
        url = f"{self.base_url}/generate"
        payload = {
            "model": self.model_name,
            "prompt": prompt,
            "stream": False, 
            "context": self.context,  # <--- Send the previous context back
            "system": "You are a helpful study assistant. Use the provided lecture notes to answer questions.",
            "options": {"temperature": 0.7}
        }
        
        try:
            response = requests.post(url, json=payload, timeout=60)
            response.raise_for_status() 
            data = response.json()
            
            # Save the new context
            self.context = data.get("context") 
            
            return data.get("response", "No response received.")
        except Exception as e:
            return f"❌ Chat Error: {e}"
            
    def clear_history(self):
        """Call this if you want the AI to 'forget' everything and start fresh."""
        self.context = None

    # Check if Ollama server is available
    def is_available(self) -> bool:
        """Check if the local Ollama server is running and reachable."""
        try:
            response = requests.get(f"{self.base_url}/tags", timeout=2)
            return response.status_code == 200
        except (requests.exceptions.ConnectionError, requests.exceptions.Timeout):
            # If the server is off or too slow to respond, it's not "available"
            return False    


if __name__ == "__main__":
    current_model = "llama2"
    ai = AIInterface(model_name=current_model)
    
    if ai.is_available():
        # Check if the model is actually there
        if not ai.is_model_installed():
            choice = input(f"❓ Model '{current_model}' not found. Download it now? (y/n): ")
            if choice.lower() == 'y':
                ai.download_model()
            else:
                print("Exiting. Cannot proceed without the model.")
                exit()
        
        # If we reach here, we have the server and the model
        response = ai.chat("What is Python?")
        print(f"\nResponse:\n{response}")
    else:
        print("❌ Ollama is not running. Please open the Ollama application first.")
