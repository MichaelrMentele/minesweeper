# Purpose
- implement minesweeper

# Constraints
- 9x9ish board to make sure board printable to console
- fixed percentage of board is mines

# Problems
- printing the board to the screen
- identifying adjacent mines
- start a game, lose a game, configure a game, etc...

# Decomposition
Game Manager
- victory tracking
- start, stop, configure
- win/loss ratio

Presenter
- print the board to the screen
- needs to take a modified masked version of the board

Board (immutable)
- represent data for the game
- initialize with set number of mines
- initialize with a given size
- Cell
  - Annotations
    - visible -> bool
    - mark -> ENUM(Mine, Count, Question)
  - has_mine -> bool
  - adj_mines -> int (computed)

Masked Board (mutable)
- computed from Board?
- track what is known to the user and what isn't
- what squares are visible -- could also store on cell object...

CLI
- command loop
  - select coordinate to open
  - select coordinate to mark as a mine

# Iterations
## Iteration 0
- CLI that can print out a hardcoded board

## Iteration 1
- CLI can select/reveal a cell

## Iteration 2
