from plugins.handlers import app  # Import the Client instance with handlers

if __name__ == "__main__":
    app.run()
    while True:
        check_membership_expiration()  # Make sure to move this function to the right place
        time.sleep(3600)
