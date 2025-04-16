from pytermgui import Container, Label, Splitter, Button, Checkbox, WindowManager


def main():
    # Define the container with UI components
    container = Container(
        Label("[bold accent]This is my example"),
        Label(""),
        Label("[surface+1 dim italic]It is very cool, you see"),
        Label(""),
        Splitter(
            Label("My first label", parent_align=0),
            Button("Some button", parent_align=2),
        ),
        Splitter(
            Label("My second label"),
            Checkbox(),
        ),
        Label(""),
        Splitter(Label("Left side"), Label("Middle"), Label("Right side")),
        Label(""),
        Button("Submit button"),
    )

    # Create the main window
    window = WindowManager()
    window.add(container)

    # Run the application
    window.run()


if __name__ == "__main__":
    main()

# none of this bs works chale come back later or do smth else
