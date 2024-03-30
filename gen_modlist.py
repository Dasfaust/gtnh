import os

def main():
  path = "./src/mods"
  files = [f for f in os.listdir(path) if os.path.isfile(os.path.join(path, f))]
  with open("modlist.txt", "w") as modlist:
    for file_name in files:
      entry = f"{file_name}\n"
      print(entry)
      modlist.write(entry)

if __name__ == "__main__":
  main()