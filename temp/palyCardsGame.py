# -*- coding:UTF-8 -*-
import random


# True_cards = [1: 'A', 2, 3, 4, 5, 6, 7, 8, 9, 10, 11: 'J', 12: 'Q', 13: 'K']
True_cards = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13]
sub_cards = ['King', 'Kinglet']   # 大王、小王
color = ['heart', 'diamond', 'club', 'spade']   # 红桃、方块、梅花、黑桃

whole_cards = ["{}_{}".format(j, i) for i in color for j in True_cards] + sub_cards

def shuffle_cards(cards):
    random.shuffle(cards)
    return cards

# def push_cards(num=3):
    # for i in range(num):
    #     if i == 0:
    #         mine_cards = []
    #     card_partner_1 = []
    #     card_partner_2 = []
    # card_mine = []
    # card_partner_1 = []
    # card_partner_1 = []

card_mine = []
card_partner_1 = []
card_partner_2 = []

shuffle_cards(whole_cards)
while len(whole_cards) > 3:
    card_mine.append(whole_cards.pop())
    card_partner_1.append(whole_cards.pop())
    card_partner_2.append(whole_cards.pop())

print(card_mine, card_partner_1, card_partner_2, sep='\n')