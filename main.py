from tkinter import Tk, Entry, Label, Button
from tkinter.font import Font

def main() -> None:
    wn = Tk()
    wn.title('Base Calculator')

    fontStyle = Font(family='Comic Sans', size=20)

    entryExp = Entry(master=wn, width=30, font=fontStyle)
    labelEq = Label(master=wn, text=' = ', font=fontStyle)
    labelResult = Label(master=wn, text='0', font=fontStyle)
    buttonCalc = Button(master=wn, text='Calculate', font=fontStyle,
                        command=lambda : calculate(entryExp, labelResult))

    entryExp.grid(row=0, column=0)
    labelEq.grid(row=0, column=1)
    labelResult.grid(row=0, column=2)
    buttonCalc.grid(row=1)

    wn.mainloop()


def calculate(expression, labelResult):
    """Evaluate the expression in the entry widget.
    Update the label with the result on row 0.
    """

    e = expression.get() 
    eParts = splitUp(e)

    newE = rebuildExpression(eParts)
    
    result = eval(newE)
    labelResult['text'] = result

def splitUp(expression):
  """ Break the expression into parts and return the list: 
  [Left #, Right #, Operator] or [#]
  """

  parts = []

  if '*' in expression:
    parts = expression.split('*')
    parts.append('*')
  elif '/' in expression:
    parts = expression.split('/')
    parts.append('/')
  elif '+' in expression:
    parts = expression.split('+')
    parts.append('+')
  elif '-' in expression:
    parts = expression.split('-')
    parts.append('-')

  return parts

def rebuildExpression(parts):
  """Convert all numbers to decimal and return the expression with the decimal #
  """

  firstNumber = parts[0]
  secondNumber = parts[1]
  operator = parts[2]

  if '0b' in firstNumber: #0b1010
    firstNumber = int(firstNumber[2:], 2)
  elif '0o' in firstNumber: #0o727
    firstNumber = int(firstNumber[2:], 8)
  elif '0d' in firstNumber: #0d123
    firstNumber = firstNumber[2:]
  elif '0x' in firstNumber: #0xff
    firstNumber = int(firstNumber[2:], 16)
  
  if '0b' in secondNumber: #0b1010
    secondNumber = int(secondNumber[2:], 2)
  elif '0o' in secondNumber: #0o727
    secondNumber = int(secondNumber[2:], 8)
  elif '0d' in secondNumber: #0d123
    secondNumber = secondNumber[2:]
  elif '0x' in secondNumber: #0xff
    secondNumber = int(secondNumber[2:], 16)


  return f'{firstNumber}{operator}{secondNumber}';

if __name__ == '__main__':
    main()