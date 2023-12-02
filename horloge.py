import threading
import time

class HorlogeDigital:
    def __init__(self):
        self.current_time = time.localtime()
        self.alarm_time = None
        self.display_mode = 24  
        self.paused = False
        self._update_thread = threading.Thread(target=self._update_time, daemon=True)
        self._update_thread.start()

    def _update_time(self):
        while True:
            if not self.paused:
                self.current_time = time.localtime()
                self.display_time()
                self.check_alarm()
            time.sleep(1)

    def display_time(self):
        if self.display_mode == 24:
            print(time.strftime("%H:%M:%S", self.current_time))
        else:
            print(time.strftime("%I:%M:%S %p", self.current_time))

    def set_time(self, time_tuple):
        """ Temp. """
        self.current_time = time.struct_time((2023, 1, 1, time_tuple[0], time_tuple[1], time_tuple[2], 0, 1, -1))

    def set_alarm(self, alarm_time):
        """ Alarm. """
        self.alarm_time = alarm_time

    def check_alarm(self):
        """ vérifier si le temp actuel correspond avec celui de l'alarm. """
        if self.alarm_time and (self.current_time.tm_hour, self.current_time.tm_min, self.current_time.tm_sec) == self.alarm_time:
            print("ALARM! Time is:", time.strftime("%H:%M:%S", self.current_time))
            self.alarm_time = None 

    def toggle_display_mode(self):
        """ bascule entre le mode 12-heur et 24-heur du mode d'affichage """
        self.display_mode = 12 if self.display_mode == 24 else 24

    def pause_clock(self):
        """ met en Pause l'horloge. """
        self.paused = True

    def resume_clock(self):
        """ Resume l'horloge. """
        self.paused = False


clock = HorlogeDigital()
clock.set_time((8, 30, 0))
clock.set_alarm((8, 30, 5))
clock.toggle_display_mode() 