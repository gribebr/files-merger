import os

INPUT_DIR = "input"
OUTPUT_DIR = "output"
OUTPUT_FILE = os.path.join(OUTPUT_DIR, "all_files.txt")

SEPARATOR = "#" * 16
EXTENSIONS = (".ts", ".tsx", ".css", ".prisma")

def files_merger():
    if not os.path.exists(OUTPUT_DIR):
        os.makedirs(OUTPUT_DIR)

    with open(OUTPUT_FILE, "w", encoding="utf-8") as output:
        for root, _, files in os.walk(INPUT_DIR):
            for file_name in sorted(files):
                if file_name.endswith(EXTENSIONS):
                    file_path = os.path.join(root, file_name)
                    relative_path = os.path.relpath(file_path, INPUT_DIR)
                    output.write(f"{SEPARATOR}\n")
                    output.write(f"FILE: {relative_path}\n")
                    output.write(f"{SEPARATOR}\n\n")

                    with open(file_path, "r", encoding="utf-8") as file:
                        output.write(file.read())

                    output.write("\n\n")

    print("Files processed successfully!")

if __name__ == "__main__":
    files_merger()