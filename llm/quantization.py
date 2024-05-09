from transformers import AutoModelForCausalLM, AutoTokenizer, QuantoConfig

model_id = "NousResearch/Meta-Llama-3-8B"
tokenizer = AutoTokenizer.from_pretrained(model_id)
quantization_config = QuantoConfig(weights="int8")
quantized_model = AutoModelForCausalLM.from_pretrained(model_id, device_map="cuda:0", quantization_config=quantization_config)