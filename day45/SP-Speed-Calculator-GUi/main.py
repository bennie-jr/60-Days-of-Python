from PyQt6.QtWidgets import QApplication, QLabel, QWidget, QGridLayout, \
    QLineEdit, QPushButton, QComboBox
import sys


class SpeedCalculator(QWidget):
    def __init__(self):
        super().__init__()

        self.setWindowTitle("Average Speed Calculator")
        grid = QGridLayout()

        # Create widgets
        distance_label = QLabel("Distance:")
        self.distance_line_edit = QLineEdit()

        self.unit_box = QComboBox()
        
        time_label = QLabel("Time (hours):")
        self.time_line_edit = QLineEdit()
        
        calculate_button = QPushButton("Calculate Speed")
        calculate_button.clicked.connect(self.calculate_speed)
        self.output_label = QLabel("")

        # Add items to unit box
        self.unit_box.addItem("Imperial(miles)")
        self.unit_box.addItem("Metric(km)")

        # Add widgets to grid
        grid.addWidget(distance_label, 0, 0)
        grid.addWidget(self.distance_line_edit, 0, 1)
        grid.addWidget(self.unit_box, 0, 2)
        grid.addWidget(time_label, 1, 0)
        grid.addWidget(self.time_line_edit, 1, 1)
        grid.addWidget(calculate_button, 2, 1)
        grid.addWidget(self.output_label, 3, 0, 1, 2)


        self.setLayout(grid)


    def calculate_speed(self):
        # Check unit box choice and calculate average speed
        if self.unit_box.currentIndex() == 0:
            distance = self.distance_line_edit.text()
            time = self.time_line_edit.text()
            average_speed_miles = float(distance) / float(time) * 0.621371
            self.output_label.setText(f"Average Speed: {average_speed_miles} mph")
        else:
            distance = self.distance_line_edit.text()
            time = self.time_line_edit.text()
            average_speed_km = float(distance) / float(time)
            self.output_label.setText(f"Average Speed: {average_speed_km} km/h")



app = QApplication(sys.argv)
speed_calculator = SpeedCalculator()
speed_calculator.show()
sys.exit(app.exec())