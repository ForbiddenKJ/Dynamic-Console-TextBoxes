from math import floor

# Get longest value in an list

def _longestValue(x: list) -> int:
    y = [0, 0]

    for index, value in enumerate(x):

        if value is not None:
            if len(value) > y[1]:
                y = [index, len(value)]

    return y[0]


class TextBox:
    def __init__(self, border: str ='*', padding: int = 4):
        # Check if padding is an odd number
        if padding&1: return

        # Check if border is one letter long
        if len(border)>1: return

        self.border = border

        self.padding = padding
        self.stringPadding = ''.join([' ' for _ in range(self.padding)])

        self.values = []
        self.drawValues = []

    def addValue(self, v: str):
        self.values.append(v)

    def removeValue(self, i: int):
        del self.values[i]

    def updateBox(self):
        # Clear drawValues

        self.drawValues = []

        # Find Maximum Length

        length = len(self.values[_longestValue(self.values)])+(2*self.padding)

        # Add Top Line Of Box

        self.drawValues.append(''.join([self.border for _ in range(length+2)]))

        # Correct Values For Draw

        for value in self.values:

            # Check if the value is a line break or not

            if value is None:
                self.drawValues.append(f"{self.border}{''.join([' ' for _ in range(length)])}{self.border}")

            # If the value is not a line break calculate how much extra padding is required

            else:

                # Get extra padding length required

                extraPaddingLength = length - (len(value)+(2*self.padding))
                extraPadding = [0, 0]

                # Check if extraPaddingLength/2 is an integar or float

                if not (extraPaddingLength/2) % 1:
                    extraPadding = [extraPaddingLength/2, extraPaddingLength/2]

                # Floor and add 1 to the right extra padding if its a float

                if (extraPaddingLength/2) % 1:
                    extraPadding = [floor(extraPaddingLength/2), (floor(extraPaddingLength/2))+1]

                # Calculate the extra padding

                ePadding = [''.join([' ' for _ in range(floor(extraPadding[0]))]), ''.join([' ' for _ in range(floor(extraPadding[1]))])]

                # Add "draw safe" line of text to draw values

                self.drawValues.append(f'{self.border}{ePadding[0]}{self.stringPadding}{value}{self.stringPadding}{ePadding[1]}{self.border}')

        # Add bottom line

        self.drawValues.append(''.join([self.border for _ in range(length+2)]))

    def drawTextBox(self):
        # Draw values

        print('\n'.join(self.drawValues))

def main():
    myTextBox = TextBox('*', 4)
    myTextBox.addValue('Hello')
    myTextBox.addValue(None)
    myTextBox.addValue('Github')
    myTextBox.addValue(None)
    myTextBox.addValue('from: KJ')

    myTextBox.updateBox()
    myTextBox.drawTextBox()

if __name__ == '__main__':
    main()
