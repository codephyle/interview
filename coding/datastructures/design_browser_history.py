# 1472. Design Browser History

# You have a browser of one tab where you start on the homepage and you can visit another url, get back in the history number of steps or move forward in the history number of steps.

# Implement the BrowserHistory class:

#     BrowserHistory(string homepage) Initializes the object with the homepage of the browser.
#     void visit(string url) Visits url from the current page. It clears up all the forward history.
#     string back(int steps) Move steps back in history. If you can only return x steps in the history and steps > x, you will return only x steps. Return the current url after moving back in history at most steps.
#     string forward(int steps) Move steps forward in history. If you can only forward x steps in the history and steps > x, you will forward only x steps. Return the current url after forwarding in history at most steps.


class BrowserHistory:
    def __init__(self, homepage):
        self.history = [homepage]
        self.current_index = 0

    def visit(self, url):
        # Clear forward history
        self.history = self.history[: self.current_index + 1]
        self.history.append(url)
        self.current_index += 1

    def back(self, steps):
        # Calculate the number of steps to move back
        steps = min(steps, self.current_index)
        self.current_index -= steps
        return self.history[self.current_index]

    def forward(self, steps):
        # Calculate the number of steps to move forward
        steps = min(steps, len(self.history) - self.current_index - 1)
        self.current_index += steps
        return self.history[self.current_index]
