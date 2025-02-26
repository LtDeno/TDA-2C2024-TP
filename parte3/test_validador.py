import validador


assert validador.validar( [1, 2, 2, 2, 2, 1],
                          [3, 3, 0, 1, 1],
                          [3, 1, 0, 3, 3],
                          {0: None, 1: [(0, 1), (0, 0)], 2: [(1, 3), (0, 3)], 3: [(4, 0), (3, 0)], 4: None, 5: None}) == False
assert validador.validar([4, 3, 3, 2, 2, 2, 1, 1, 1, 1],
                         [3, 2, 2, 4, 2, 1, 1, 2, 3, 0],
                         [1, 2, 1, 3, 2, 2, 3, 1, 5, 0],
                         {0: [(3, 8), (0, 8)], 1: [(2, 6), (0, 6)], 2: [(8, 5), (8, 3)], 3: [(3, 1), (3, 0)], 4: [(4, 3), (3, 3)], 5: [(7, 8), (7, 7)], 6: [(0, 2), (0, 2)], 7: [(4, 5), (4, 5)], 8: [(5, 1), (5, 1)], 9: [(6, 4), (6, 4)]}) == True
assert validador.validar([10, 6, 6, 11, 14, 15, 8, 10, 1, 14, 7, 6, 16, 13, 16, 12, 1, 12, 5, 10, 4, 14, 13, 12, 4],
                         [3, 11, 11, 1, 2, 5, 4, 10, 5, 2, 12, 6, 12, 7, 0, 2, 0, 8, 10, 11, 6, 10, 0, 11, 5, 8, 6, 9, 8, 0],
                         [3, 12, 1, 5, 14, 15, 6, 11, 2, 10, 12, 10, 6, 2, 7, 1, 5, 11, 5, 10, 7, 11, 4, 0, 5],
                         {0: [(13, 1), (4, 1)], 1: [(7, 21), (7, 16)], 2: [(10, 21), (10, 16)], 3: [(12, 19), (12, 9)], 4: None, 5: None, 6: [(23, 7), (23, 0)], 7: [(18, 12), (18, 3)], 8: [(0, 0), (0, 0)], 9: None, 10: [(1, 22
                                                                                                                                                                                                                             ), (1, 16)], 11: [(17, 21), (17, 16)], 12: None, 13: None, 14: None, 15: [(11, 4), (0, 4)], 16: [(0, 6), (0, 6)], 17: None, 18: [(27, 9), (23, 9)], 19: [(21, 14), (21, 5)], 20: [(2, 12), (2, 9)], 21: None, 22: None, 23: None, 24: [(8, 7), (5, 7)]}) == False
