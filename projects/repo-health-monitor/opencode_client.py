#!/usr/bin/env python3
from hermes_tools import terminal
res = terminal("opencode run --command 'Create hello.txt in the current directory with content hello-world-test'", timeout=120)
print(res.get("output", ""))
