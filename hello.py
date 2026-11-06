import platform
import sys


def main():
	name = input("What is your name? ")
	print(f"Hello, {name}! Welcome to the AI Engineering lab.")
	print(f"Python version : {sys.version.split()[0]}")
	print(f"Running from   : {sys.executable}")
	print(f"Operating sys. : {platform.system()} {platform.release()}")

	in_venv = sys.prefix != sys.base_prefix
	print(f"Inside a venv  : {'yes' if in_venv else 'NO - activate .venv first'}")


if __name__ == "__main__":
	main()
