# test_adapter.py
from transformers import AutoModelForSeq2SeqLM, AutoTokenizer
from peft import PeftModel
import torch

# Paths
base_model_name = "google/flan-t5-base"
adapter_path = "./lora_flant5_adapter"  # the trained adapter folder

# Load tokenizer and model
tokenizer = AutoTokenizer.from_pretrained(base_model_name)
model = AutoModelForSeq2SeqLM.from_pretrained(base_model_name)
model = PeftModel.from_pretrained(model, adapter_path)

# Make sure model is in eval mode
model.eval()

# Device
device = "cuda" if torch.cuda.is_available() else "cpu"
model.to(device)

# Function to run inference on a single string input
def generate_policy_output(input_string, max_length=256):
    inputs = tokenizer(input_string, return_tensors="pt").to(device)
    with torch.no_grad():
        output_ids = model.generate(**inputs, max_length=max_length)
    return tokenizer.decode(output_ids[0], skip_special_tokens=True)

# Example usage
if __name__ == "__main__":
    test_input = "Project Leads may read/write all documents in their project workspace; no access to other projects’ workspaces."
    result = generate_policy_output(test_input)
    print("Input:", test_input)
    print("Output:", result)
