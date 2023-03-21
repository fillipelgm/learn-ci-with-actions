from datetime import date, timedelta


def get_today_as_str():
    """Returns the current date as a string"""
    return str(date.today())


def get_yesterday_as_str():
    """Returns yesterday's date as a string"""
    return str(date.today() - timedelta(days=1))


def main():
    """Main function (meant to test stuff only)"""
    print(type(date.today()))
    print(f"today: {get_today_as_str()}")
    print(f"yesterday: {get_yesterday_as_str()}")


if __name__ == "__main__":
    main()
