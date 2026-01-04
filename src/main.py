from explorer import Explorer
from textual.app import App
from textual.widgets import Terminal
from textual import Header, Footer

class NJine(App):
    def compose(self):
        yield Header()
        yield Sidebar(
              yield Explorer("./", position="left   "
        )
      )
        yield Terminal("right")
        yield Footer()

if __name__ == "__main__":
    NJine().run()