import requests
import time

host = 'localhost'
port = '8080'

def wait_init():
    started = False
    for _ in range(10):
        try:
            requests.get(f'http://{host}:{port}/healthcheck')
            started = True
        except BaseException:
            print('Wainting for NLU Models to initialize...')
            time.sleep(10)
        else:
            break
    if not started:
        raise EnvironmentError("Failed to wait Chat-Bot start. Most probable reason code - RASA model initialization")

def ask(text, ctx):
    st_time = time.time()
    response = requests.post(f'http://{host}:{port}/psy-chat/', json={'text': text, 'ctx': ctx}).json()
    total_time = time.time() - st_time
    print(f"{text=} -> {response['text']}")
    print(f"exec time = {total_time:.3f}s")
    return response['text'], response['ctx']

if __name__ == "__main__":
    ctx = None
    while True:
        text = input("type your answer: ")
        _, ctx = ask(text, ctx)