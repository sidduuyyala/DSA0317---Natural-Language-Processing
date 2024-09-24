import openai
openai.api_key = 'your-openai-api-key'
def generate_text(prompt, model="text-davinci-003", max_tokens=100):
    response = openai.Completion.create(
        engine=model,
        prompt=prompt,
        max_tokens=max_tokens,
        n=1,
        stop=None,
        temperature=0.7,
    )
    return response.choices[0].text.strip()
prompt = "Write a short story about a robot exploring Mars."
generated_text = generate_text(prompt)
print(generated_text)