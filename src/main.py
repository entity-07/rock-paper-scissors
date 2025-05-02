from textual.app import App, ComposeResult
from textual.widgets import Static, Header, Footer, Label, Button
from textual.containers import HorizontalGroup, VerticalGroup, Horizontal, Vertical, Container

splash = Label("""
  ___  ___   ___ _  __    ___  _   ___ ___ ___     ___  ___ ___ ___ ___  ___  ___  ___  _ 
 | _ \/ _ \ / __| |/ /   | _ \/_\ | _ \ __| _ \   / __|/ __|_ _/ __/ __|/ _ \| _ \/ __|| |
 |   / (_) | (__| ' < _  |  _/ _ \|  _/ _||   /_  \__ \ (__ | |\__ \__ \ (_) |   /\__ \|_|
 |_|_\\\___/ \___|_|\_( ) |_|/_/ \_\_| |___|_|_( ) |___/\___|___|___/___/\___/|_|_\|___/(_)
                     |/                       |/                                         
""", id="splash")


class MyApp(App):

    CSS_PATH = "main-styles.tcss"

    def compose(self) -> ComposeResult:
        # vertical_container = Vertical(
        #     splash,
        #     HorizontalGroup(), id="vert_container",
        # )
        yield VerticalGroup(Container(splash), HorizontalGroup(Button(), Button(), Button()))
        yield Header()
        yield Footer()


if __name__ == "__main__":
    app = MyApp()
    app.run()
