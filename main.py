import openai

# put in your key here

openai.api_key = ""

# ask initial prompt

user_response = input("Input your prompt now. To exit conversation, say #quit.\n\n")
list1 = [{"role": "user", "content": user_response}]



while True:

    if user_response == "#quit" or user_response == "quit" or user_response == "!quit":
        print("\n\nExited conversation.")
        break

    # Generate a response

    completion = openai.ChatCompletion.create(
        model="gpt-3.5-turbo",
        messages=list1
    )

    # parse response

    gpt_response = str(completion.choices[0]["message"]["content"])

    # gets rid of redundant \n usages

    if gpt_response[:2] == "\n\n":

        gpt_response = gpt_response[2:]

    # append ChatGPT's response to the conversation

    list1.append({"role": "assistant", "content": gpt_response})
    user_response = input(f'ChatGPT: {gpt_response}\n')

    # append user's response to the conversation

    list1.append({"role": "user", "content": user_response})
