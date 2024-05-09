from transformers import AutoTokenizer, AutoModelForCausalLM
from accelerate import disk_offload
import torch

model_id = "NousResearch/Meta-Llama-3-8B-Instruct"

model = AutoModelForCausalLM.from_pretrained(model_id, torch_dtype=torch.float16, low_cpu_mem_usage = True).cpu()   

disk_offload(model=model, offload_dir="offload")

tokenizer = AutoTokenizer.from_pretrained(model_id)


messages = [
    {"role": "system", "content": "You are a pirate chatbot who always responds in pirate speak!"},
    {"role": "user", "content": "Who are you?"},
]

input_ids = tokenizer.apply_chat_template(
    messages,
    add_generation_prompt=True,
    return_tensors="pt"
).to(model.device)

terminators = [
    tokenizer.eos_token_id,
    tokenizer.convert_tokens_to_ids("<|eot_id|>")
]

outputs = model.generate(
    input_ids,
    max_new_tokens=256,
    eos_token_id=terminators,
    do_sample=True,
    temperature=0.6,
    top_p=0.9,
)
print(outputs)