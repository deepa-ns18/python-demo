import os

APP_NAME = os.getenv("APP_NAME", "Python Demo")
ENVIRONMENT = os.getenv("ENVIRONMENT", "development")
LOG_LEVEL = os.getenv("LOG_LEVEL", "info")


def build_message():
    return (
        f"Application: {APP_NAME}\n"
        f"Environment: {ENVIRONMENT}\n"
        f"Log Level: {LOG_LEVEL}"
    )


if __name__ == "__main__":
    print(build_message())
