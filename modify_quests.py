import os
from glob import iglob

def main():
  path = "./src/config/betterquesting/DefaultQuests/Quests/**/*"
  files = [f for f in iglob(path, recursive=True) if os.path.isfile(f)]
  for filePath in files:
    print(filePath)
    contents = ""
    with open(filePath, "r", encoding="utf8") as file:
      contents = file.read()
      contents = contents.replace("bq_standard:crafting", "bq_standard:retrieval")
      contents = contents.replace("§1", "§9")
      contents = contents.replace("§2", "§a")
      contents = contents.replace("§3", "§b")
      contents = contents.replace("§4", "§c")
      contents = contents.replace("§5", "§d")
      contents = contents.replace("§6", "§e")
      contents = contents.replace("§8", "§7")
    if len(contents) > 0:
      with open(filePath, "w", encoding="utf8") as file:
        file.write(contents)

if __name__ == "__main__":
  main()