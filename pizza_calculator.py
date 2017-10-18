# made by malcolm mccarthy
# in oct 2017
# calculates cost of a pizza with various sizes and toppings
import ui


LARGE = 6
EXTRA_LARGE = 10
HST = 0.13

#toppings_amount = int(view['toppings_textfield'].text)

def calculate_button(sender):
     # calculates cost of the toppings
     number_of_toppings = int(view['toppings_textfield'].text)
     if int(view['toppings_textfield'].text) == 0:
        toppings_cost = 0 
        
     elif int(view['toppings_textfield'].text) == 1:
        toppings_cost = 1 
        
     else:
        toppings_cost = (number_of_toppings * 0.75) + 0.25
     
     # calculates cost of pizza. first, just subtotal, then, HST, then total cost
     if int(view['size_textfield'].text) == 1:
        pizza_size = LARGE
        subtotal = pizza_size + toppings_cost
        view['sub_total_label'].text = "subtotal is: " + '${:,.2F}'.format(subtotal)
        cost_of_HST = (HST * subtotal) 
        view['HST_label'].text = "HST is: " + '${:,.2F}'.format(cost_of_HST)
        total_cost = cost_of_HST + subtotal
        view['total_cost_label'].text = "Total cost is:" + '${:,.2F}'.format(total_cost)
     else:
        int(view['size_textfield'].text) == 2
        pizza_size = EXTRA_LARGE
        subtotal = pizza_size + toppings_cost
        view['sub_total_label'].text = "subtotal is: " + '${:,.2F}'.format(subtotal)
        cost_of_HST = (HST * subtotal) 
        view['HST_label'].text = "HST is: " + '${:,.2F}'.format(cost_of_HST)
        total_cost = cost_of_HST + subtotal
        view['total_cost_label'].text = "Total cost is:" + '${:,.2F}'.format(total_cost)

view = ui.load_view()
view.present('sheet')
