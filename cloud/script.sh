!/bin/bash
# Properly quoted variables to satisfy ShellCheck
echo "${USER_INPUT}"

# Proper globbing for file iteration
for f in *.py; do
    [ -e "$f" ] || continue
    cat "$f"
done
