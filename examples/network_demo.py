# file: network_demo.py
#

# import modules
#
import sys
from tgdhstruct.member_agent import MemberAgent

# function: main
#
def main(argv):

    # create an initial tree
    #
    group_tree = MemberAgent(int(argv[1]))

    # demonstrate a join event
    #
    group_tree.join_protocol()

    # do another join
    #
    group_tree.join_protocol()

    # exit gracefully
    #
    group_tree.close()

# begin gracefully
#
if __name__ == '__main__':
    main(sys.argv)

#
# end file: network_demo.py