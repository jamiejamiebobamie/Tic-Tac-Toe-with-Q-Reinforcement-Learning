# Tic Tac Toe AI

This is a Python Tic Tac Toe terminal game that implements Q-Learning to play against the player and to suggest moves.
The AI wins on average 97% of the time when going first (when playing against someone who is just picking randomly) and 85%
of the time when going second. The AI ties 100% of the time when both players are using the AI. When neither player is using the AI and just picking moves at random, the first person who went wins 58% of the time.

## Getting Started

Clone the repo locally. In your terminal, navigate to the main folder of the cloned repo and type: "python3 play.py" without quotations to play the game.

### Prerequisites

You will need the latest version of Python to play.

## Authors

* **Jamie McCrory**

## License

This project is licensed under the MIT License - see the [LICENSE.md](LICENSE.md) file for details

## Acknowledgments

* https://towardsdatascience.com/simple-reinforcement-learning-q-learning-fcddc4b6fe56
* http://mnemstudio.org/path-finding-q-learning-tutorial.htm
* https://www.learndatasci.com/tutorials/reinforcement-q-learning-scratch-python-openai-gym/

## To-Do

Write a function that tests one pickled brain against another.

## Note

The folder marked "different_implementation" builds a Q with just a board_state as the key.
This led to ambiguity when asking the Q for the best move as it didn't know whose turn it was, yielding a slightly lower accuracy.
