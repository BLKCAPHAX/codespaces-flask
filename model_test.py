# load the large language model file
from llama_cpp import Llama

LLM = Llama(model_path="./llama-2-7b.Q8_0.gguf", n_ctx=9999)

while True:
    prompt = input()
    output = LLM(prompt, max_tokens=0, stream=True)

    print()
    print("answer = ", end="", flush=True)
    for txt in output:
        print(txt["choices"][0]["text"], end="", flush=True)
    print()