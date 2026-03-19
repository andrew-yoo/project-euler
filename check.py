"""Check Project Euler Python solutions against hashes in answers.csv.

Usage: python check.py START END [--csv answers.csv] [--dir Python]

Example: python check.py 1 10
"""

import argparse
import csv
import importlib
import importlib.util
import io
import contextlib
import os
import sys
from types import ModuleType
from typing import Dict, Optional

import hash as hashmod


def read_answers(csv_path: str) -> Dict[int, str]:
	answers = {}
	with open(csv_path, newline="", encoding="utf-8") as fh:
		reader = csv.reader(fh)
		next(reader)  # header
		for row in reader:
			if not row:
				continue
			try:
				pid = int(row[0])
			except Exception:
				continue
			if len(row) >= 3 and row[2].strip():
				answers[pid] = row[2].strip()
	return answers


def import_solution_module(path: str, module_name: str) -> Optional[ModuleType]:
	if not os.path.exists(path):
		return None
	spec = importlib.util.spec_from_file_location(module_name, path)
	if spec is None:
		return None
	mod = importlib.util.module_from_spec(spec)
	loader = spec.loader
	assert loader is not None
	# suppress any stdout/stderr produced during module import
	with io.StringIO() as buf_out, io.StringIO() as buf_err:
		with contextlib.redirect_stdout(buf_out), contextlib.redirect_stderr(buf_err):
			loader.exec_module(mod)
	return mod


def compute_hash(value, bits: int = 256) -> str:
	return hashmod.blake2b(value, bits=bits)


def main() -> int:
	p = argparse.ArgumentParser()
	p.add_argument("start", type=int)
	p.add_argument("end", type=int)
	p.add_argument("--csv", default="answers.csv", help="Path to answers.csv")
	p.add_argument("--dir", default="Python", help="Directory containing solution files")
	p.add_argument("--bits", type=int, default=256, help="Hash bits (default 256)")
	args = p.parse_args()

	answers = read_answers(args.csv)

	matched = []
	mismatched = []
	missing = []
	errored = []

	for pid in range(args.start, args.end + 1):
		expected = answers.get(pid)
		fname = f"pe{pid:04d}.py"
		fpath = os.path.join(args.dir, fname)
		modname = f"pe{pid:04d}"

		mod = import_solution_module(fpath, modname)
		if mod is None:
			missing.append(pid)
			print(f"{pid:03d}: ERROR file missing")
			continue

		if not hasattr(mod, "answer"):
			errored.append(pid)
			print(f"{pid:03d}: ERROR no answer()")
			continue

		try:
			res = mod.answer()
		except Exception as e:
			errored.append(pid)
			msg = str(e).splitlines()[0]
			print(f"{pid:03d}: ERROR runtime: {msg}")
			continue

		if res is None:
			print(f"{pid:03d}: ERROR no result")
			continue

		try:
			# expected integer-ish result
			int_res = int(res)
		except Exception:
			errored.append(pid)
			print(f"{pid:03d}: ERROR non-integer result")
			continue

		got_hash = compute_hash(int_res, bits=args.bits)

		if expected is None:
			print(f"{pid:03d}: ERROR no hash")
			mismatched.append(pid)
			continue

		if got_hash == expected:
			matched.append(pid)
			print(f"{pid:03d}: OK")
		else:
			mismatched.append(pid)
			print(f"{pid:03d}: ERROR mismatch")

	print("")
	print(f"Matched: {len(matched)}")
	print(f"Mismatched: {len(mismatched)}")
	print(f"Missing files: {len(missing)}")
	print(f"Errored: {len(errored)}")

	return 0 if (not mismatched and not errored) else 2


if __name__ == "__main__":
	raise SystemExit(main())

