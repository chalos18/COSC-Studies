class RDTSender:
    """Sender-side simulation of RDT 3.0 (Alternating bit protocol)"""

    # Event codes
    DATA = 0
    ACK = 1
    TIMEOUT = 2

    # States - see FSM
    WAIT_DATA0 = 0  # Waiting for data, which will get sent with sequence number 0.
    WAIT_ACK0 = 1  # Waiting for ACK with sequence number 0.
    WAIT_DATA1 = 2  # Waiting for data, which will get sent with sequence number 1.
    WAIT_ACK1 = 3  # Waiting for ACK with sequence number 1.

    # Status codes
    ERROR = -1
    DATA_SENT = 0
    ACK_PROCESSED = 1
    RE_SENT = 2

    def __init__(self):
        self.last_sent_data = None
        self.state = self.WAIT_DATA0
        self.seq_num = 0

    def __str__(self):
        return f"RDT sender is in state {self.state}."

    def send(self, seq_num, data):
        """Call this to 'send' the given data
        with the given sequence number.
        Since we're only simulating a sender,
        this just updates last_sent_data and
        prints out the data and sequence number.
        """
        self.last_sent_data = data  # Store data in case we need to re-send it.
        print(f"Packet sent: seq #{seq_num}, data {data}")

    def go_next_state(self, current_state):
        states = [0, 1, 2, 3]
        if current_state == 3:
            self.state = 0
        else:
            self.state = states[current_state + 1]

    def process_event(self, event):
        """event format: (event_code, extra) -> tuple simulating an event"""
        event_code, extra = event

        # Data sent
        if event_code == self.DATA:  # Data event
            if self.state == self.WAIT_DATA0:
                self.send(0, extra)
                self.state = self.WAIT_ACK0
                return self.DATA_SENT
            elif self.state == self.WAIT_DATA1:
                self.send(1, extra)
                self.state = self.WAIT_ACK1
                return self.DATA_SENT

        # ACK received
        elif event_code == self.ACK:  # ACK event
            if self.state == self.WAIT_ACK0 and extra == 0:
                self.state = self.WAIT_DATA1
                return self.ACK_PROCESSED
            elif self.state == self.WAIT_ACK1 and extra == 1:
                self.state = self.WAIT_DATA0
                return self.ACK_PROCESSED

        # Timeout event
        elif event_code == self.TIMEOUT:  # Timeout event
            state_seq = {self.WAIT_ACK0: 0, self.WAIT_ACK1: 1}
            if self.state in state_seq:
                self.send(state_seq[self.state], self.last_sent_data)
                return self.RE_SENT

        return self.ERROR  # Unexpected event

def sender_test(event_list):
    sender = RDTSender()
    print(sender)
    print("-" * 10)
    for event in event_list:
        status = sender.process_event(event)
        print(f"Status: {status}")
        print(sender)
        print("-" * 10)

"""
RDT sender is in state 0.
----------
Packet sent: seq #0, data 10
Status: 0
RDT sender is in state 1.
----------
Status: 1
RDT sender is in state 2.
----------
Packet sent: seq #1, data 15
Status: 0
RDT sender is in state 3.
----------
Status: -1
RDT sender is in state 3.
----------
Status: 1
RDT sender is in state 0.
----------
Packet sent: seq #0, data 12
Status: 0
RDT sender is in state 1.
----------
Status: 1
RDT sender is in state 2.
----------
Status: -1
RDT sender is in state 2.
----------
Packet sent: seq #1, data 9
Status: 0
RDT sender is in state 3.
----------
Packet sent: seq #1, data 9
Status: 2
RDT sender is in state 3.
----------
"""
sender_test(
    [
        (0, 10),
        (1, 0),
        (0, 15),
        (1, 0),
        (1, 1),
        (0, 12),
        (1, 0),
        (1, 0),
        (0, 9),
        (2, None),
    ]
)


"""
RDT sender is in state 0.
----------
Status: -1
RDT sender is in state 0.
----------
Status: -1
RDT sender is in state 0.
----------
Packet sent: seq #0, data 50
Status: 0
RDT sender is in state 1.
----------
Status: -1
RDT sender is in state 1.
----------
Status: -1
RDT sender is in state 1.
----------
"""
# Examples of unexpected events
# sender_test([(2, None), (1, 0), (0, 50), (1, 1), (0, 30)])

"""
RDT sender is in state 0.
----------
Packet sent: seq #0, data 1
Status: 0
RDT sender is in state 1.
----------
Packet sent: seq #0, data 1
Status: 2
RDT sender is in state 1.
----------
"""
# sender_test([(0, 1), (2, None)])

"""
RDT sender is in state 0.
----------
Packet sent: seq #0, data 11
Status: 0
RDT sender is in state 1.
----------
Status: 1
RDT sender is in state 2.
----------
Packet sent: seq #1, data 22
Status: 0
RDT sender is in state 3.
----------
Packet sent: seq #1, data 22
Status: 2
RDT sender is in state 3.
----------
Status: 1
RDT sender is in state 0.
----------
"""
# sender_test([(0, 11), (1, 0), (0, 22), (2, None), (1, 1)])
