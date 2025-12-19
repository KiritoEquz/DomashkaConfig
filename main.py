import sys
import yaml
from lark import Lark, Tree, Token

def main():
    parser = Lark.open("syntax.lark", parser = "lalr")

    source = sys.stdin.read()
    tree = parser.parse(source)
    result = tree_to_dict(tree)
    yaml.dump(result,
              stream=sys.stdout,
              allow_unicode=True,
              sort_keys=False)



def tree_to_dict(node):
    """
    Преобразует parse tree Lark в Python-структуру,
    пригодную для сериализации в YAML
    """
    if isinstance(node, Tree):
        return {
            "type": node.data,
            "children": [tree_to_dict(child) for child in node.children]
        }
    elif isinstance(node, Token):
        return {
            "type": node.type,
            "value": node.value
        }
    else:
        return str(node)



if __name__ == "__main__":
    main()