class RDTReceiver:
    """Receiver-side simulation of RDT 3.0 (Alternating bit protocol)"""

    # Status codes
    ERROR = -1
    DUPLICATE = 0
    NEW_DATA = 1

    def __init__(self):
        self.expected_seq_num = 0

    def __str__(self):
        return f"RDT receiver expects {self.expected_seq_num} next."

    def ack(self, seq_num):
        """Call this to send an ACK with the given seq number.
        Since we're only simulating a receiver, this just prints a message.
        """
        print(f"ACK {seq_num} sent.")

    def receive(self, packet):
        """packet: (seq_num, data)
        output: status
        """
        seq_num, data = packet

        if seq_num not in [0, 1]:
            return self.ERROR
        else:
            # Check if it's the expected sequence number
            if seq_num == self.expected_seq_num:
                # Send back an ACK
                self.ack(seq_num)
                # Toggle expected sequence number for the next packet
                self.expected_seq_num = 1 - self.expected_seq_num
                return self.NEW_DATA
            else:
                # Duplicate packet, send ACK again
                self.ack(seq_num)
                return self.DUPLICATE
