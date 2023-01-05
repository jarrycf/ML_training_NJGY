import random
import markovify

text_model = markovify.Text('result')

subheadings = ['有害食品', '无害食品', '注意事项']
for i in range(5):
    print(text_model.make_sentence())
# Generate a random subheading
subheading = random.choice(subheadings)

# Use the subheading to generate text using the text generation model
generated_text = text_model.make_sentence(prefix=subheading)

print(generated_text)
