from transformers import AutoModelForCausalLM

# Load or save the model
model_id = "NousResearch/Meta-Llama-3-8B-Instruct"
model_path = "C:\chatbot nic\engdata\llama"

# Check if the model is already saved
try:
    # Load the saved model from disk
    model = AutoModelForCausalLM.from_pretrained(model_path)
    print("Model loaded from disk.")
except:
    # If the model is not saved, load it and save it to disk
    model = AutoModelForCausalLM.from_pretrained(model_id)
    model.save_pretrained(model_path)
    print("Model loaded and saved to disk.")

# Now you can use the model for inference
