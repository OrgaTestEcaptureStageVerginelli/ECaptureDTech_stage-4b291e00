#!/bin/bash
# Properly quoted variables to satisfy ShellCheck
echo "${USER_INPUT}"

# Proper globbing for file iteration
for f in *.py; do
    [ -e "$f" ] || continue
    cat "$f"
done

# #!/bin/bash
# # ShellCheck Error: Variable is unquoted, may break on spaces
# echo $USER_INPUT

# # ShellCheck Error: Don't use ls to iterate over files, use globs
# for f in $(ls *.py); do
#     cat $f
# done
