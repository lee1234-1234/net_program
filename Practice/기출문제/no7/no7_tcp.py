#안나올거같음
import struct
import binascii

class Tcphdr:
    def __init__(self, srcport, dstport, seqnum, acknum, data_offset, flags, window, checksum, urg_pointer):
        self.srcport = srcport
        self.dstport = dstport
        self.seqnum = seqnum
        self.acknum = acknum
        self.data_offset = data_offset
        self.flags = flags
        self.window = window
        self.checksum = checksum
        self.urg_pointer = urg_pointer

    def pack_Tcphdr(self):
        packed = b''
        # Pack the TCP header fields using struct.pack
        packed += struct.pack('!HH', self.srcport, self.dstport)  # Source port, destination port
        packed += struct.pack('!LL', self.seqnum, self.acknum)   # Sequence number, acknowledgment number
        packed += struct.pack('!BB', (self.data_offset << 4) + self.flags, self.window)  # Data offset + flags, window size
        packed += struct.pack('!HH', self.checksum, self.urg_pointer)  # Checksum, urgent pointer
        return packed

# Example TCP header
tcp = Tcphdr(
    srcport=5555, 
    dstport=80, 
    seqnum=12345, 
    acknum=0, 
    data_offset=5,  # 5 is the minimum data offset (no options)
    flags=2,        # SYN flag (0x02)
    window=1024, 
    checksum=0xFFFF, 
    urg_pointer=0
)

# Pack the TCP header
packed_tcphdr = tcp.pack_Tcphdr()
print("Packed TCP Header:", binascii.b2a_hex(packed_tcphdr))

# Unpack function
def unpack_Tcphdr(buffer):
    unpacked = struct.unpack('!HHLLBBHH', buffer[:20])  # 20 bytes for TCP header
    return unpacked

# Unpack the packed TCP header
unpacked_tcphdr = unpack_Tcphdr(packed_tcphdr)
print("Unpacked TCP Header:", unpacked_tcphdr)

# Extract fields from the unpacked TCP header
def getSrcPort(unpacked_tcphdr):
    return unpacked_tcphdr[0]

def getDstPort(unpacked_tcphdr):
    return unpacked_tcphdr[1]

def getSeqNum(unpacked_tcphdr):
    return unpacked_tcphdr[2]

def getAckNum(unpacked_tcphdr):
    return unpacked_tcphdr[3]

def getFlags(unpacked_tcphdr):
    return unpacked_tcphdr[5]

def getWindow(unpacked_tcphdr):
    return unpacked_tcphdr[6]

def getChecksum(unpacked_tcphdr):
    return unpacked_tcphdr[7]

# Print extracted fields
print('Source Port: {} Destination Port: {} Sequence Number: {} Acknowledgment Number: {} Flags: {} Window: {} Checksum: {}'.format(
    getSrcPort(unpacked_tcphdr),
    getDstPort(unpacked_tcphdr),
    getSeqNum(unpacked_tcphdr),
    getAckNum(unpacked_tcphdr),
    getFlags(unpacked_tcphdr),
    getWindow(unpacked_tcphdr),
    getChecksum(unpacked_tcphdr)
))
