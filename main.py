# main.py
from crew import crew

if __name__ == "__main__":
    # inputs = {
    #     "url": "https://en.wikipedia.org/wiki/OpenAI"  # test URL; change as you like
    # }

    try:
        result = crew.kickoff(inputs = {
        "url": "https://www.weekday.works/people/harshdeep%20-khatke-harshdeepkhatke" #"https://en.wikipedia.org/wiki/OpenAI"  # test URL; change as you like
    })
        #crew.kickoff({"url": "https://example.com"})

    except TypeError:
        # some CrewAI versions use .run instead of .kickoff
        result = crew.run(inputs)

    print("\n=== FINAL RESULT ===")
    print(result)
