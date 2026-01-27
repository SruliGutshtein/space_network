from space_network_lib import SpaceEntity

class Satellite(SpaceEntity):
    def receive_signal(self, packet):
        """מדפיסה את הפקטה עם שם הלווין"""
        print(f"[{self.name}] Received: {packet}")