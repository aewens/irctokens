import unittest
import irctokens

class HostmaskTest(unittest.TestCase):
    def test_all(self):
        hostmask = irctokens.Hostmask("nick!user@host")
        self.assertEqual(hostmask.nickname, "nick")
        self.assertEqual(hostmask.username, "user")
        self.assertEqual(hostmask.hostname, "host")

    def test_no_hostname(self):
        hostmask = irctokens.Hostmask("nick!user")
        self.assertEqual(hostmask.nickname, "nick")
        self.assertEqual(hostmask.username, "user")
        self.assertIsNone(hostmask.hostname)

    def test_no_ident(self):
        hostmask = irctokens.Hostmask("nick@host")
        self.assertEqual(hostmask.nickname, "nick")
        self.assertIsNone(hostmask.username)
        self.assertEqual(hostmask.hostname, "host")

    def test_only_nickname(self):
        hostmask = irctokens.Hostmask("nick")
        self.assertEqual(hostmask.nickname, "nick")
        self.assertIsNone(hostmask.username)
        self.assertIsNone(hostmask.hostname)

    def test_line(self):
        line = irctokens.tokenise(":nick!user@host PRIVMSG #channel hello")
        hostmask = irctokens.Hostmask("nick!user@host")
        self.assertEqual(line.hostmask, hostmask)
        self.assertEqual(line.hostmask.nickname, "nick")
        self.assertEqual(line.hostmask.username, "user")
        self.assertEqual(line.hostmask.hostname, "host")

    def test_none(self):
        hostmask = irctokens.Hostmask(None)
        self.assertIsNone(hostmask.nickname)
        self.assertIsNone(hostmask.username)
        self.assertIsNone(hostmask.hostname)
