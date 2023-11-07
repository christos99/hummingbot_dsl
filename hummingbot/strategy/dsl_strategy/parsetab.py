
# parsetab.py
# This file is automatically generated. Do not edit.
# pylint: disable=W,C,R
_tabversion = '3.10'

_lr_method = 'LALR'

_lr_signature = 'nonassocBUYSELLnonassocIFleftORleftANDrightNOTnonassocLTLEGTGEEQleftCROSSOVERSMAEMARSIAND BALANCE BUY COMMA CROSSOVER EMA EQ GE GT IF LE LPAREN LT NOT NUMBER OR PRICE RPAREN RSI SELL SMA VOLUMEcommand : BUY IF condition\n               | SELL IF conditioncondition : expression\n                 | NOT condition\n                 | condition AND condition\n                 | condition OR conditionexpression : PRICE\n                  | VOLUME\n                  | BALANCE\n                  | NUMBER\n                  | function_call\n                  | expression LT expression\n                  | expression LE expression\n                  | expression GT expression\n                  | expression GE expression\n                  | expression EQ expressionfunction_call : CROSSOVER LPAREN expression COMMA expression RPAREN\n                     | SMA LPAREN NUMBER RPAREN\n                     | EMA LPAREN NUMBER RPAREN\n                     | RSI LPAREN NUMBER RPARENexpression : LPAREN condition RPAREN'
    
_lr_action_items = {'BUY':([0,],[2,]),'SELL':([0,],[3,]),'$end':([1,6,7,9,10,11,12,13,19,27,33,34,35,36,37,38,39,40,46,47,48,50,],[0,-1,-3,-7,-8,-9,-10,-11,-2,-4,-5,-6,-12,-13,-14,-15,-16,-21,-18,-19,-20,-17,]),'IF':([2,3,],[4,5,]),'NOT':([4,5,8,14,20,21,],[8,8,8,8,8,8,]),'PRICE':([4,5,8,14,20,21,22,23,24,25,26,29,45,],[9,9,9,9,9,9,9,9,9,9,9,9,9,]),'VOLUME':([4,5,8,14,20,21,22,23,24,25,26,29,45,],[10,10,10,10,10,10,10,10,10,10,10,10,10,]),'BALANCE':([4,5,8,14,20,21,22,23,24,25,26,29,45,],[11,11,11,11,11,11,11,11,11,11,11,11,11,]),'NUMBER':([4,5,8,14,20,21,22,23,24,25,26,29,30,31,32,45,],[12,12,12,12,12,12,12,12,12,12,12,12,42,43,44,12,]),'LPAREN':([4,5,8,14,15,16,17,18,20,21,22,23,24,25,26,29,45,],[14,14,14,14,29,30,31,32,14,14,14,14,14,14,14,14,14,]),'CROSSOVER':([4,5,8,14,20,21,22,23,24,25,26,29,45,],[15,15,15,15,15,15,15,15,15,15,15,15,15,]),'SMA':([4,5,8,14,20,21,22,23,24,25,26,29,45,],[16,16,16,16,16,16,16,16,16,16,16,16,16,]),'EMA':([4,5,8,14,20,21,22,23,24,25,26,29,45,],[17,17,17,17,17,17,17,17,17,17,17,17,17,]),'RSI':([4,5,8,14,20,21,22,23,24,25,26,29,45,],[18,18,18,18,18,18,18,18,18,18,18,18,18,]),'AND':([6,7,9,10,11,12,13,19,27,28,33,34,35,36,37,38,39,40,46,47,48,50,],[20,-3,-7,-8,-9,-10,-11,20,-4,20,-5,20,-12,-13,-14,-15,-16,-21,-18,-19,-20,-17,]),'OR':([6,7,9,10,11,12,13,19,27,28,33,34,35,36,37,38,39,40,46,47,48,50,],[21,-3,-7,-8,-9,-10,-11,21,-4,21,-5,-6,-12,-13,-14,-15,-16,-21,-18,-19,-20,-17,]),'RPAREN':([7,9,10,11,12,13,27,28,33,34,35,36,37,38,39,40,42,43,44,46,47,48,49,50,],[-3,-7,-8,-9,-10,-11,-4,40,-5,-6,-12,-13,-14,-15,-16,-21,46,47,48,-18,-19,-20,50,-17,]),'LT':([7,9,10,11,12,13,35,36,37,38,39,40,41,46,47,48,49,50,],[22,-7,-8,-9,-10,-11,None,None,None,None,None,-21,22,-18,-19,-20,22,-17,]),'LE':([7,9,10,11,12,13,35,36,37,38,39,40,41,46,47,48,49,50,],[23,-7,-8,-9,-10,-11,None,None,None,None,None,-21,23,-18,-19,-20,23,-17,]),'GT':([7,9,10,11,12,13,35,36,37,38,39,40,41,46,47,48,49,50,],[24,-7,-8,-9,-10,-11,None,None,None,None,None,-21,24,-18,-19,-20,24,-17,]),'GE':([7,9,10,11,12,13,35,36,37,38,39,40,41,46,47,48,49,50,],[25,-7,-8,-9,-10,-11,None,None,None,None,None,-21,25,-18,-19,-20,25,-17,]),'EQ':([7,9,10,11,12,13,35,36,37,38,39,40,41,46,47,48,49,50,],[26,-7,-8,-9,-10,-11,None,None,None,None,None,-21,26,-18,-19,-20,26,-17,]),'COMMA':([9,10,11,12,13,35,36,37,38,39,40,41,46,47,48,50,],[-7,-8,-9,-10,-11,-12,-13,-14,-15,-16,-21,45,-18,-19,-20,-17,]),}

_lr_action = {}
for _k, _v in _lr_action_items.items():
   for _x,_y in zip(_v[0],_v[1]):
      if not _x in _lr_action:  _lr_action[_x] = {}
      _lr_action[_x][_k] = _y
del _lr_action_items

_lr_goto_items = {'command':([0,],[1,]),'condition':([4,5,8,14,20,21,],[6,19,27,28,33,34,]),'expression':([4,5,8,14,20,21,22,23,24,25,26,29,45,],[7,7,7,7,7,7,35,36,37,38,39,41,49,]),'function_call':([4,5,8,14,20,21,22,23,24,25,26,29,45,],[13,13,13,13,13,13,13,13,13,13,13,13,13,]),}

_lr_goto = {}
for _k, _v in _lr_goto_items.items():
   for _x, _y in zip(_v[0], _v[1]):
       if not _x in _lr_goto: _lr_goto[_x] = {}
       _lr_goto[_x][_k] = _y
del _lr_goto_items
_lr_productions = [
  ("S' -> command","S'",1,None,None,None),
  ('command -> BUY IF condition','command',3,'p_command','parser_dsl.py',20),
  ('command -> SELL IF condition','command',3,'p_command','parser_dsl.py',21),
  ('condition -> expression','condition',1,'p_condition','parser_dsl.py',26),
  ('condition -> NOT condition','condition',2,'p_condition','parser_dsl.py',27),
  ('condition -> condition AND condition','condition',3,'p_condition','parser_dsl.py',28),
  ('condition -> condition OR condition','condition',3,'p_condition','parser_dsl.py',29),
  ('expression -> PRICE','expression',1,'p_expression','parser_dsl.py',41),
  ('expression -> VOLUME','expression',1,'p_expression','parser_dsl.py',42),
  ('expression -> BALANCE','expression',1,'p_expression','parser_dsl.py',43),
  ('expression -> NUMBER','expression',1,'p_expression','parser_dsl.py',44),
  ('expression -> function_call','expression',1,'p_expression','parser_dsl.py',45),
  ('expression -> expression LT expression','expression',3,'p_expression','parser_dsl.py',46),
  ('expression -> expression LE expression','expression',3,'p_expression','parser_dsl.py',47),
  ('expression -> expression GT expression','expression',3,'p_expression','parser_dsl.py',48),
  ('expression -> expression GE expression','expression',3,'p_expression','parser_dsl.py',49),
  ('expression -> expression EQ expression','expression',3,'p_expression','parser_dsl.py',50),
  ('function_call -> CROSSOVER LPAREN expression COMMA expression RPAREN','function_call',6,'p_function_call','parser_dsl.py',58),
  ('function_call -> SMA LPAREN NUMBER RPAREN','function_call',4,'p_function_call','parser_dsl.py',59),
  ('function_call -> EMA LPAREN NUMBER RPAREN','function_call',4,'p_function_call','parser_dsl.py',60),
  ('function_call -> RSI LPAREN NUMBER RPAREN','function_call',4,'p_function_call','parser_dsl.py',61),
  ('expression -> LPAREN condition RPAREN','expression',3,'p_expression_group','parser_dsl.py',69),
]