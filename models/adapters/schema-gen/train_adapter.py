from transformers import AutoTokenizer, AutoModelForSeq2SeqLM
from transformers import Trainer, TrainingArguments, DataCollatorForSeq2Seq
from datasets import load_dataset
from peft import LoraConfig, get_peft_model, TaskType

# 1. Load model & tokenizer
model_name = "google/flan-t5-base"
tokenizer = AutoTokenizer.from_pretrained(model_name)
model = AutoModelForSeq2SeqLM.from_pretrained(model_name)

# 2. Attach LoRA adapter
lora_config = LoraConfig(
    task_type=TaskType.SEQ_2_SEQ_LM,
    r=8,
    lora_alpha=16,
    lora_dropout=0.1,
    target_modules=["q", "v"]
)
model = get_peft_model(model, lora_config)

# 3. Load datasets
train_dataset = load_dataset("json", data_files="data.jsonl")["train"]
eval_dataset = load_dataset("json", data_files="test.jsonl")["train"]

# 4. Data preprocessing
def preprocess(batch):
    inputs = tokenizer(batch["policy_string"], padding="max_length", truncation=True, max_length=512)
    labels = tokenizer(batch["json_schema_output"], padding="max_length", truncation=True, max_length=512)
    inputs["labels"] = labels["input_ids"]
    return inputs

train_dataset = train_dataset.map(preprocess, batched=True)
eval_dataset = eval_dataset.map(preprocess, batched=True)

# 5. Data collator
data_collator = DataCollatorForSeq2Seq(tokenizer, model=model)

# 6. Training arguments
training_args = TrainingArguments(
    output_dir="./lora_flant5",
    per_device_train_batch_size=4,
    per_device_eval_batch_size=4,
    learning_rate=1e-4,
    num_train_epochs=3,
    logging_dir="./logs",
    logging_steps=50,
    save_strategy="epoch",
    evaluation_strategy="epoch",
    save_total_limit=2,
    load_best_model_at_end=True,
    report_to="none"
)

# 7. Trainer
trainer = Trainer(
    model=model,
    args=training_args,
    train_dataset=train_dataset,
    eval_dataset=eval_dataset,
    tokenizer=tokenizer,
    data_collator=data_collator
)

# 8. Train adapter
trainer.train()

# 9. Save LoRA adapter only
model.save_pretrained("./lora_flant5_adapter")
