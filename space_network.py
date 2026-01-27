import time

from space_network_lib import SpaceEntity, SpaceNetwork, Packet, TemporalInterferenceError, DataCorruptedError

class Satellite(SpaceEntity):
    def receive_signal(self, packet):
        """מדפיסה את הפקטה עם שם הלווין"""
        print(f"[{self.name}] Received: {packet}")

def attempt_transmission(packet):
    success = False
    while not success:
        try:
            network.send(packet)
            success = True
        except TemporalInterferenceError:
            print("Temporary interference, please retry")
            time.sleep(2)
        except DataCorruptedError:
            print("Data corrupted during transmission")







network = SpaceNetwork(2)
sat1 = Satellite("Sat1", 100)
sat2 = Satellite("Sat2", 200)
my_packet = Packet("היי, אחת שתיים, שומע שומע?", sat1, sat2)
network.send(my_packet)