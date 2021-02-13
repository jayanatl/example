import pytz
import datetime

def lambda_handler(event, context):
    Pacific = pytz.timezone("PST8PDT")
    now = datetime.datetime.utcnow()
    return Pacific.localize(now)

if __name__ == "__main__":
    print(lambda_handler(None, None))
