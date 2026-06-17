# scratch script to check brace balance in css/responsive.css
with open('css/responsive.css', 'r') as f:
    content = f.read()

lines = content.split('\n')
stack = []
for i, line in enumerate(lines):
    # Strip comments
    # Simple check for braces
    for char in line:
        if char == '{':
            stack.append(i + 1)
        elif char == '}':
            if len(stack) == 0:
                print(f"Unmatched closing brace at line {i + 1}")
            else:
                stack.pop()

print("Remaining open braces from lines:", stack)
