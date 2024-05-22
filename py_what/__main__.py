import torch
from transformers import AutoModelForCausalLM, AutoTokenizer, pipeline

torch.random.manual_seed(0)

model = AutoModelForCausalLM.from_pretrained(
    "microsoft/Phi-3-mini-128k-instruct",
    device_map="cpu",
    torch_dtype="auto",
    trust_remote_code=True,
)
tokenizer = AutoTokenizer.from_pretrained("microsoft/Phi-3-mini-128k-instruct")

pipe = pipeline(
    "text-generation",
    model=model,
    tokenizer=tokenizer,
)

generation_args = {
    "max_new_tokens": 500,
    "return_full_text": False,
    "temperature": 0.0,
    "do_sample": False,
}

messages = []

while(True):
    print("======================")
    msg = input("enter your message\n> ")

    messages.append(
        {"role": "user", "content": msg }
    )

    output = pipe(messages, **generation_args)
    context = output[0]['generated_text']
    print("< ", context)
    messages.append(
        {"role": "assistant", "content": context}
    )