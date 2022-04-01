# Converting Unraid Apps

- Get the raw json app list
- Turn it into yaml
- run the following in notepad++

regex replace without newline match.
find: `(^- Name: )([a-zA-Z0-9-]+)`
replace: `\2:`