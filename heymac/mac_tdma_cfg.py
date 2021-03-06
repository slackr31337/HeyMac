# A time slot (Tslot) is a window of time to complete a 256 byte frame
# and an acknowledgement frame.  The HeyMac TDMA protocol uses a whole number
# of Tslots within one second.
TSLOTS_PER_SEC = 4

# The log2 of the number of consecutive Tslots that form a superframe (Sframe).
# In other words, 2^FRAME_SPEC_SF_ORDER == Tslots per Sframe.
# This value MUST fit within 4 bits in the Frame Spec.
# There must be enough Tslots so that every node in a two-hop range
# can own at least one Tslots in the Sframe.
FRAME_SPEC_SF_ORDER = 7

# The log2 of the number of consecutive Sframes between a node's extended beacon.
# In other words, 2^FRAME_SPEC_EB_ORDER * 2^FRAME_SPEC_SF_ORDER == Tslots per extd_bcn.
# This value MUST fit within 3 bits in the Frame Spec.
# This value SHOULD be large enough so that nodes transmit standard beacons
# regularly and extended beacons rarely.
# This value SHOULD be small enough that an extended beacon is transmitted
# at least once every 10 minutes (to comply with FCC identification regulations).
#
# The recommended value (4) is intended to be used with FRAME_SPEC_SF_ORDER = 7
# so that an Sframe is 32s in duration and an EBcn is transmitted
# roughly every 8.5 minutes.
FRAME_SPEC_EB_ORDER = 4

# The amount of time before the start of a Tslot to activate the software
# so it can decide what to do and perform any preparation so the radio action
# happens as close to the start of a Tslot as possible.
# The following value was determined through experimentation.
# It should be great enough to prevent a busy system from missing the time
# and small enough to not block for a significant amount of time.
TSLOT_PREP_TIME = 0.020 # secs

# The amount of time [seconds] since the reception of a PPS signal
# after which the timing is no longer disciplined.
# The following value is a guess and can be improved.
DSCPLN_PPS_TIMEOUT = 10.0 * 60.0 # ten minutes

# The amount of time [seconds] since the reception of a HeyMac beacon
# after which the timing is no longer disciplined.
# This value SHOULD be greater than DSCPLN_PPS_TIMEOUT to allow the weaker
# form of discipline more time to operate.
DSCPLN_BCN_TIMEOUT = 50.0 * 60.0 # fifty minutes

# The amount of time between the true start of a Beacon frame
# and the point when the receiver detects reception via DIO3/ValidHeader.
# This time must be accounted for by Beacon discipline.
# This time was determined by comparing 1 receiver's log file:
#   2018-04-25 23:13:42,998 pps            898898.480569
#   2018-04-25 23:13:43,394 rx_time        898898.748040    RXD 139 bytes...
TIME_TO_VALID_HEADER = 0.0175

# The number of Sframes a node should remain in the Listening state
# before transitioning to a state which allows transmitting.
# A decent value is 2.  A smaller value is used for debugging.
N_SFRAMES_TO_LISTEN = 2
