import flet as ft

def main(page: ft.Page):
    # Window settings
    page.title = "Almasa Dental Clinic"
    page.window_width = 800
    page.window_height = 600
    page.bgcolor = ft.colors.WHITE

    appointments = []

    # Function to add appointments
    def add_appointment(e):
        name = name_field.value
        phone = phone_field.value
        date = date_field.value

        if name and phone and date:
            appointment = {"name": name, "phone": phone, "date": date}
            appointments.append(appointment)
            update_appointments_list()
            name_field.value = ""
            phone_field.value = ""
            date_field.value = ""
        else:
            page.snack_bar = ft.SnackBar(ft.Text("Please fill in all fields"))
            page.snack_bar.open = True
            page.update()

    # Function to delete an appointment
    def delete_appointment(appointment):
        appointments.remove(appointment)
        update_appointments_list()

    # Function to edit an appointment
    def edit_appointment(appointment):
        name_field.value = appointment["name"]
        phone_field.value = appointment["phone"]
        date_field.value = appointment["date"]
        appointments.remove(appointment)
        update_appointments_list()
        page.update()

    def update_appointments_list():
        appointments_list.controls.clear()
        for appointment in appointments:
            appointments_list.controls.append(
                ft.Row([
                ft.Text(f"Name: {appointment['name']}, Phone: {appointment['phone']}, Date: {appointment['date']}"),
                ft.ElevatedButton("Edit", on_click=lambda e, app=appointment: edit_appointment(app), bgcolor = ft.colors.YELLOW_800, color = ft.colors.WHITE),
                ft.ElevatedButton("Delete", on_click=lambda e, app=appointment: delete_appointment(app), bgcolor = ft.colors.RED_ACCENT_700, color = ft.colors.WHITE)
            ])
            )
        page.update()


    # UI elements
    title = ft.Row(
        [
            ft.Text("🦷 ", style=ft.TextStyle(size=30, color = ft.colors.BLUE)),
            ft.Text(
                "Almasa Dental Clinic",
                style=ft.TextStyle(size=24, weight=ft.FontWeight.BOLD, color=ft.colors.BLACK)
            ),
        ],
         alignment=ft.MainAxisAlignment.CENTER
    )

    doctor_name = ft.Text(
        "Dr. Mohamed",
         style=ft.TextStyle(size=18, weight=ft.FontWeight.BOLD, color=ft.colors.BLUE_GREY_900)
     ,
     )

    name_field = ft.TextField(label="Patient's Name", border_color=ft.colors.BLUE_GREY_500,
                               focused_border_color=ft.colors.BLUE, text_style=ft.TextStyle(color=ft.colors.BLACK))
    phone_field = ft.TextField(label="Phone Number", border_color=ft.colors.BLUE_GREY_500,
                               focused_border_color=ft.colors.BLUE, text_style=ft.TextStyle(color=ft.colors.BLACK))
    date_field = ft.TextField(label="Appointment Date", border_color=ft.colors.BLUE_GREY_500,
                               focused_border_color=ft.colors.BLUE, text_style=ft.TextStyle(color=ft.colors.BLACK))
    add_button = ft.ElevatedButton("Add Appointment", on_click=add_appointment, bgcolor=ft.colors.BLUE, color=ft.colors.WHITE)


    # Layout UI components with margins
    title_container = ft.Container(
        content=ft.Column([title, doctor_name],
            horizontal_alignment=ft.CrossAxisAlignment.CENTER
        ),
        bgcolor=ft.colors.LIGHT_BLUE_300,
        padding=20,
        alignment=ft.alignment.center
    )

    input_container = ft.Container(
        content=ft.Column(
            [
                name_field,
                phone_field,
                date_field,
                add_button
            ],
            horizontal_alignment=ft.CrossAxisAlignment.CENTER
        ),
        bgcolor=ft.colors.LIGHT_GREEN_100,
        padding=20,
        margin=ft.Margin(top=10, left=10, right=10, bottom=10),
        alignment=ft.alignment.center
    )

    appointments_list = ft.Column()
    appointments_container = ft.Container(
        content=ft.Column(
            [
                ft.Text("Appointment List:", style=ft.TextStyle(weight=ft.FontWeight.BOLD)),
                appointments_list
            ]
        ),
        bgcolor=ft.colors.GREY_100,
        padding=20,
        margin=ft.Margin(top=10, left=10, right=10, bottom=10)
    )

    # Add all containers to the page
    page.add(
        title_container,
        input_container,
        appointments_container
    )


if __name__ == "__main__":
    ft.app(target=main)