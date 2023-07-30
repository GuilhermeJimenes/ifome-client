if __name__ == '__main__':
    from src.application.status_app import StatusApp
    print('Waiting for a message...')

    while True:
        result = StatusApp().status()
        if result == 'error':
            break
        elif result:
            print("Result:", result)
