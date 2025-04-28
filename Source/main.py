import ollama

def test_mistral_model():
    response = ollama.chat(
        model='mistral',
        messages=[
            {"role": "user", "content": "So as you are running locally do you need to be connected to the internet? and if so, why? and do i have a limit on how many times i can use it?"}
        ]
    )
    print("Mistral Response:", response['message']['content'])

if __name__ == "__main__":
    test_mistral_model()
