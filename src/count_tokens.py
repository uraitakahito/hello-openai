import tiktoken


def main():
    text = "サピエンス全史を図書館で借りました。"

    encoding = tiktoken.encoding_for_model("gpt-4o")
    tokens = encoding.encode(text)
    print(len(tokens))


if __name__ == "__main__":
    main()
