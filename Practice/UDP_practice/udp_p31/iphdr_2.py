import socket
import struct
import binascii

class Iphdr:
    def __init__(self, tot_len, protocol, saddr, daddr):
        self.ver_len = 0x45
        self.tos = 0
        self.tot_len = tot_len
        self.id = 0
        self.frag_off = 0
        self.ttl = 127
        self.protocol = protocol  # TCP(6)/UDP(17)
        self.check = 0
        self.saddr = socket.inet_aton(saddr)
        self.daddr = socket.inet_aton(daddr)

    def pack_Iphdr(self):
        packed = b""
        packed += struct.pack("!BBH", self.ver_len, self.tos, self.tot_len)
        packed += struct.pack("!HH", self.id, self.frag_off)
        packed += struct.pack("!BBH", self.ttl, self.protocol, self.check)
        packed += struct.pack("!4s", self.saddr)
        packed += struct.pack("!4s", self.daddr)
        return packed

    def unpack_Iphdr(buffer):
        unpacked = struct.unpack("!BBHHHBBH4s4s", buffer[:20])
        return unpacked

    def getPacketSize(unpacked_ipheader):
        return unpacked_ipheader[2]

    def getProtocolId(unpacked_ipheader):
        return unpacked_ipheader[6]

    def getIP(unpacked_ipheader):
        src_ip = socket.inet_ntoa(unpacked_ipheader[8])
        dst_ip = socket.inet_ntoa(unpacked_ipheader[9])
        return src_ip, dst_ip


if __name__ == "__main__":
    ip = Iphdr(1000, 6, "10.0.0.1", "11.0.0.1")
    packed_iphdr = ip.pack_Iphdr()
    print(binascii.b2a_hex(packed_iphdr))

    unpacked_iphdr = Iphdr.unpack_Iphdr(packed_iphdr)
    print(unpacked_iphdr)
    print(
        "Packet size:{} Protocol:{} IP:{}".format(
            Iphdr.getPacketSize(unpacked_iphdr),
            Iphdr.getProtocolId(unpacked_iphdr),
            Iphdr.getIP(unpacked_iphdr),
        )
    )
