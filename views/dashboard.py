

def DashboardView(page, ft, Pyre):
    


    myFirebase = Pyre(page)
    my_data = myFirebase.get_data()

    return ft.Column(
        [ft.Text("Dashboard"),
            ft.Text(my_data)])