from datetime import datetime
import pytz

SIGNS = {
    "Aries": {
        "from": {
            "month": 3,
            "day": 21,
        },
        "to": {
            "month": 4,
            "day": 20,
        },
    },
    "Taurus": {
        "from": {
            "month": 4,
            "day": 21,
        },
        "to": {
            "month": 5,
            "day": 20,
        },
    },
    "Gemini": {
        "from": {
            "month": 5,
            "day": 21,
        },
        "to": {
            "month": 6,
            "day": 21,
        },
    },
    "Cancer": {
        "from": {
            "month": 6,
            "day": 22,
        },
        "to": {
            "month": 7,
            "day": 22,
        },
    },
    "Leo": {
        "from": {
            "month": 7,
            "day": 23,
        },
        "to": {
            "month": 8,
            "day": 23,
        },
    },
    "Virgo": {
        "from": {
            "month": 8,
            "day": 24,
        },
        "to": {
            "month": 9,
            "day": 23,
        },
    },
    "Libra": {
        "from": {
            "month": 9,
            "day": 24,
        },
        "to": {
            "month": 10,
            "day": 23,
        },
    },
    "Scorpio": {
        "from": {
            "month": 10,
            "day": 24,
        },
        "to": {
            "month": 11,
            "day": 22,
        },
    },
    "Sagittarius": {
        "from": {
            "month": 11,
            "day": 23,
        },
        "to": {
            "month": 12,
            "day": 21,
        },
    },
    "Capricorn": {
        "from": {
            "month": 12,
            "day": 22,
        },
        "to": {
            "month": 1,
            "day": 20,
        },
    },
    "Aquarius": {
        "from": {
            "month": 1,
            "day": 21,
        },
        "to": {
            "month": 2,
            "day": 20,
        },
    },
    "Pisces": {
        "from": {
            "month": 2,
            "day": 21,
        },
        "to": {
            "month": 3,
            "day": 20,
        },
    },
}


def get_zodiac(birthday_: datetime):
    birthday = datetime(
        year=birthday_.year, month=birthday_.month, day=birthday_.day + 1
    )
    for sign_key in SIGNS.keys():
        sign = SIGNS.get(sign_key)
        _from = get_timezone(
            datetime(
                year=birthday.year,
                month=sign.get("from").get("month"),
                day=sign.get("from").get("day"),
            )
        )
        _to = get_timezone(
            datetime(
                year=birthday.year,
                month=sign.get("to").get("month"),
                day=sign.get("to").get("day"),
            )
        )
        birthday = birthday.replace(tzinfo=pytz.UTC)
        _to = _to.replace(tzinfo=pytz.UTC)
        _from = _from.replace(tzinfo=pytz.UTC)
        if _from <= birthday <= _to:
            return sign_key


def get_timezone(datetime_: datetime):
    timezone = pytz.timezone("Etc/GMT+5")
    return datetime_.astimezone(timezone)
