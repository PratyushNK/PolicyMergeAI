from transformers import AutoModelForSeq2SeqLM, AutoTokenizer
from peft import PeftModel

# Load base model
base_model_name = "models/flan-t5-base"
tokenizer = AutoTokenizer.from_pretrained(base_model_name)
model = AutoModelForSeq2SeqLM.from_pretrained(base_model_name)

# Load adapters one by one
adapters = [
    "models/adapters/schema-gen"
    #"models/adapters/schema-to-alloy",
    #"models/adapters/alloy-explain"
]

for adapter_path in adapters:
    model = PeftModel.from_pretrained(model, adapter_path)
    print(f"Loaded adapter: {adapter_path}")

# Quick test generation
input_text = "Translate policy text to canonical schema"
inputs = tokenizer(input_text, return_tensors="pt")
outputs = model.generate(**inputs, max_length=100)
print("Output:", tokenizer.decode(outputs[0], skip_special_tokens=True))
