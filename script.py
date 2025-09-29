import datetime

def portfolio_message():
    tijd = datetime.datetime.now().strftime("%H:%M:%S")
    return f"Welkom op mijn portfolio! (Het is nu {tijd})"

if __name__ == "__main__":
    print(portfolio_message())
