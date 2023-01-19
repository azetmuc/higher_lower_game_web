from flask import Flask
import random


gif_list = ['https://media.giphy.com/media/26gs9hWZig4XobSTe/giphy.gif',
            'https://media.giphy.com/media/l0ExncehJzexFpRHq/giphy.gif',
            'https://media.giphy.com/media/26gsqQxPQXHBiBEUU/giphy.gif',
            'https://media.giphy.com/media/l0EwYkyU1JCExVquc/giphy.gif',
            'https://media.giphy.com/media/d1E1szXDsHUs3WvK/giphy.gif',
            'https://media.giphy.com/media/l0ExvMqtnw7aTzPCE/giphy.gif',
            'https://media.giphy.com/media/l0Ex9pftnvPgw0nPa/giphy.gif',
            'https://media.giphy.com/media/l0ExiSoCkhCfSm94k/giphy.gif',
            'https://media.giphy.com/media/26gsasKHkeH0VP8d2/giphy.gif',
            'https://media.giphy.com/media/26gsjCWitFy3euTeM/giphy.gif']
gif_url = random.choice(gif_list)

my_number = random.randint(0, 9)
print(f'Random number is: {my_number}\n')

app = Flask(__name__)

@app.route('/')
def higher_lower_start():
    return f'<h1>Guess a number between 0 and 9</h1>' \
           f'<h2>Using URL field (e.g. http://URL/3), guess the hidden number</h2>' \
           f'<img src="{gif_url}">'


@app.route('/<int:guess>')
def higher_lower(guess):
    if guess > my_number:
            return f'<h1 style="color: red">Too high, try again!</h1><img src="https://media.giphy.com/media/3o6ZtaO9BZHcOjmErm/giphy.gif">'
    elif guess < my_number:
            return f'<h1 style="color: red">Too low, try again!</h1><img src="https://media.giphy.com/media/jD4DwBtqPXRXa/giphy.gif">'
    else:
            return f'<h1 style="color: green">You found it!</h1><img src="https://media.giphy.com/media/4T7e4DmcrP9du/giphy.gif">'


if __name__ == '__main__':
    app.run(debug=True)