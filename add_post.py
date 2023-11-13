import sys
from dataclasses import dataclass


@dataclass
class NewPost:
    title: str
    link: str
    category: str
    subcategory: str


@dataclass
class Category:
    title: str
    posts: list[str]

    def __repr__(self) -> str:
        return f"Category(title={self.title}, total posts={len(self.posts)})"

    def __str__(self) -> str:
        return self.__repr__()


try:
    new_post = NewPost(
        title=sys.argv[1],
        link=sys.argv[2],
        category=sys.argv[3],
        subcategory=sys.argv[4]
    )
except IndexError:
    raise IndexError(
        "Usage: python add_post.py <title> <link> <category> <subcategory>")


categories = []

with open(f"./{new_post.category}/README.md", "r", encoding="utf-8") as f:
    lines = [line for line in f.read().split("\n") if line]

lines = lines[1:]  # 파일 제목 제거


for line in lines:
    if line.startswith("##"):
        categories.append(Category(title=line[3:].strip(), posts=[]))
    else:
        categories[-1].posts.append(line)

# add now aws link

for category in categories:
    if category.title == new_post.subcategory:
        category.posts.append(
            f"- [{new_post.title}]({new_post.link})")
        break
else:
    # category not found
    categories.append(Category(title=new_post.subcategory, posts=[
        f"- [{new_post.title}]({new_post.link})"]))

with open(f"./{new_post.category}/README.md", "w", encoding="utf-8") as f:
    f.write(f"# {new_post.category}\n\n")
    for category in categories:
        f.write(f"## {category.title}\n\n")
        for post in category.posts:
            f.write(f"{post}\n")
        f.write("\n")
