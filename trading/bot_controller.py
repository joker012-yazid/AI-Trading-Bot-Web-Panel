"""Controller untuk logik AI Trading Bot."""

from __future__ import annotations

import datetime
import json
from pathlib import Path
from typing import List

try:
    import MetaTrader5 as mt5  # type: ignore
    MT5_AVAILABLE = True
except Exception:  # pragma: no cover - pakej mungkin tiada
    from . import mt5_stub as mt5  # type: ignore
    MT5_AVAILABLE = False


CONFIG_FILE = Path(__file__).with_name("config.json")
ALLOWED_SYMBOLS = {"XAUUSD", "US30"}


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
        self.load_settings()

    @property
    def status(self) -> str:
        return "Berjalan" if self._running else "Berhenti"

    def log(self, message: str) -> None:
        timestamp = datetime.datetime.now().strftime("%Y-%m-%d %H:%M:%S")
        self.logs.insert(0, f"[{timestamp}] {message}")
        # Kekalkan log terkini sahaja supaya memori tidak meningkat tanpa kawalan
        if len(self.logs) > 200:
            self.logs = self.logs[:200]

    def _validate_symbol(self, symbol: str) -> str:
        """Pastikan simbol yang diterima berada dalam senarai dibenarkan."""
        if not symbol:
            return self.settings["symbol"]
        normalized = symbol.upper()
        if normalized not in ALLOWED_SYMBOLS:
            self.log(
                f"Simbol {normalized} tidak disokong; menggunakan nilai sebelumnya."
            )
            return self.settings["symbol"]
        return normalized

    def _sanitize_numeric(self, value: float, fallback: float, label: str) -> float:
        """Pastikan nilai numerik adalah sah dan tidak negatif."""
        try:
            number = float(value)
        except (TypeError, ValueError):
            self.log(f"Nilai {label} tidak sah; menggunakan nilai sebelumnya.")
            return fallback
        if number < 0:
            self.log(f"Nilai {label} tidak boleh negatif; menggunakan nilai sebelumnya.")
            return fallback
        return number

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
        current = self.settings
        updated_settings = {
            "symbol": self._validate_symbol(symbol),
            "lot": self._sanitize_numeric(lot, current["lot"], "lot"),
            "sl": self._sanitize_numeric(sl, current["sl"], "SL"),
            "tp": self._sanitize_numeric(tp, current["tp"], "TP"),
        }
        self.settings.update(updated_settings)
        self.save_settings()
        self.log("Tetapan dagangan dikemas kini.")

    def load_settings(self) -> None:
        """Muat tetapan daripada fail JSON jika wujud."""
        if CONFIG_FILE.exists():
            try:
                with CONFIG_FILE.open("r", encoding="utf-8") as fh:
                    data = json.load(fh)
                self.settings.update(data)
            except Exception:
                self.log("Gagal membaca fail konfigurasi.")

    def save_settings(self) -> None:
        """Simpan tetapan ke fail JSON."""
        try:
            with CONFIG_FILE.open("w", encoding="utf-8") as fh:
                json.dump(self.settings, fh)
        except Exception:
            self.log("Gagal menulis fail konfigurasi.")
