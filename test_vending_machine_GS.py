"""
Gouravjeet Singh (Fall 2024)
# Student id- 100920691

This program is strictly my own work. Any material
beyond course learning materials that is taken from
the Web or other sources is properly cited, giving.
credit to the original author(s)

For the 'vending_machine_Gs.py' script - WORKS
 """

from vending_machine_GS import VendingMachine, WaitingState, AddCoinsState, DeliverProductState, CountChangeState

def test_VendingMachine():
# new machine object
     vending = VendingMachine()

 # Add the states - ORG
     vending.add_state(WaitingState())
     vending.add_state(AddCoinsState())
     vending.add_state(DeliverProductState())
     vending.add_state(CountChangeState())

 # My revisions
     vending.add_state(WaitingState())
     vending.add_state(AddCoinsState())
     vending.add_state(DeliverProductState())
     vending.add_state(CountChangeState())


 # Reset state is "waiting for first coin"
     vending.go_to_state('waiting')
     assert vending.state.name == 'waiting'

 # test that the first coin causes a transition to 'coins'
     vending.event = '$2' # a twonie
     vending.update()
     assert vending.state.name == 'add_coins'
     assert vending.amount == 200 # pennies, was .total
     
     vending.event = '$1' # a “loonie”
     vending.update()
     assert vending.state.name == 'add_coins'
     assert vending.amount == 300 # Total amount is now 300 pennies (200 + 100)
     
     vending.event = '¢25' # a “quarter”
     vending.update()
     assert vending.state.name == 'add_coins'
     assert vending.amount == 325 # Total amount is now 325 pennies (300 + 25)

     
     vending.event = '¢10' # a “dime”
     vending.update()
     assert vending.state.name == 'add_coins'
     assert vending.amount == 335 # Total amount is now 335 pennies (325 + 10)

     
     vending.event = '¢5' # a “nickel”
     vending.update()
     assert vending.state.name == 'add_coins'
     assert vending.amount == 340 # Total amount is now 340 pennies (335 + 5)

