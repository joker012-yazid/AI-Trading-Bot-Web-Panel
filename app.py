from typing import Optional

from flask import Flask, render_template, request, redirect, url_for

from trading.bot_controller import BotController

app = Flask(__name__)
bot = BotController()


def _parse_float(value: Optional[str], default: float) -> float:
    """Safely parse a float from form data, falling back to a default."""
    try:
        if value is None or value == "":
            return default
        return float(value)
    except (TypeError, ValueError):
        return default


@app.route('/', methods=['GET', 'POST'])
def index():
    if request.method == 'POST':
        action = request.form.get('action')
        if action == 'start':
            bot.start()
        elif action == 'stop':
            bot.stop()
        elif action == 'save':
            symbol = request.form.get('symbol') or bot.settings.get('symbol', '')
            lot = _parse_float(request.form.get('lot'), bot.settings.get('lot', 0.0))
            sl = _parse_float(request.form.get('sl'), bot.settings.get('sl', 0.0))
            tp = _parse_float(request.form.get('tp'), bot.settings.get('tp', 0.0))
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
