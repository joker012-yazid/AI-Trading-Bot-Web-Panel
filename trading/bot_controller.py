"""Controller untuk logik AI Trading Bot."""

from __future__ import annotations

import datetime
from typing import List

try:
    import MetaTrader5 as mt5  # type: ignore
    MT5_AVAILABLE = True
except Exception:  # pragma: no cover - pakej mungkin tiada
    from . import mt5_stub as mt5  # type: ignore
    MT5_AVAILABLE = False


class BotController:
    """Urus mula/henti bot serta tetapan dagangan."""

    def __init__(self) -> None:
        self._running = False
        self.settings = {
            "symbol": "XAUUSD",
            "lot": 0.01,
            "sl": 0.0,
            "tp": 0.0,
        }
        self.logs: List[str] = []

    @property
    def status(self) -> str:
        return "Berjalan" if self._running else "Berhenti"

    def log(self, message: str) -> None:
        timestamp = datetime.datetime.now().strftime("%Y-%m-%d %H:%M:%S")
        self.logs.insert(0, f"[{timestamp}] {message}")

    def start(self) -> None:
        if self._running:
            self.log("Bot sudah berjalan.")
            return
        if not mt5.initialize():
            self.log("Gagal sambung ke MT5.")
            return
        if not MT5_AVAILABLE:
            self.log("Pakej MetaTrader5 tidak dipasang; menggunakan mod simulasi.")
        self._running = True
        self.log("Bot dimulakan.")
        # TODO: Tambah logik sambungan ke MT4/MT5 dan AI di sini

    def stop(self) -> None:
        if not self._running:
            self.log("Bot tidak berjalan.")
            return
        mt5.shutdown()
        self._running = False
        self.log("Bot dihentikan.")

    def update_settings(self, symbol: str, lot: float, sl: float, tp: float) -> None:
        self.settings.update({
            "symbol": symbol,
            "lot": lot,
            "sl": sl,
            "tp": tp,
        })
        self.log("Tetapan dagangan dikemas kini.")
