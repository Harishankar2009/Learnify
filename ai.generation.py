from transformers import pipeline

generator = pipeline('text-generation', model = 'gpt2')

response = generator("Explain The pythagorean theorem", max_length = 100, num_return_sequences = 1)

print(response[0]['generated_text'])
