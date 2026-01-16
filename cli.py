from qa_engine import StudyAssistant
import os

def clear_screen():
    os.system('cls' if os.name == 'nt' else 'clear')

def print_banner():
    banner = """  
  ___________________________________________________________________________________________________________________________________________           
 /      \   |  \                    |  \                 /      \                     |  \            |  \                         |  \          
|  $$$$$$\ _| $$_    __    __   ____| $$ __    __       |  $$$$$$\  _______   _______  \$$  _______  _| $$_     ______   _______  _| $$_         
| $$___\$$|   $$ \  |  \  |  \ /      $$|  \  |  \      | $$__| $$ /       \ /       \|  \ /       \|   $$ \   |      \ |       \|   $$ \        
 \$$    \  \$$$$$$  | $$  | $$|  $$$$$$$| $$  | $$      | $$    $$|  $$$$$$$|  $$$$$$$| $$|  $$$$$$$ \$$$$$$    \$$$$$$\| $$$$$$$\\$$$$$$        
 _\$$$$$$\  | $$ __ | $$  | $$| $$  | $$| $$  | $$      | $$$$$$$$ \$$    \  \$$    \ | $$ \$$    \   | $$ __  /      $$| $$  | $$ | $$ __       
|  \__| $$  | $$|  \| $$__/ $$| $$__| $$| $$__/ $$      | $$  | $$ _\$$$$$$\ _\$$$$$$\| $$ _\$$$$$$\  | $$|  \|  $$$$$$$| $$  | $$ | $$|  \      
 \$$    $$   \$$  $$ \$$    $$ \$$    $$ \$$    $$      | $$  | $$|       $$|       $$| $$|       $$   \$$  $$ \$$    $$| $$  | $$  \$$  $$      
  \$$$$$$     \$$$$   \$$$$$$   \$$$$$$$ _\$$$$$$$       \$$   \$$ \$$$$$$$  \$$$$$$$  \$$ \$$$$$$$     \$$$$   \$$$$$$$ \$$   \$$   \$$$$       
                                        |  \__| $$                                                                                               
                                         \$$    $$                                                                                               
                                          \$$$$$$                                                                                              
____________________________________________________________________________________________________________________________________________
    """
    print(banner)
    print("  Welcome! Paste a PDF path to load it, or just start typing to chat.")
    print("  Type '/clear' to reset history or 'exit' to quit.")
    print("_________________________________________________________________________________________________________________________________\n")

def main():
    assistant = StudyAssistant()
    clear_screen()
    print_banner()

    while True:
        # Get input and clean it up
        user_input = input("-> ").strip()
        
        # Exit
        if user_input.lower() in ["exit", "quit", "q"]:
            print(" Goodbye!")
            break

        # Manual History Clear
        if user_input.lower() == "/clear":
            assistant.clear_history() 
            print(" Chat history cleared!")
            continue

        if not user_input:
            continue

        # Is it a File or a Question?
        potential_path = user_input.replace('"', '').replace("'", "")
        
        if os.path.isfile(potential_path) and potential_path.lower().endswith('.pdf'):
            print(f" [System] Loading: {os.path.basename(potential_path)}...")
            success = assistant.load_pdf(potential_path)
            if success:
                print("✅ [System] PDF context is ready! What would you like to know?")
            else:
                print("❌ [System] Failed to load PDF.")
        
        else:
            print(" [Assistant] Thinking...")
            answer = assistant.ask(user_input) 
            print(f"\nASSISTANT ❯ {answer}\n")

if __name__ == "__main__":
    main()