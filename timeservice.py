# Copyright 2016 Daniel Estevez <daniel@destevez.net>.
# 
# This is free software; you can redistribute it and/or modify
# it under the terms of the GNU General Public License as published by
# the Free Software Foundation; either version 3, or (at your option)
# any later version.
# 
# This software is distributed in the hope that it will be useful,
# but WITHOUT ANY WARRANTY; without even the implied warranty of
# MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.  See the
# GNU General Public License for more details.
# 
# You should have received a copy of the GNU General Public License
# along with this software; see the file COPYING.  If not, write to
# the Free Software Foundation, Inc., 51 Franklin Street,
# Boston, MA 02110-1301, USA.

"""Outernet time service receiver

Receives time packets in the Outernet service
"""

__author__ = 'Daniel Estevez'
__copyright__ = 'Copyright 2016, Daniel Estevez'
__license__ = 'GPLv3'
__maintainer__ = 'Daniel Estevez'
__email__ = 'daniel@destevez.net'


import datetime
import struct

class TimeService:
    """
    Packet handler for Outernet time service

    Gets time packets from LDPRouter() and prints them
    """
    def __init__(self, router):
        """
        Initialize time service handler

        Args:
          router (LDPRouter): LDP router to get packets from
        """
        router.register(self.__get, 0x8100, 0x0104)

    def __get(self, packet):
        """
        Time packet handler

        Prints the timestamp in the packet

        Args:
          packet (LDP): the LDP time packet
        """
        timestamp = datetime.datetime.utcfromtimestamp(struct.unpack('>I', packet.payload[10:14])[0])
        groundstation = str(packet.payload[:4], 'utf-8')
        print('[Time service] Received time packet from {}: {} UTC'.format(groundstation,timestamp))
