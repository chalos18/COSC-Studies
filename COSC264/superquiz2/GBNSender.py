class GBNSender:
    """Sender-side simulation of GBN"""

    # Event constants
    DATA = 0
    ACK = 1
    TIMEOUT = 2

    # Status constants
    ERROR = -1  # unexpected event or window full
    DATA_SENT = 0
    ACK_PROCESSED = 1
    RE_SENT = 2

    def __init__(self, window_size):
        self.window_size = window_size
        self.base = 0  # seq number of lower window boundary
        self.next_seq = 0  # next available sequence number
        self.sent_messages = dict()  # seq_num: data dictionary

    def __str__(self):
        return f"GBN sender: base {self.base}, next_seq {self.next_seq}"

    def send(self, seq_num, data):
        """Call this to 'send' the given data
        with the given sequence number.
        Since we're only simulating a sender,
        this just updates the sent_messages dict and
        prints out the data and sequence number.
        """
        self.sent_messages[seq_num] = data  # Store data in case we need to re-send it.
        print(f"Packet sent: seq #{seq_num}, data {data}")

    def process_event(self, event):
        """event: [event_code, extra]
         extra is:
               data for data events
               sequence number for ACK events
               None for timeout events
        output: status
        """
        event_code, extra = event[0], event[1]
        current_window_size = self.next_seq - self.base

        # checking if window is full
        if event_code == self.DATA:
            if current_window_size < self.window_size:  # we can send more data
                self.send(self.next_seq, extra)
                self.next_seq += 1
                return self.DATA_SENT
            else:
                return self.ERROR  # window is full

        if event_code == self.ACK:
            # extra is the seq_number of the packet being acknowledged
            if extra in range(self.base, self.next_seq):
                # slide the window
                while self.base <= extra:
                    self.base += 1
                return self.ACK_PROCESSED
            else:
                return self.ERROR

        if event_code == self.TIMEOUT:
            # re send all unACKed packets, pulling
            # the necessary data from the sent_messages dictionary
            for seq_num in range(self.base, self.next_seq):
                self.send(seq_num, self.sent_messages[seq_num])
            return self.RE_SENT

        return self.ERROR  # Unexpected event


def sender_test(event_list):
    sender = GBNSender(4)
    print(sender)
    print("-" * 10)
    for event in event_list:
        status = sender.process_event(event)
        print(f"Status: {status}")
        print(sender)
        print("-" * 10)

"""
GBN sender: base 0, next_seq 0
----------
Status: -1
GBN sender: base 0, next_seq 0
----------
"""
sender_test([(1, 0)])

"""
GBN sender: base 0, next_seq 0
----------
Packet sent: seq #0, data 1
Status: 0
GBN sender: base 0, next_seq 1
----------
Status: 1
GBN sender: base 1, next_seq 1
----------
"""
# sender_test([(0, 1), (1, 0)])

"""
GBN sender: base 0, next_seq 0
----------
Packet sent: seq #0, data 1
Status: 0
GBN sender: base 0, next_seq 1
----------
Packet sent: seq #1, data 2
Status: 0
GBN sender: base 0, next_seq 2
----------
Packet sent: seq #0, data 1
Packet sent: seq #1, data 2
Status: 2
GBN sender: base 0, next_seq 2
----------
"""
# sender_test([(0, 1), (0, 2), (2, None)])

"""
GBN sender: base 0, next_seq 0
----------
Packet sent: seq #0, data 1
Status: 0
GBN sender: base 0, next_seq 1
----------
Packet sent: seq #1, data 2
Status: 0
GBN sender: base 0, next_seq 2
----------
Packet sent: seq #2, data 3
Status: 0
GBN sender: base 0, next_seq 3
----------
Status: 1
GBN sender: base 2, next_seq 3
----------
Packet sent: seq #2, data 3
Status: 2
GBN sender: base 2, next_seq 3
----------
"""
# sender_test([(0, 1), (0, 2), (0, 3), (1, 1), (2, None)])
