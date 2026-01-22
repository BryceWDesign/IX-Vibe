"""
IX-Vibe common I/O utilities (v0.1)

Design goals:
- minimal dependencies
- predictable CSV parsing with sensible fallbacks
- traceability baked into plot outputs
"""

from __future__ import annotations

import os
from dataclasses import dataclass
from typing import Optional, Sequence, Tuple

import pandas as pd


@dataclass(frozen=True)
class TraceInfo:
    run_ids: Sequence[str]
    raw_files: Sequence[str]
    notes: str = ""


def _normalize_columns(df: pd.DataFrame) -> pd.DataFrame:
    df = df.copy()
    df.columns = [str(c).strip().lower().replace(" ", "_") for c in df.columns]
    return df


def read_spectrum_csv(
    path: str,
    freq_col_candidates: Sequence[str] = ("freq_hz", "frequency_hz", "frequency", "freq"),
    value_col_candidates: Sequence[str] = ("mag", "magnitude", "value", "resp", "response", "srs", "srs_g", "g"),
) -> Tuple[pd.Series, pd.Series, pd.DataFrame]:
    """
    Read a generic spectrum CSV and return (freq_hz, value, full_df).

    The CSV can be produced by various tools. We attempt common column names first.
    If columns are not found, we fall back to:
      - first numeric column as frequency
      - second numeric column as value

    Returns:
      freq: pd.Series (float, Hz)
      val:  pd.Series (float)
      df:   normalized full dataframe
    """
    if not os.path.exists(path):
        raise FileNotFoundError(f"CSV not found: {path}")

    df = pd.read_csv(path)
    df = _normalize_columns(df)

    freq_col = next((c for c in freq_col_candidates if c in df.columns), None)
    val_col = next((c for c in value_col_candidates if c in df.columns), None)

    if freq_col and val_col:
        freq = pd.to_numeric(df[freq_col], errors="coerce")
        val = pd.to_numeric(df[val_col], errors="coerce")
        mask = freq.notna() & val.notna()
        return freq[mask], val[mask], df

    # Fallback: infer numeric columns
    numeric_cols = []
    for c in df.columns:
        try:
            _ = pd.to_numeric(df[c], errors="coerce")
            numeric_cols.append(c)
        except Exception:
            continue

    if len(numeric_cols) < 2:
        raise ValueError(
            f"Could not infer frequency/value columns from {path}. "
            f"Expected at least 2 numeric columns."
        )

    freq = pd.to_numeric(df[numeric_cols[0]], errors="coerce")
    val = pd.to_numeric(df[numeric_cols[1]], errors="coerce")
    mask = freq.notna() & val.notna()
    return freq[mask], val[mask], df


def ensure_dir(path: str) -> None:
    os.makedirs(path, exist_ok=True)


def parse_csv_list(arg: str) -> Sequence[str]:
    """
    Allow either:
      --files a.csv,b.csv,c.csv
    or:
      --files "a.csv, b.csv"
    """
    parts = [p.strip() for p in arg.split(",") if p.strip()]
    if not parts:
        raise ValueError("No files provided.")
    return parts


def parse_run_ids(arg: Optional[str]) -> Sequence[str]:
    if not arg:
        return []
    return [p.strip() for p in arg.split(",") if p.strip()]


def trace_line(trace: TraceInfo) -> str:
    runs = ", ".join(trace.run_ids) if trace.run_ids else "(none)"
    files = ", ".join(trace.raw_files) if trace.raw_files else "(none)"
    base = f"Runs: {runs} | Raw: {files}"
    return f"{base} | Notes: {trace.notes}" if trace.notes else base
