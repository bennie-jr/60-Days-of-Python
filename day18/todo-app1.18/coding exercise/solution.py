import FreeSimpleGUI as sg
from converter import convert_meters

sg.theme("Black")
feet_label = sg.Text("Enter Feet: ")
feet_input = sg.Input( key="feet")

inches_label = sg.Text("Enter Inches: ")
inches_input = sg.Input(key="inches")

convert_button = sg.Button("Convert")
output_label = sg.Text(key="output")
exit_button = sg.Button("Exit")

window = sg.Window("Convertor", layout=[[feet_label, feet_input],
                                        [inches_label, inches_input],
                                        [convert_button, exit_button, output_label]])
while True:
    event, values = window.read()
    match event:
        case "Convert":
            results = convert_meters(values['feet'], values["inches"])
            window['output'].update(value=f"{results} m")
        case "Exit":
            break
        case sg.WIN_CLOSED:
            break


window.close()