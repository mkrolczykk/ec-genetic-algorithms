import tkinter as tk
import sv_ttk
from other.events_listeners.data_storage_event_listener import DataStorageEventListener
from other.events_listeners.plot_creation_event_listener import PlotCreationEventListener
from other.events_listeners.statistics_event_listener import StatisticsEventListener
from ui.Controller import Controller
from ui.Model import Model
from ui.View import View


class Application(tk.Tk):
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)

        self.title("EC Genetic Algorithms project 1")
        self.minsize(600, 0)
        self.resizable(False, True)

        # MVC pattern
        model = Model()
        view = View(self)
        controller = Controller(model, view)

        view.set_controller(controller)

        view.pack(fill=tk.BOTH)

        sv_ttk.use_light_theme()

        event_listeners = (
            StatisticsEventListener(),
            PlotCreationEventListener(),
            DataStorageEventListener()
        )

        for event_listener in event_listeners:
            event_listener.listen()


if __name__ == "__main__":
    app = Application()
    app.mainloop()
