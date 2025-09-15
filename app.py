from flask import Flask, render_template, request, redirect, url_for
from trading.bot_controller import BotController

app = Flask(__name__)
bot = BotController()


@app.route('/', methods=['GET', 'POST'])
def index():
    if request.method == 'POST':
        action = request.form.get('action')
        if action == 'start':
            bot.start()
        elif action == 'stop':
            bot.stop()
        elif action == 'save':
            symbol = request.form.get('symbol')
            lot = float(request.form.get('lot', 0))
            sl = float(request.form.get('sl', 0))
            tp = float(request.form.get('tp', 0))
            bot.update_settings(symbol, lot, sl, tp)
        return redirect(url_for('index'))

    return render_template(
        'index.html',
        bot_status=bot.status,
        settings=bot.settings,
        logs=bot.logs,
    )


if __name__ == '__main__':
    app.run(debug=True)
