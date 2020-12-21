# Vim Reminders

Because we all forget.

`i` for insert, esc for command

`h` left, `k` up, `l` right, `j` down ... uh arrow keys seem to work too

`w` start of next word, `e` end of word, `b` beginning of word
this can be combined with numbers, `5w` --> pressing w 5 times

`{number}i{phrase>}` inserts the phrase that number of times

`f` find next occurance, `F` find previous occurance, `3fq` --> third occurance of `f`

`%` find matching parentheses or bracket

`0` beginning of line, `$` end of line

`*` next occurance of word, `#` previous occurance of word

`gg` beginning of file, `G` end of file, `{number}G` goes to line {number}

`/{phrase}` searches for the phrase, `n` next occurance, `N` previous occurance

`o` inserts a new line below and changes to insert mode, `O` inserts a line above

`x` deletes character at cursor, `X` deletes to the left of cursor

`d` deletes, can be combined with movement --> `dw` deletes the first word on the right

repeat commands with `.`

`v` enters visual mode --> enables "highlighting" of scope for next command

`:w` save, `:q` quit, `:q!` quit without saving, `u` undo, `:help` for help
