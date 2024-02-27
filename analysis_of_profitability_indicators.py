
lang = input('Choose language(ru/en): ')

if lang != 'ru' and lang != 'en':
    print("Wrong language!!!")


import ru_local as ru
import en_local as en


if lang == 'ru':
    input_revenue = ru.REVENUE_INPUT
    input_cost = ru.TYPE_COST_INPUT
    input_amount = ru.AMOUNT_INPUT
    output_revenue = ru.REVENUE_OUTPUT
    output_total_cost = ru.TOTAL_COST
    output_profit = ru.PROFIT
    output_profitability = ru.PROFITABILITY

if lang == 'en':
    input_revenue = en.REVENUE_INPUT
    input_cost = en.TYPE_COST_INPUT
    input_amount = en.AMOUNT_INPUT
    output_revenue = en.REVENUE_OUTPUT
    output_total_cost = en.TOTAL_COST
    output_profit = en.PROFIT
    output_profitability = en.PROFITABILITY


def work_with_indicators():
    revenue = float(input(f'{input_revenue}: \n'))
    cost = {}
    while True:
        type_cost = input(f'{input_cost}: \n')
        if type_cost.lower() == 'done' or 'готово':
            break
        amount = float(input(f'{input_amount} {type_cost}: \n'))
        cost[type_cost] = amount
    total_cost = sum(cost.values())
    profit = revenue - total_cost
    profitability = (profit/total_cost)
    print(f'{output_revenue} = {revenue}\n {output_total_cost} = {total_cost}\n {output_profit} = {profit}\n {output_profitability} = {profitability:.0%}')


work_with_indicators()


