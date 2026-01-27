from space_network_lib import SpaceEntity, SpaceNetwork, Packet

class Satellite(SpaceEntity):
    def receive_signal(self, packet):
        """מדפיסה את הפקטה עם שם הלווין"""
        print(f"[{self.name}] Received: {packet}")

space_network = SpaceNetwork(1)
sat1 = Satellite("Sat1", 100)
sat2 = Satellite("Sat2", 200)
my_packet = Packet("היי, אחת שתיים, שומע שומע?", sat1, sat2)
space_network.send(my_packet)