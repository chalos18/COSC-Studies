class GBNReceiver:
    """Receiver-side simulation of GBN"""

    # Status constants
    ERROR = -1
    ACKED = 0

    def __init__(self):
        self.expected_seq_num = 1

    def __str__(self):
        return f"GBN receiver expects {self.expected_seq_num} next."

    def ack(self, seq_num):
        """Call this to send an ACK with the given seq number.
        Since we're only simulating a receiver, this just prints a message.
        """
        print(f"ACK {seq_num} sent.")

    def receive(self, packet):
        """packet: (seq_num, data)
        output: status
        """
        seq_numb, data = packet
        if seq_numb == self.expected_seq_num:
            self.ack(seq_numb)
            self.expected_seq_num = self.expected_seq_num + 1
            return self.ACKED
        else:
            self.ack(self.expected_seq_num-1)
            return self.ERROR


def receiver_test(packet_list):
    receiver = GBNReceiver()
    for packet in packet_list:
        status = receiver.receive(packet)
        print(f"Status: {status}")
        print(receiver)
        print("-" * 10)


"""
ACK 1 sent.
Status: 0
GBN receiver expects 2 next.
----------
"""
# receiver_test([(1, 1)])

"""
ACK 1 sent.
Status: 0
GBN receiver expects 2 next.
----------
ACK 2 sent.
Status: 0
GBN receiver expects 3 next.
----------
ACK 3 sent.
Status: 0
GBN receiver expects 4 next.
----------
"""
# receiver_test([(1, 1), (2, 2), (3, 3)])

"""
ACK 1 sent.
Status: 0
GBN receiver expects 2 next.
----------
ACK 2 sent.
Status: 0
GBN receiver expects 3 next.
----------
ACK 2 sent.
Status: -1
GBN receiver expects 3 next.
----------
"""
# receiver_test([(1, 1), (2, 2), (4, 3)])
