milk = 5
eggs = 3
coffee = 10

# Outputs should be:
# -->  "The Total Cost: $<total-of-items>"
# --> "Final Amount after 10% discount: $<total-with-discount>"
total_cost = milk + eggs + coffee
print(f' The total cost : $ {total_cost}')
discount = 0.10
amountToSubtract = total_cost * discount
final_amount = total_cost - amountToSubtract
print(f'Final Amount after 10% discount: $ {final_amount}')