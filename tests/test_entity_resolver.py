import sys
from pathlib import Path
sys.path.insert(0, str(Path(__file__).parent.parent))

from Task2_access.entity_resolver import EntityResolver

resolver = EntityResolver()

while True:
    query = input()
    if query.lower() == 'exit':
        break

    print(resolver.resolver(query))