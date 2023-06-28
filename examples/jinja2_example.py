from jinja2 import Environment, FileSystemLoader

test_name = "Python Challenge"

environment = Environment(loader=FileSystemLoader("templates/"))
template = environment.get_template("example.py.j2")

content = template.render(test_name=test_name)
with open('example.py', mode="w", encoding="utf-8") as message:
    message.write(content)
    print(f"... wrote")
