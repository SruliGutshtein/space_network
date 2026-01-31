import time

from space_network_lib import SpaceEntity, SpaceNetwork, Packet, TemporalInterferenceError, DataCorruptedError, LinkTerminatedError, OutOfRangeError, CommsError

class Satellite(SpaceEntity):
    def receive_signal(self, packet):
        """מדפיסה את הפקטה עם שם הלווין"""
        if isinstance(packet, RelayPacket):
            inner_packet = packet.data
            if inner_packet.receiver == self:
                print(f"[{self.name}] 🌟 MISSION ACCOMPLISHED! Received final message: {inner_packet.data}")
            else:
                print(f"[{self.name}] Unwrapping and forwarding to {inner_packet.receiver.name}")
                attempt_transmission(inner_packet)
        else:
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

class RelayPacket(Packet):
    def __init__(self, packet_to_relay, sender, proxy):
        super().__init__(data=packet_to_relay, receiver=proxy, sender= sender)

    def __repr__(self):
        return f"RelayPacket(Relaying [{self.data}] to {self.receiver} from {self.sender})"

class GroundStation(SpaceEntity):
    def receive_signal(self, packet):
        print(f"[{self.name}] Signal received (ignoring).")

def smart_send_packet(packet, entities_list):
    sorted_entities = sorted(entities_list, key=lambda x: x.distance_from_earth)
    try:
        start_index = sorted_entities.index(packet.sender)
        end_index = sorted_entities.index(packet.receiver)
    except ValueError:
        print("Error: Sender or Receiver not in the entities list!")
        return
    if start_index > end_index:
        print("Error: Currently only supporting Earth -> Space direction")
        return
    path = sorted_entities[start_index: end_index + 1]

    print(f"[Smart Router] Calculated path: {[e.name for e in path]}")
    current_packet = packet
    for i in range(len(path) - 2, -1, -1):
        sender_node = path[i]
        next_hop = path[i + 1]
        current_packet = RelayPacket(packet_to_relay=current_packet, sender=sender_node, proxy=next_hop)
    print("[Smart Router] Onion wrapping complete. Initiating launch...")
    attempt_transmission(current_packet)

network = SpaceNetwork(3)
sat1 = Satellite("Sat1", 100)
sat2 = Satellite("Sat2", 200)
sat3 = Satellite("Sat3", 300)
sat4 = Satellite("Sat4", 400)
# my_packet = Packet("היי, אחת שתיים, שומע שומע?", sat1, sat2)
# try:
#     attempt_transmission(my_packet)
# except BrokenConnectionError:
#     print("Transmission failed")
#
earth = GroundStation(name="Earth", distance_from_earth=0)
# p_final = Packet(data="Hello from Earth!!",sender=sat1, receiver=sat2)
# p_earth_to_sat1 = RelayPacket(packet_to_relay=p_final, sender=earth, proxy=sat1)
# attempt_transmission(p_earth_to_sat1)

# p_final = Packet(data="Hello From Earth!", sender=sat3, receiver=sat4)
# p_layer_3 = RelayPacket(packet_to_relay=p_final, sender=sat2, proxy=sat3)
# p_layer_2 = RelayPacket(packet_to_relay=p_layer_3, sender=sat1, proxy=sat2)
# p_layer_1 = RelayPacket(packet_to_relay=p_layer_2, sender=earth, proxy=sat1)
# attempt_transmission(p_layer_1)
all_entities = [earth, sat1, sat2, sat3, sat4]
original_packet = Packet(data="Hello from Earth to Sat4 via Smart Routing!", sender=earth, receiver=sat4)

smart_send_packet(original_packet, all_entities)