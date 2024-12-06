import FreeSimpleGUI as sg
from converter import convert_meters

feet_label = sg.Text("Enter Feet: ")
feet_input = sg.Input( key="feet")

inches_label = sg.Text("Enter Inches: ")
inches_input = sg.Input(key="inches")

convert_button = sg.Button("Convert")
output_label = sg.Text(key="output")

window = sg.Window("Convertor", layout=[[feet_label, feet_input],
                                        [inches_label, inches_input],
                                        [convert_button, output_label]])
while True:
    events, values = window.read()
    results = convert_meters(values['feet'], values["inches"])
    window['output'].update(value=f"{results}m")


window.close()