message = input('>')


def emoji_converter(input):
    words = message.split(" ")
    emojis = {
        ":)": "😃",
        ":(": "🙁"
    }

    output = ""
    for word in words:
        output = output+emojis.get(word, word)+" "

    return output


print(emoji_converter(message))
