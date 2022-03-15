from utils import seconds_to_days


def test_seconds_to_days():
    seconds = 86400
    days = seconds_to_days(seconds)
    print(days)
    assert days == float(1)


if __name__ == '__main__':
    test_seconds_to_days()
