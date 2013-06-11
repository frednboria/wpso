
# parsetab.py
# This file is automatically generated. Do not edit.
_tabversion = '3.2'

_lr_method = 'LALR'

_lr_signature = '\xe74\xc6\xfa\xe0\xe5\xac(\x1f\xfb\xfb\\\x01\r\x90\xe4'
    
_lr_action_items = {'WORD':([5,9,10,12,17,19,21,25,],[11,11,11,11,11,11,11,11,]),'SEMICOLON':([4,7,18,26,28,],[6,-4,-5,-6,-7,]),'INSTRUCTION':([0,1,3,6,],[-1,2,-2,-3,]),'NUMBER':([5,9,10,12,17,19,21,25,],[8,8,8,8,8,8,8,8,]),'OPERATOR':([8,11,13,14,15,16,20,22,23,24,27,],[-9,-8,17,-12,17,17,-13,-11,17,17,17,]),'COMMA':([8,11,13,14,16,20,22,23,24,],[-9,-8,19,-12,21,-13,-11,25,-10,]),'LPAREN':([2,5,9,10,12,17,19,21,25,],[5,10,10,10,10,10,10,10,10,]),'NOT':([5,9,10,12,17,19,21,25,],[9,9,9,9,9,9,9,9,]),'RPAREN':([5,8,11,13,14,15,20,22,23,24,27,],[7,-9,-8,18,-12,20,-13,-11,26,-10,28,]),'QUANTIFIER':([5,9,10,12,17,19,21,25,],[12,12,12,12,12,12,12,12,]),'$end':([0,1,3,6,],[-1,0,-2,-3,]),}

_lr_action = { }
for _k, _v in _lr_action_items.items():
   for _x,_y in zip(_v[0],_v[1]):
      if not _x in _lr_action:  _lr_action[_x] = { }
      _lr_action[_x][_k] = _y
del _lr_action_items

_lr_goto_items = {'explist':([0,],[1,]),'args':([2,],[4,]),'expression':([5,9,10,12,17,19,21,25,],[13,14,15,16,22,23,24,27,]),'instr':([1,],[3,]),}

_lr_goto = { }
for _k, _v in _lr_goto_items.items():
   for _x,_y in zip(_v[0],_v[1]):
       if not _x in _lr_goto: _lr_goto[_x] = { }
       _lr_goto[_x][_k] = _y
del _lr_goto_items
_lr_productions = [
  ("S' -> explist","S'",1,None,None,None),
  ('explist -> <empty>','explist',0,'p_explist','/home/fred/project/wpso/logic/engine/parser.py',8),
  ('explist -> explist instr','explist',2,'p_explist','/home/fred/project/wpso/logic/engine/parser.py',9),
  ('instr -> INSTRUCTION args SEMICOLON','instr',3,'p_instr','/home/fred/project/wpso/logic/engine/parser.py',18),
  ('args -> LPAREN RPAREN','args',2,'p_args','/home/fred/project/wpso/logic/engine/parser.py',23),
  ('args -> LPAREN expression RPAREN','args',3,'p_args','/home/fred/project/wpso/logic/engine/parser.py',24),
  ('args -> LPAREN expression COMMA expression RPAREN','args',5,'p_args','/home/fred/project/wpso/logic/engine/parser.py',25),
  ('args -> LPAREN expression COMMA expression COMMA expression RPAREN','args',7,'p_args','/home/fred/project/wpso/logic/engine/parser.py',26),
  ('expression -> WORD','expression',1,'p_expression_wordornumber','/home/fred/project/wpso/logic/engine/parser.py',37),
  ('expression -> NUMBER','expression',1,'p_expression_wordornumber','/home/fred/project/wpso/logic/engine/parser.py',38),
  ('expression -> QUANTIFIER expression COMMA expression','expression',4,'p_expression_quantifier','/home/fred/project/wpso/logic/engine/parser.py',42),
  ('expression -> expression OPERATOR expression','expression',3,'p_expression_op','/home/fred/project/wpso/logic/engine/parser.py',46),
  ('expression -> NOT expression','expression',2,'p_expression_not','/home/fred/project/wpso/logic/engine/parser.py',50),
  ('expression -> LPAREN expression RPAREN','expression',3,'p_expression_group','/home/fred/project/wpso/logic/engine/parser.py',54),
]
