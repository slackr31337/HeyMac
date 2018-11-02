#!/usr/bin/env python3


import unittest

import heymac


class TestHeyMacFrame(unittest.TestCase):
    """Tests the heymac.HeyMacFrame packing and unpacking.
    Each test function should test pack and unpack of the same data.
    """

    def test_min(self,):
        # Pack
        f = heymac.HeyMacFrame()
        f.fctl_type = heymac.HeyMacFrame.FCTL_TYPE_MIN
        b = bytes(f)
        self.assertEqual(b, b"\x00")
        # Unpack
        f = heymac.HeyMacFrame(b)
        self.assertEqual(f.fctl_type, heymac.HeyMacFrame.FCTL_TYPE_MIN)
        self.assertEqual(f.fctl_l, 0)
        self.assertEqual(f.fctl_r, 0)
        self.assertEqual(f.fctl_n, 0)
        self.assertEqual(f.fctl_d, 0)
        self.assertEqual(f.fctl_i, 0)
        self.assertEqual(f.fctl_s, 0)
        self.assertEqual(f.raddr, b"")
        self.assertEqual(f.pend, b"")
        self.assertEqual(f.ver, b"")
        self.assertEqual(f.seq, b"")
        self.assertEqual(f.exttype, b"")
        self.assertEqual(f.netid, b"")
        self.assertEqual(f.daddr, b"")
        self.assertEqual(f.saddr, b"")
        self.assertEqual(f.data, b"")

    def test_mac(self,):
        # Pack
        f = heymac.HeyMacFrame()
        f.fctl_type = heymac.HeyMacFrame.FCTL_TYPE_MAC
        b = bytes(f)
        self.assertEqual(b, b"\x40\x10")
        # Unpack
        f = heymac.HeyMacFrame(b)
        self.assertEqual(f.fctl_type, heymac.HeyMacFrame.FCTL_TYPE_MAC)
        self.assertEqual(f.fctl_l, 0)
        self.assertEqual(f.fctl_r, 0)
        self.assertEqual(f.fctl_n, 0)
        self.assertEqual(f.fctl_d, 0)
        self.assertEqual(f.fctl_i, 0)
        self.assertEqual(f.fctl_s, 0)
        self.assertEqual(f.raddr, b"")
        self.assertEqual(f.pend, 0)
        self.assertEqual(f.ver, 1)
        self.assertEqual(f.seq, 0)
        self.assertEqual(f.exttype, b"")
        self.assertEqual(f.netid, b"")
        self.assertEqual(f.daddr, b"")
        self.assertEqual(f.saddr, b"")
        self.assertEqual(f.data, b"")

    def test_net(self,):
        # Pack
        f = heymac.HeyMacFrame()
        f.fctl_type = heymac.HeyMacFrame.FCTL_TYPE_NET
        b = bytes(f)
        self.assertEqual(b, b"\x80\x10")
        # Unpack
        f = heymac.HeyMacFrame(b)
        self.assertEqual(f.fctl_type, heymac.HeyMacFrame.FCTL_TYPE_NET)
        self.assertEqual(f.fctl_l, 0)
        self.assertEqual(f.fctl_r, 0)
        self.assertEqual(f.fctl_n, 0)
        self.assertEqual(f.fctl_d, 0)
        self.assertEqual(f.fctl_i, 0)
        self.assertEqual(f.fctl_s, 0)
        self.assertEqual(f.raddr, b"")
        self.assertEqual(f.pend, 0)
        self.assertEqual(f.ver, 1)
        self.assertEqual(f.seq, 0)
        self.assertEqual(f.exttype, b"")
        self.assertEqual(f.netid, b"")
        self.assertEqual(f.daddr, b"")
        self.assertEqual(f.saddr, b"")
        self.assertEqual(f.data, b"")

    def test_ext_using_fctl(self,):
        # Pack
        f = heymac.HeyMacFrame()
        f.fctl_type = heymac.HeyMacFrame.FCTL_TYPE_EXT
        b = bytes(f)
        self.assertEqual(b, b"\xC0\x10\x00")
        # Unpack
        f = heymac.HeyMacFrame(b)
        self.assertEqual(f.fctl_type, heymac.HeyMacFrame.FCTL_TYPE_EXT)
        self.assertEqual(f.fctl_l, 0)
        self.assertEqual(f.fctl_r, 0)
        self.assertEqual(f.fctl_n, 0)
        self.assertEqual(f.fctl_d, 0)
        self.assertEqual(f.fctl_i, 0)
        self.assertEqual(f.fctl_s, 0)
        self.assertEqual(f.raddr, b"")
        self.assertEqual(f.pend, 0)
        self.assertEqual(f.ver, 1)
        self.assertEqual(f.seq, 0)
        self.assertEqual(f.exttype, 0)
        self.assertEqual(f.netid, b"")
        self.assertEqual(f.daddr, b"")
        self.assertEqual(f.saddr, b"")
        self.assertEqual(f.data, b"")

    def test_ext_using_field(self,):
        # Pack
        f = heymac.HeyMacFrame()
        f.exttype = b"\x05"
        b = bytes(f)
        self.assertEqual(b, b"\xC0\x10\x05")
        # Unpack
        f = heymac.HeyMacFrame(b)
        self.assertEqual(f.fctl_type, heymac.HeyMacFrame.FCTL_TYPE_EXT)
        self.assertEqual(f.fctl_l, 0)
        self.assertEqual(f.fctl_r, 0)
        self.assertEqual(f.fctl_n, 0)
        self.assertEqual(f.fctl_d, 0)
        self.assertEqual(f.fctl_i, 0)
        self.assertEqual(f.fctl_s, 0)
        self.assertEqual(f.raddr, b"")
        self.assertEqual(f.pend, 0)
        self.assertEqual(f.ver, 1)
        self.assertEqual(f.seq, 0)
        self.assertEqual(f.exttype, 5)
        self.assertEqual(f.netid, b"")
        self.assertEqual(f.daddr, b"")
        self.assertEqual(f.saddr, b"")
        self.assertEqual(f.data, b"")

    def test_min_payld(self,):
        # Pack
        f = heymac.HeyMacFrame()
        f.fctl_type = heymac.HeyMacFrame.FCTL_TYPE_MIN
        f.data = b"ABCD"
        b = bytes(f)
        self.assertEqual(b, b"\x00ABCD")
        # Unpack
        f = heymac.HeyMacFrame(b)
        self.assertEqual(f.fctl_type, heymac.HeyMacFrame.FCTL_TYPE_MIN)
        self.assertEqual(f.fctl_l, 0)
        self.assertEqual(f.fctl_r, 0)
        self.assertEqual(f.fctl_n, 0)
        self.assertEqual(f.fctl_d, 0)
        self.assertEqual(f.fctl_i, 0)
        self.assertEqual(f.fctl_s, 0)
        self.assertEqual(f.raddr, b"")
        self.assertEqual(f.pend, b"")
        self.assertEqual(f.ver, b"")
        self.assertEqual(f.seq, b"")
        self.assertEqual(f.exttype, b"")
        self.assertEqual(f.netid, b"")
        self.assertEqual(f.daddr, b"")
        self.assertEqual(f.saddr, b"")
        self.assertEqual(f.data, b"ABCD")

    def test_mac_verseq(self,):
        # Pack
        f = heymac.HeyMacFrame()
        f.fctl_type = heymac.HeyMacFrame.FCTL_TYPE_MAC
        f.seq = 7
        b = bytes(f)
        self.assertEqual(b, b"\x40\x17")
        # Unpack
        f = heymac.HeyMacFrame(b)
        self.assertEqual(f.fctl_type, heymac.HeyMacFrame.FCTL_TYPE_MAC)
        self.assertEqual(f.fctl_l, 0)
        self.assertEqual(f.fctl_r, 0)
        self.assertEqual(f.fctl_n, 0)
        self.assertEqual(f.fctl_d, 0)
        self.assertEqual(f.fctl_i, 0)
        self.assertEqual(f.fctl_s, 0)
        self.assertEqual(f.raddr, b"")
        self.assertEqual(f.pend, 0)
        self.assertEqual(f.ver, 1)
        self.assertEqual(f.seq, 7)
        self.assertEqual(f.exttype, b"")
        self.assertEqual(f.netid, b"")
        self.assertEqual(f.daddr, b"")
        self.assertEqual(f.saddr, b"")
        self.assertEqual(f.data, b"")

    def test_min_saddr64b(self,):
        # Pack
        f = heymac.HeyMacFrame()
        f.fctl_type = heymac.HeyMacFrame.FCTL_TYPE_MIN
        f.saddr = b"\x01\x02\x03\x04\x05\x06\x07\x08"
        b = bytes(f)
        self.assertEqual(b, b"\x21\x01\x02\x03\x04\x05\x06\x07\x08")
        # Unpack
        f = heymac.HeyMacFrame(b)
        self.assertEqual(f.fctl_type, heymac.HeyMacFrame.FCTL_TYPE_MIN)
        self.assertEqual(f.fctl_l, 1)
        self.assertEqual(f.fctl_r, 0)
        self.assertEqual(f.fctl_n, 0)
        self.assertEqual(f.fctl_d, 0)
        self.assertEqual(f.fctl_i, 0)
        self.assertEqual(f.fctl_s, 1)
        self.assertEqual(f.raddr, b"")
        self.assertEqual(f.pend, b"")
        self.assertEqual(f.ver, b"")
        self.assertEqual(f.seq, b"")
        self.assertEqual(f.exttype, b"")
        self.assertEqual(f.netid, b"")
        self.assertEqual(f.daddr, b"")
        self.assertEqual(f.saddr, b"\x01\x02\x03\x04\x05\x06\x07\x08")
        self.assertEqual(f.data, b"")

    def test_mac_verseq_saddr64b(self,):
        # Pack
        f = heymac.HeyMacFrame()
        f.fctl_type = heymac.HeyMacFrame.FCTL_TYPE_MAC
        f.seq = 9
        f.saddr = b"\x01\x02\x03\x04\x05\x06\x07\x08"
        b = bytes(f)
        self.assertEqual(b, b"\x61\x19\x01\x02\x03\x04\x05\x06\x07\x08")
        # Unpack
        f = heymac.HeyMacFrame(b)
        self.assertEqual(f.fctl_type, heymac.HeyMacFrame.FCTL_TYPE_MAC)
        self.assertEqual(f.fctl_l, 1)
        self.assertEqual(f.fctl_r, 0)
        self.assertEqual(f.fctl_n, 0)
        self.assertEqual(f.fctl_d, 0)
        self.assertEqual(f.fctl_i, 0)
        self.assertEqual(f.fctl_s, 1)
        self.assertEqual(f.raddr, b"")
        self.assertEqual(f.pend, 0)
        self.assertEqual(f.ver, 1)
        self.assertEqual(f.seq, 9)
        self.assertEqual(f.exttype, b"")
        self.assertEqual(f.netid, b"")
        self.assertEqual(f.daddr, b"")
        self.assertEqual(f.saddr, b"\x01\x02\x03\x04\x05\x06\x07\x08")
        self.assertEqual(f.data, b"")

    def test_mac_len_verseq_saddr16b_beacon(self,):
        # Pack
        f = heymac.HeyMacFrame()
        f.fctl_type = heymac.HeyMacFrame.FCTL_TYPE_MAC
        f.seq = 2
        f.saddr = b"\x11\x12"
        bcn = heymac.mac_cmds.HeyMacCmdSbcn(
            bcn_en=1,
            sf_order=5,
            eb_order=7,
            dscpln=2,
            caps=3,
            status=4,
            asn=42,
        )
        f.data = bytes(bcn)
        b = bytes(f)
        self.assertEqual(b, b"\x41\x12\x11\x12\x01\xf5\x02\x03\x04\x00\x00\x00\x2a\x00\x00\x00\x00\x00\x00\x00\x00")
        # Unpack
        f = heymac.HeyMacFrame(b)
        self.assertEqual(f.fctl_type, heymac.HeyMacFrame.FCTL_TYPE_MAC)
        self.assertEqual(f.fctl_l, 0)
        self.assertEqual(f.fctl_r, 0)
        self.assertEqual(f.fctl_n, 0)
        self.assertEqual(f.fctl_d, 0)
        self.assertEqual(f.fctl_i, 0)
        self.assertEqual(f.fctl_s, 1)
        self.assertEqual(f.raddr, b"")
        self.assertEqual(f.pend, 0)
        self.assertEqual(f.ver, 1)
        self.assertEqual(f.seq, 2)
        self.assertEqual(f.exttype, b"")
        self.assertEqual(f.netid, b"")
        self.assertEqual(f.daddr, b"")
        self.assertEqual(f.saddr, b"\x11\x12")
        self.assertEqual(type(f.data), heymac.mac_cmds.HeyMacCmdSbcn)
        self.assertEqual(f.data.bcn_en, 1)
        self.assertEqual(f.data.sf_order, 5)
        self.assertEqual(f.data.eb_order, 7)
        self.assertEqual(f.data.dscpln, 2)
        self.assertEqual(f.data.caps, 3)
        self.assertEqual(f.data.status, 4)
        self.assertEqual(f.data.asn, 42)

    def test_mac_len_verseq_saddr64b(self,):
        # Pack
        f = heymac.HeyMacFrame()
        f.fctl_type = heymac.HeyMacFrame.FCTL_TYPE_MAC
        f.seq = 2
        f.saddr = b"\x01\x02\x03\x04\x05\x06\x07\x08"
        b = bytes(f)
        self.assertEqual(b, b"\x61\x12\x01\x02\x03\x04\x05\x06\x07\x08")
        # Unpack
        f = heymac.HeyMacFrame(b)
        self.assertEqual(f.fctl_type, heymac.HeyMacFrame.FCTL_TYPE_MAC)
        self.assertEqual(f.fctl_l, 1)
        self.assertEqual(f.fctl_r, 0)
        self.assertEqual(f.fctl_n, 0)
        self.assertEqual(f.fctl_d, 0)
        self.assertEqual(f.fctl_i, 0)
        self.assertEqual(f.fctl_s, 1)
        self.assertEqual(f.raddr, b"")
        self.assertEqual(f.pend, 0)
        self.assertEqual(f.ver, 1)
        self.assertEqual(f.seq, 2)
        self.assertEqual(f.exttype, b"")
        self.assertEqual(f.netid, b"")
        self.assertEqual(f.daddr, b"")
        self.assertEqual(f.saddr, b"\x01\x02\x03\x04\x05\x06\x07\x08")
        self.assertEqual(f.data, b"")

    def test_mac_len_verseq_saddr64b_daddr64b(self,):
        # Pack
        f = heymac.HeyMacFrame()
        f.fctl_type = heymac.HeyMacFrame.FCTL_TYPE_MAC
        f.daddr = b"\xd1\xd2\xd3\xd4\xd5\xd6\xd7\xd8"
        f.saddr = b"\xc1\xc2\xc3\xc4\xc5\xc6\xc7\xc8"
        f.data = b"hi"
        b = bytes(f)
        self.assertEqual(b, b"\x65\x10\xd1\xd2\xd3\xd4\xd5\xd6\xd7\xd8\xc1\xc2\xc3\xc4\xc5\xc6\xc7\xc8hi")
        # Unpack
        f = heymac.HeyMacFrame(b)
        self.assertEqual(f.fctl_type, heymac.HeyMacFrame.FCTL_TYPE_MAC)
        self.assertEqual(f.fctl_l, 1)
        self.assertEqual(f.fctl_r, 0)
        self.assertEqual(f.fctl_n, 0)
        self.assertEqual(f.fctl_d, 1)
        self.assertEqual(f.fctl_i, 0)
        self.assertEqual(f.fctl_s, 1)
        self.assertEqual(f.raddr, b"")
        self.assertEqual(f.pend, 0)
        self.assertEqual(f.ver, 1)
        self.assertEqual(f.seq, 0)
        self.assertEqual(f.exttype, b"")
        self.assertEqual(f.netid, b"")
        self.assertEqual(f.daddr, b"\xd1\xd2\xd3\xd4\xd5\xd6\xd7\xd8")
        self.assertEqual(f.saddr, b"\xc1\xc2\xc3\xc4\xc5\xc6\xc7\xc8")
        self.assertEqual(f.data, b"hi")

    def test_mac_len_verseq_saddr16b_daddr16b(self,):
        # Pack
        f = heymac.HeyMacFrame()
        f.fctl_type = heymac.HeyMacFrame.FCTL_TYPE_MAC
        f.daddr = b"\xd1\xd2"
        f.saddr = b"\xc1\xc2"
        f.data = b"hello world"
        b = bytes(f)
        self.assertEqual(b, b"\x45\x10\xd1\xd2\xc1\xc2hello world")
        # Unpack
        f = heymac.HeyMacFrame(b)
        self.assertEqual(f.fctl_type, heymac.HeyMacFrame.FCTL_TYPE_MAC)
        self.assertEqual(f.fctl_l, 0)
        self.assertEqual(f.fctl_r, 0)
        self.assertEqual(f.fctl_n, 0)
        self.assertEqual(f.fctl_d, 1)
        self.assertEqual(f.fctl_i, 0)
        self.assertEqual(f.fctl_s, 1)
        self.assertEqual(f.raddr, b"")
        self.assertEqual(f.pend, 0)
        self.assertEqual(f.ver, 1)
        self.assertEqual(f.seq, 0)
        self.assertEqual(f.exttype, b"")
        self.assertEqual(f.netid, b"")
        self.assertEqual(f.daddr, b"\xd1\xd2")
        self.assertEqual(f.saddr, b"\xc1\xc2")
        self.assertEqual(f.data, b"hello world")

    def test_net_data(self,):
        # Pack
        f = heymac.HeyMacFrame()
        f.fctl_type = heymac.HeyMacFrame.FCTL_TYPE_NET
        f.data = heymac.APv6Frame()
        b = bytes(f)
        self.assertEqual(b, b"\x80\x10\xD7")
        # Unpack
        f = heymac.HeyMacFrame(b)
        self.assertEqual(f.fctl_type, heymac.HeyMacFrame.FCTL_TYPE_NET)
        self.assertEqual(f.fctl_l, 0)
        self.assertEqual(f.fctl_r, 0)
        self.assertEqual(f.fctl_n, 0)
        self.assertEqual(f.fctl_d, 0)
        self.assertEqual(f.fctl_i, 0)
        self.assertEqual(f.fctl_s, 0)
        self.assertEqual(f.raddr, b"")
        self.assertEqual(f.pend, 0)
        self.assertEqual(f.ver, 1)
        self.assertEqual(f.seq, 0)
        self.assertEqual(f.exttype, b"")
        self.assertEqual(f.netid, b"")
        self.assertEqual(f.daddr, b"")
        self.assertEqual(f.saddr, b"")
        self.assertEqual(type(f.data), heymac.APv6Frame)


    def test_ext_data(self,):
        # Pack
        f = heymac.HeyMacFrame()
        f.fctl_type = heymac.HeyMacFrame.FCTL_TYPE_EXT
        f.raddr = b"\x11\x11"
        f.exttype = b"\x2A"
        f.data = b"6x7"
        b = bytes(f)
        self.assertEqual(b, b"\xD0\x11\x11\x10\x2A6x7")
        # Unpack
        f = heymac.HeyMacFrame(b)
        self.assertEqual(f.fctl_type, heymac.HeyMacFrame.FCTL_TYPE_EXT)
        self.assertEqual(f.fctl_l, 0)
        self.assertEqual(f.fctl_r, 1)
        self.assertEqual(f.fctl_n, 0)
        self.assertEqual(f.fctl_d, 0)
        self.assertEqual(f.fctl_i, 0)
        self.assertEqual(f.fctl_s, 0)
        self.assertEqual(f.raddr, b"\x11\x11")
        self.assertEqual(f.pend, 0)
        self.assertEqual(f.ver, 1)
        self.assertEqual(f.seq, 0)
        self.assertEqual(f.exttype, 42)
        self.assertEqual(f.netid, b"")
        self.assertEqual(f.daddr, b"")
        self.assertEqual(f.saddr, b"")
        self.assertEqual(f.data, b"6x7")


    def test_raddr_pvs(self,):
        """Tests a frame with raddr and _pvs field present
        to ensure fields are in proper order
        """
        # Pack
        f = heymac.HeyMacFrame()
        f.fctl_type = heymac.HeyMacFrame.FCTL_TYPE_MAC
        f.raddr = b"\x11\x11"
        f.seq = 9
        f.data = b"6x7"
        b = bytes(f)
        self.assertEqual(b, b"\x50\x11\x11\x196x7")
        # Unpack
        f = heymac.HeyMacFrame(b)
        self.assertEqual(f.fctl_type, heymac.HeyMacFrame.FCTL_TYPE_MAC)
        self.assertEqual(f.fctl_l, 0)
        self.assertEqual(f.fctl_r, 1)
        self.assertEqual(f.fctl_n, 0)
        self.assertEqual(f.fctl_d, 0)
        self.assertEqual(f.fctl_i, 0)
        self.assertEqual(f.fctl_s, 0)
        self.assertEqual(f.raddr, b"\x11\x11")
        self.assertEqual(f.pend, 0)
        self.assertEqual(f.ver, 1)
        self.assertEqual(f.seq, 9)
        self.assertEqual(f.exttype, b"")
        self.assertEqual(f.netid, b"")
        self.assertEqual(f.daddr, b"")
        self.assertEqual(f.saddr, b"")
        self.assertEqual(f.data, b"6x7")


    def test_exttype_netid(self,):
        """Tests a frame with raddr and _pvs field present
        to ensure fields are in proper order
        """
        # Pack
        f = heymac.HeyMacFrame()
        f.fctl_type = heymac.HeyMacFrame.FCTL_TYPE_MAC
        f.exttype = 3
        f.netid = 0x80A5
        f.data = b"data"
        b = bytes(f)
        self.assertEqual(b, b"\xC8\x10\x03\x80\xa5data")
        # Unpack
        f = heymac.HeyMacFrame(b)
        self.assertEqual(f.fctl_type, heymac.HeyMacFrame.FCTL_TYPE_EXT)
        self.assertEqual(f.fctl_l, 0)
        self.assertEqual(f.fctl_r, 0)
        self.assertEqual(f.fctl_n, 1)
        self.assertEqual(f.fctl_d, 0)
        self.assertEqual(f.fctl_i, 0)
        self.assertEqual(f.fctl_s, 0)
        self.assertEqual(f.raddr, b"")
        self.assertEqual(f.pend, 0)
        self.assertEqual(f.ver, 1)
        self.assertEqual(f.seq, 0)
        self.assertEqual(f.exttype, 3)
        self.assertEqual(f.netid, b"\x80\xA5")
        self.assertEqual(f.daddr, b"")
        self.assertEqual(f.saddr, b"")
        self.assertEqual(f.data, b"data")


    def test_netid_daddr(self,):
        """Tests a frame with raddr and _pvs field present
        to ensure fields are in proper order
        """
        # Pack
        f = heymac.HeyMacFrame()
        f.fctl_type = heymac.HeyMacFrame.FCTL_TYPE_MAC
        f.netid = 0x80A5
        f.daddr = 0xd1d2
        f.data = b"data"
        b = bytes(f)
        self.assertEqual(b, b"\x4C\x10\x80\xa5\xd1\xd2data")
        # Unpack
        f = heymac.HeyMacFrame(b)
        self.assertEqual(f.fctl_type, heymac.HeyMacFrame.FCTL_TYPE_MAC)
        self.assertEqual(f.fctl_l, 0)
        self.assertEqual(f.fctl_r, 0)
        self.assertEqual(f.fctl_n, 1)
        self.assertEqual(f.fctl_d, 1)
        self.assertEqual(f.fctl_i, 0)
        self.assertEqual(f.fctl_s, 0)
        self.assertEqual(f.raddr, b"")
        self.assertEqual(f.pend, 0)
        self.assertEqual(f.ver, 1)
        self.assertEqual(f.seq, 0)
        self.assertEqual(f.exttype, b"")
        self.assertEqual(f.netid, b"\x80\xA5")
        self.assertEqual(f.daddr, b"\xd1\xd2")
        self.assertEqual(f.saddr, b"")
        self.assertEqual(f.data, b"data")


if __name__ == '__main__':
    unittest.main()
