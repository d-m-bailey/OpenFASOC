import time

def _print_progress(total_runs: int, run_number: int, start_time: int, end: str = '\r'):
	"""Displays the simulation progress.

	Displays the number of simulations completed, total simulations and the time elapsed.
	"""
	print(f"Completed {run_number} out of {total_runs} simulations. Elapsed time: {_format_elapsed_time(start_time)}{f'. Average: {_format_elapsed_time(start_time, run_number)} per simulation.' if run_number > 0 else ''}", end=end)

def _format_elapsed_time(start_time: int, divisor: int = 1):
	"""Formats the elapsed time (in seconds) into hours, minutes, and seconds format.
	"""
	elapsed_seconds = int((int(time.time()) - start_time) / divisor)

	if elapsed_seconds > 60 * 60:
		hours, minutes = divmod(elapsed_seconds, 60 * 60)
		minutes, seconds = divmod(minutes, 60)
		return f"{hours}h {minutes}m {seconds}s"

	elif elapsed_seconds > 60:
		minutes, seconds = divmod(elapsed_seconds, 60)
		return f"{minutes}m {seconds}s"

	else:
		return f"{elapsed_seconds}s"