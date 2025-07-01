import openai
          openai.api_key = "${{ secrets.OPENAI_KEY }}"
          response = openai.Completion.create(engine="text-davinci-003", prompt="Generate ebook outline about digital products", max_tokens=500)
          with open("templates/ebooks/outline.md", "w") as f:
              f.write(response.choices[0].text)
