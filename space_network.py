import time

from space_network_lib import SpaceEntity, SpaceNetwork, Packet, TemporalInterferenceError, DataCorruptedError, LinkTerminatedError, OutOfRangeError, CommsError

class Satellite(SpaceEntity):
    def receive_signal(self, packet):
        """מדפיסה את הפקטה עם שם הלווין"""
        print(f"[{self.name}] Received: {packet}")


class BrokenConnectionError(CommsError):
    pass
def attempt_transmission(packet):
    success = False
    while not success:
        try:
            network.send(packet)
            success = True
        except TemporalInterferenceError:
            print("Temporary interruption, please wait while I try again")
            time.sleep(2)
        except DataCorruptedError:
            print("Data corrupted during transmission")
        except LinkTerminatedError:
            print("Link lost")
            raise BrokenConnectionError("Transmission failed")
        except OutOfRangeError:
            print("Target out of range")
            raise BrokenConnectionError("Transmission failed")







network = SpaceNetwork(3)
sat1 = Satellite("Sat1", 100)
sat2 = Satellite("Sat2", 200)
my_packet = Packet("היי, אחת שתיים, שומע שומע?", sat1, sat2)
attempt_transmission(my_packet)

