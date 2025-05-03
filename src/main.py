from textual.app import App, ComposeResult
from textual.widgets import Static, Header, Footer, Label, Button
from textual.binding import Binding
from textual.containers import HorizontalGroup, VerticalGroup, Horizontal, Vertical, Container
from player_and_enemy import Opponent as Opponent
from player_and_enemy import Player as Player
from player_and_enemy import compare_guess as cg

splash = Label("""
  ___  ___   ___ _  __    ___  _   ___ ___ ___     ___  ___ ___ ___ ___  ___  ___  ___  _
 | _ \/ _ \ / __| |/ /   | _ \/_\ | _ \ __| _ \   / __|/ __|_ _/ __/ __|/ _ \| _ \/ __|| |
 |   / (_) | (__| ' < _  |  _/ _ \|  _/ _||   /_  \__ \ (__ | |\__ \__ \ (_) |   /\__ \|_|
 |_|_\\\___/ \___|_|\_( ) |_|/_/ \_\_| |___|_|_( ) |___/\___|___|___/___/\___/|_|_\|___/(_)
                     |/                       |/
""", id="splash")


class OpponentChoice(Label):
    """Widget to display the opponents choice"""

    def __init__(self):
        super().__init__("This is where the opponent's choice will appear")


class PlayerSelect(VerticalGroup):
    """Buttons used to select which hand the user is playing"""

    def __init__(self):
        super().__init__()
        # Default choice for the player
        self.player = Player(Player.Choice.NONE)
        self.id = "player_select"  # Unique id for querying

    def on_button_pressed(self, event: Button.Pressed) -> None:
        global verdict
        button_id = event.button.id
        if button_id == "rock":
            self.player.choice = Player.Choice.ROCK
        elif button_id == "paper":
            self.player.choice = Player.Choice.PAPER
        elif button_id == "scissors":
            self.player.choice = Player.Choice.SCISSORS
        else:
            self.query_one("#player_choice_label", Label).update(
                "This is where your choice will appear")

        # Update the player's choice label
        self.query_one("#player_choice_label", Label).update(
            "Your Choice: " + str(self.player.choice.name))
        # Update the opponent's choice label
        opponent = Opponent()
        opponent_choice_label = self.query_one(OpponentChoice)
        opponent_choice_label.update(
            "Opponent's choice: " + str(opponent.choice.name))

        # Compare guesses and get the verdict
        verdict = cg(self.player.choice, opponent.choice)
        verdict_label = self.query_one("#verdict_label", Label)
        verdict_label.update(verdict)

    def compose(self) -> ComposeResult:
        yield HorizontalGroup(
            Button(id="rock"),
            Button(id="paper"),
            Button(id="scissors"),
        )
        yield HorizontalGroup(
            Label(str(self.player.choice.name), id="player_choice_label"),
            Label("This is where the verdict goes", id="verdict_label"),
            OpponentChoice()
        )


class RockPaperScissors(App):
    CSS_PATH = "main-styles.tcss"
    BINDINGS = [
        Binding(key="^q", action="none",
                description="Ctrl + Q to quit this app btw")
    ]

    def on_mount(self) -> None:
        self.theme = "gruvbox"

    def action_none(self) -> None:
        pass

    def compose(self) -> ComposeResult:
        yield Header()
        yield VerticalGroup(Container(splash, id="splash_container"),
                            Container(
                                Label("Which HAND will you PLAY?", id="the_question"), id="exclude"),
                            PlayerSelect(),
                            Label("INSTRUCTIONS"),
                            Label("1. Play this in fullscreen"),
                            Label(
                                "2. Click on the palette bottom right to access settings and change the color scheme"),
                            Label(
                                "3. There is no end screen, the game ends when you quit"),
                            Label("4. have fun"),
                            Label("json was here"),

                            id="final_vert"
                            )
        yield Footer()


if __name__ == "__main__":
    app = RockPaperScissors()
    app.run()
